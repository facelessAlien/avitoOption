from driver_config import make_driver
from get_card_urls import get_urls, encode_url
from deep_card_info import card_info
import json
import os


def find_category_file(categories):
    """Ищет файл, в котором содержится значение categories"""
    directory = "categories"  # Директория с JSON-файлами

    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            filepath = os.path.join(directory, filename)
            try:
                with open(filepath, "r", encoding="utf-8") as file:
                    data = json.load(file)
                    if categories in data.values():  # Проверяем, есть ли значение в файле
                        return os.path.splitext(filename)[0]  # Возвращаем имя файла без .json
            except (json.JSONDecodeError, FileNotFoundError):
                print(f"⚠ Ошибка чтения файла {filename}")

    return None  # Если ничего не найдено


def run(thread):
    """Запускаем парсер с возможностью мгновенной остановки"""

    with open(r"config.json", "r", encoding="utf-8") as file:
        config = json.load(file)

    ##### НАСТРОЙКИ ЗАПРОСА #####
    city = config["city"]
    user_response = config["user_response"]
    categories = config['categories']
    keywords = config["keywords"]
    black_list = config["black_list"]
    max_page = config["max_page"]
    min_price = config["min_price"]
    max_price = config["max_price"]
    deep_search = config["deep_search"]
    send_tg = config["send_tg"]
    update = config["update"]
    pause = config["pause"]
    requests_pause = config["requests_pause"]
    category_file = find_category_file(categories)
    if send_tg:
        try:
            tg_token, chat_id = config["telegram_bot_token"].split('::')[0], config["telegram_bot_token"].split('::')[1]
        except:
            tg_token, chat_id = None, None
    else:
        tg_token, chat_id = None, None
    # Настройки браузера
    headless = config.get("headless", False)
    proxies_value = config["proxy"]
    print(f'Текущие настройки:\n{"✨" * 20}'
          f'\n📍 Город: {city}'
          f'\n🔍 Запрос: {user_response}'
          f'\n🛒 Категория: {category_file if category_file else "Не указаны"}'
          f'\n🔑 Ключевые слова: {", ".join(keywords) if keywords else "Не указаны"}'
          f'\n🔐 Черный список: {", ".join(black_list) if black_list else "Не указаны"}'
          f'\n📄 Максимальное количество страниц: {max_page}'
          f'\n💰 Цена: от {min_price}₽ до {max_price}₽'
          f'\n🛠️ Глубокий парсинг: {"Включен" if deep_search else "Выключен"}'
          f'\n📤 Отправка в Telegram: {"Включена" if send_tg else "Выключена"}'
          f'\n🔄 Обновления: {"Включены" if update else "Выключены"}'
          f'\n📡 Прокси: {proxies_value if proxies_value else "Не используется"}'
          f'\n🖥️ Режим браузера: {"Без интерфейса (headless)" if headless else "С открытым окном"}'
          )

    # Добавляем строку паузы только если `update=True`
    if update:
        print(f'⏳ Пауза между обновлениями: {pause} секунд')
    if requests_pause:
        print(f'⏳ Пауза между запросами: {requests_pause} секунд')

    print(f'{"✨" * 20}\n\n')

    encode_user_response = encode_url(text=user_response)

    driver = make_driver(headless=headless, proxies_value=proxies_value)

    while thread.running:  # Проверяем, не нажал ли пользователь "Стоп"
        is_get_urls = get_urls(thread, driver, categories=categories, city=city, max_page=max_page,
                               response=encode_user_response,
                               black_list=black_list, keywords=keywords, min_price=min_price, max_price=max_price, tg_token=tg_token,
                               chat_id=chat_id,
                               update=update, pause=pause, requests_pause=requests_pause)

        if is_get_urls or not thread.running:
            break  # Если получили ссылки или нажали "Стоп" — выходим из цикла
        else:
            # print('Произошла ошибка, перезапустите программу или проверьте настройки поиска...')
            break

    if thread.running and deep_search:
        card_info(thread, driver, total_urls=is_get_urls, tg_token=tg_token, chat_id=chat_id, requests_pause=requests_pause)  # Передаём thread!

    print('\nПарсинг завершен!')
    driver.close()
    driver.quit()
