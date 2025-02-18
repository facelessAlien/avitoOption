import time
import urllib.parse
import requests
from bs4 import BeautifulSoup

# Селекторы
NAME = "h1"
DESCRIPTIONS = "meta[itemprop='description']"
DESCRIPTIONS_FULL_PAGE = "[data-marker='item-view/item-description']"
URL = "[itemprop='url']"
PRICE = "[itemprop='price']"
TOTAL_VIEWS = "[data-marker='item-view/total-views']"
PARAMS = "[data-marker='item-view/item-params']"
DATE_PUBLIC = "[data-marker='item-view/item-date']"
SELLER_NAME = "[data-marker='seller-info/label']"
SELLER_LINK = "[data-marker='seller-link/link']"
COMPANY_NAME = "[data-marker='seller-link/link']"
COMPANY_NAME_TEXT = "span"
ADDRESS = "div[class*='style-item-address']"

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

def card_info(thread, driver, total_urls: list, tg_token: str = None, chat_id: str = None, requests_pause: int = 0):
    """Собираем информацию с карточки товара с возможностью остановки"""
    print(f'\n\n{"+" * 25} ЗАПУСК СБОРА ИНФОРМАЦИИ ПО КАРТЕ ТОВАРА {"+" * 25}\n')
    print("🔸" * 50 + '\n\n')
    for total_url in total_urls:
        if not thread.running:
            print("⚠️ Остановка сбора информации по карточкам товаров...")
            return
        print(f"⏳ Ожидание {requests_pause} секунд перед следующим обновлением...")
        time.sleep(requests_pause)
        driver.get(total_url)

        # Получаем и декодируем исходный код страницы
        while True:
            if not thread.running:
                print("⚠️ Остановка сбора информации по карточкам товаров...")
                return

            decoded_html = urllib.parse.unquote(driver.page_source)
            soup = BeautifulSoup(decoded_html, "lxml")
            h2_element = soup.find('h2')

            # Если нет <h2> или в нём нет 'IP' — выходим из цикла
            if not h2_element or 'IP' not in h2_element.text:
                break

            # Иначе перезагружаем страницу
            print("⚠️ Обнаружена защита Avito (IP). Обновляем страницу каждые 3 секунды...")
            driver.refresh()
            time.sleep(3)  # Небольшая пауза перед следующей проверкой)

        # Название
        title_element = soup.select_one(NAME)
        title = title_element.text.strip() if title_element else "Нет названия"

        # Цена
        price_element = soup.select_one(PRICE)
        price = price_element.text.strip() if price_element else "Цена не указана"

        # характеристики
        characteristic_element = soup.select_one(PARAMS)
        characteristic = characteristic_element.text if characteristic_element else 'Характеристика отсутствует'

        # URL объявления
        url_element = soup.select_one(URL)
        url = url_element['content'] if url_element and url_element.has_attr('content') else total_url

        # Описание
        desc_meta = soup.select_one(DESCRIPTIONS_FULL_PAGE).find_all('p')
        description_meta = []
        for d in desc_meta:
            try:
                description_meta.append(d.text)
            except:
                continue
        description_meta = description_meta if description_meta else 'не найдено'
        total_views_element = soup.select_one(TOTAL_VIEWS)
        total_views = total_views_element.text.strip() if total_views_element else "Нет данных"

        date_public_element = soup.select_one(DATE_PUBLIC)
        date_public = date_public_element.text.strip() if date_public_element else "Нет даты"

        seller_element = soup.select_one(SELLER_NAME)
        seller_name = seller_element.text.strip() if seller_element else "Продавец не указан"

        seller_link_element = soup.select_one(SELLER_LINK)
        seller_link = 'https://www.avito.ru' + seller_link_element[
            'href'] if seller_link_element and seller_link_element.has_attr('href') else "Нет ссылки"

        company_element = soup.select_one(COMPANY_NAME)
        company_name = company_element.text.strip() if company_element else "Частное лицо"

        address_element = soup.select_one(ADDRESS)
        address = address_element.text.strip() if address_element else "Местоположение неизвестно"
        unpack_desc = "\n".join(description_meta)
        # Вывод в GUI и консоль
        parsed_text = f"""
        <b><font color="yellow">Название:</font></b> {title} <br>
        <b><font color="yellow">Цена:</font></b> {price} <br>
        <b><font color="yellow">Характеристика:</font></b> {characteristic} <br>
        <b><font color="yellow">Описание:</font></b> {unpack_desc} <br>
        <b><font color="yellow">Просмотры:</font></b> {total_views} <br>
        <b><font color="yellow">Дата публикации:</font></b> {date_public} <br>
        <b><font color="yellow">Продавец:</font></b> {seller_name} <br>
        <b><font color="yellow">Ссылка на продавца:</font></b> {seller_link} <br>
        <b><font color="yellow">Компания:</font></b> {company_name} <br>
        <b><font color="yellow">Адрес:</font></b> {address} <br>
        <b><font color="yellow">URL объявления:</font></b> {url}
        """

        print(parsed_text)


        # Формируем данные для сохранения
        parsed_data = {
            "Название": title,
            "Цена": price,
            "Характеристика": characteristic,
            "Описание": unpack_desc,
            "Просмотры": total_views,
            "Дата публикации": date_public,
            "Продавец": seller_name,
            "Ссылка на продавца": seller_link,
            "Компания": company_name,
            "Адрес": address,
            "URL": url
        }

        thread.data_collected.emit(parsed_data)  # Отправляем данные в GUI
        if tg_token:
            # 📌 Отправляем данные в Telegram, разбивая сообщение на части
            send_message_to_telegram(parsed_text, tg_token, chat_id)
        print('                      ')
        print("🔸" * 50 + '\n\n')

