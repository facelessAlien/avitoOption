import json
import re
import os
import time
import math
import urllib.parse
import requests

from selenium.webdriver.common.by import By

from driver_config import is_element


def encode_url(text: str) -> str:
    return urllib.parse.quote(text, encoding='utf-8').replace('%20', '+')


def extract_avito_id(url):
    match = re.search(r'_(\d+)\?context', url)
    return match.group(1) if match else None


def send_message_to_telegram(text, tg_token, chat_id):
    """Функция отправки сообщения в Telegram с разбиением на части"""
    max_length = 4096  # Максимальная длина сообщения в Telegram

    if len(text) <= max_length:
        # Если сообщение короткое, отправляем его сразу
        requests.post(
            f'https://api.telegram.org/bot{tg_token}/sendMessage',
            data={'chat_id': chat_id, 'text': text}
        )
    else:
        # Если сообщение длинное, разбиваем его на части
        parts = [text[i:i + max_length] for i in range(0, len(text), max_length)]
        for part in parts:
            requests.post(
                f'https://api.telegram.org/bot{tg_token}/sendMessage',
                data={'chat_id': chat_id, 'text': part}
            )


def get_urls(thread, driver, response: str, requests_pause: int = None, categories: str = None, city: str = 'all',
             max_page: int = None,
             keywords: list = None,
             black_list: list = None,
             min_price: int = None, max_price: int = None, tg_token: str = None, chat_id: str = None,
             update: bool = False, pause: int = None) -> list:
    """
    Парсим ссылки объявлений с Avito, с возможностью обновления и паузы.
    """
    json_file = r'product_id.json'
    product_data = {}
    min_price = int(min_price)
    max_price = int(max_price)
    if update:
        if os.path.exists(json_file) and os.path.getsize(json_file) > 0:
            try:
                with open(json_file, 'r', encoding='utf-8') as file:
                    product_data = json.load(file)
            except (json.JSONDecodeError, TypeError):
                print("⚠️ Ошибка чтения product_id.json. Используем пустую базу.")
                product_data = {}
        else:
            print("⚠️ Файл product_id.json отсутствует. Будем считать базу пустой.")

    first_run = (update and (len(product_data) == 0)) or (not update)
    iteration_count = 0

    while True:
        iteration_count += 1
        print("\n" + "=" * 80)
        print(f"🔄 Итерация обновления № {iteration_count}")
        print("=" * 80 + "\n")

        total_urls = []
        if categories:
            url = f'https://www.avito.ru/{city}{categories}?p=1&q={response}'
        else:
            url = f'https://www.avito.ru/{city}?p=1&q={response}'
        driver.get(url)
        driver.refresh()
        new_data_found = False

        if not thread.running:
            return []
        if is_element(driver, 10, By.CLASS_NAME, 'no-results-title-jho0M'):
            print('🚫 Ничего не найдено по заданным фильтрам или запросу поиска. Проверьте ваш запрос и фильтры\nИщем: Похоже на то, что вы ищете')
            # return []
        if is_element(driver, 10, By.CLASS_NAME, 'page-title-count-yKVwK'):
            cards_count = int(driver.find_element(By.CLASS_NAME, 'page-title-count-yKVwK').text.replace(' ', ''))
            total_page = math.ceil(cards_count / 50)  # Всего страниц
            page_count = min(total_page, max_page) if max_page else total_page  # Учитываем max_page

            print(f'Количество найденных объявлений: {cards_count}')
            print(f'Парсим страниц: {page_count}/{total_page}\n')
        else:
            page_count = 1
            print(f'\nПарсим страниц: {page_count}\n')

        try:  # 🔹 Добавляем обработку исключений внутри for-цикла
            for page in range(1, page_count + 1):
                if page > 1:
                    print(f"⏳ Ожидание {requests_pause} секунд перед следующим обновлением...")
                    time.sleep(requests_pause)
                print(f'📄 Страница {page}/{page_count}')
                if not thread.running:
                    return []

                if categories:
                    url = f'https://www.avito.ru/{city}{categories}?p={page}&q={response}'
                else:
                    url = f'https://www.avito.ru/{city}?p={page}&q={response}'
                driver.get(url)
                for_tg = []

                if is_element(driver, 60, By.CLASS_NAME, 'items-items-pZX46'):
                    blocks = driver.find_elements(By.CLASS_NAME, 'iva-item-content-OWwoq')
                    for block in blocks:
                        if not thread.running:
                            return []
                        if is_element(driver, 60, By.TAG_NAME, 'a'):
                            try:
                                # Получаем заголовок объявления
                                title = block.find_element(By.CSS_SELECTOR, '[data-marker="item-title"]').text
                                # Если хотя бы одно слово из black_list содержится в title, пропускаем объявление
                                if black_list and any(word.lower() in title.lower() for word in black_list):
                                    # print(f"🚫 Пропущено объявление (black_list): {title}")
                                    continue

                                href = block.find_element(By.TAG_NAME, 'a').get_attribute('href')
                                try:
                                    desc = block.find_element(By.CLASS_NAME, 'iva-item-bottomBlock-FhNhY').text
                                except:
                                    desc = 'не указано'
                                # Получаем текст цены
                                # Получаем текст цены и убираем пробелы по краям
                                item_price_text = block.find_element(By.CLASS_NAME,
                                                                     'price-priceContent-kPm_N').text.strip()

                                # Если строка содержит указания на диапазон, пропускаем объявление
                                if any(x in item_price_text.lower() for x in ["от", "до", "-", "·"]):
                                    continue
                                else:
                                    # Убираем символ рубля и пробелы, затем извлекаем первую последовательность цифр
                                    clean_text = item_price_text.replace('₽', '').replace(' ', '')
                                    price_match = re.search(r'\d+', clean_text)
                                    item_price = int(price_match.group()) if price_match else None

                                # Если не удалось получить цену числом, пробуем получить ее из элемента <strong>
                                if not item_price:
                                    item_price = block.find_element(By.TAG_NAME, 'strong').text

                                title_match = any(word in title.lower() for word in keywords) if keywords else True

                                price_match = True
                                if isinstance(item_price, int):
                                    if item_price is not None:
                                        if min_price is not None and item_price < min_price:
                                            price_match = False
                                        if max_price is not None and item_price > max_price:
                                            price_match = False
                                else:
                                    item_price = item_price

                                if title_match and price_match:
                                    total_urls.append(href)
                                    product_id = extract_avito_id(href)

                                    if update and product_id:
                                        old_price = product_data.get(product_id)
                                        if product_id in product_data:
                                            if old_price is not None and item_price is not None and item_price < old_price:
                                                print(
                                                    f"📉 <b><font color='yellow'>Цена снижена!</font></b> {title} | <b><font color='yellow'>Было:</font></b> {old_price}₽ | <b><font color='yellow'>Стало:</font></b> {item_price}₽")
                                                product_data[product_id] = item_price
                                                new_data_found = True
                                            else:
                                                continue
                                        else:
                                            print(
                                                f"🆕 <b><font color='yellow'>Новое объявление!</font></b> {title} | <b><font color='yellow'>Цена:</font></b> {item_price if item_price else 'Не указана'}₽")
                                            product_data[product_id] = item_price
                                            new_data_found = True
                                    elif not update and product_id:
                                        new_data_found = True

                                    print(f"📌 {title}")
                                    print(f"📝 <b><font color='yellow'>Описание:</font></b>: {desc}")
                                    print(f"🔗 <b><font color='yellow'>Ссылка:</font></b> {href}")
                                    print(
                                        f"💰 <b><font color='yellow'>Цена:</font></b> {item_price if item_price else 'Не указана'}₽")
                                    print("-" * 50)

                                    for_tg.append(
                                        f"Название: {title}\nСсылка: {href}\nЦена: {item_price if item_price else 'Не указана'}₽\n")
                                    parsed_data = {"Название": title,
                                                   "Описание": desc,
                                                   "Цена": item_price if item_price else "Цена не указана",
                                                   "URL": href}
                                    thread.data_collected.emit(parsed_data)

                            except Exception as e:
                                print(f"❌ Ошибка при обработке объявления: {str(e)}")
                                continue

                    if for_tg and tg_token:
                        message_text = "\n".join(for_tg)
                        send_message_to_telegram(message_text, tg_token, chat_id)
                    for_tg.clear()

        except Exception as e:
            print(f"❌ Ошибка при парсинге страницы: {str(e)}")
            continue
        if update:
            if first_run:
                print("🆕 Начальное заполнение базы объявлений завершено.")
                first_run = False
            elif not new_data_found:
                print("🔹 Нет новых объявлений или изменений цен.")

            if new_data_found:
                with open(json_file, 'w', encoding='utf-8') as file:
                    json.dump(product_data, file, indent=4, ensure_ascii=False)

            print(f"✅ Объявлений найдено за итерацию: {len(total_urls)}")
        else:
            print(f"✅ Объявлений найдено: {len(total_urls)}")
            break

        print(f"⏳ Ожидание {pause} секунд перед следующим обновлением...")
        time.sleep(pause)

    return total_urls

