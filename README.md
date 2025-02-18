# 🛍️ avitoOption — Мощный парсер Avito

📢 **avitoOption** — это гибкий и мощный парсер объявлений Avito, который поддерживает мониторинг, работу через прокси, отправку данных в Telegram, выбор категорий и сохранение информации в JSON/XLSX.
Этот проект вдохновлен [Duff89/parser_avito](https://github.com/Duff89/parser_avito)
## 🚀 Основные возможности

- 🔹 **Обычный режим** – парсер проходит заданное количество страниц и собирает объявления.
- 🔹 **Режим мониторинга** – парсер периодически проверяет новые объявления и изменения цен.
- 🔹 **Детальный режим** – парсер заходит в карточки товаров и извлекает подробную информацию.
- 🔹 **Поддержка прокси** – рекомендуется использовать ротационные прокси с IP-адресами СНГ.
- 🔹 **Отправка уведомлений в Telegram** – передача данных в реальном времени.
- 🔹 **Выбор категорий** – возможность более точного поиска в конкретных категориях.
- 🔹 **Фильтры** – ключевые слова, черный список, ценовой диапазон, выбор города.
- 🔹 **Сохранение данных** – JSON и Excel (XLSX).
- 🔹 **Графический интерфейс** – удобное управление всеми настройками.

---

## 🔑 Категории
Для более точного поиска можно выбрать категорию **прямо в программе**.  
На момент выхода добавлены **все существующие категории Avito**.

### 📂 Примеры категорий:
- 📱 **Электроника** – `/bytovaya_elektronika`
- 🚗 **Транспорт** – `/transport`
- 🏠 **Недвижимость** – `/nedvizhimost`
- 🎣 **Охота и рыбалка** – `/ohota_i_rybalka`

---

## 📡 Отправка данных в Telegram
Чтобы получать данные о найденных объявлениях в **Telegram**, выполните следующие шаги:

1. **Создайте бота** через [@BotFather](https://t.me/BotFather).
2. **Получите API-токен** после создания бота.
3. **Узнайте ваш `chat_id`** через [@userinfobot](https://t.me/userinfobot).
```json
"telegram_bot_token": "TOKEN::CHAT_ID",
"send_tg": true
```
## 🛠️ Установка

### 🔹 1. Установка через исходный код
> **Требования:** Python 3.10+ и `pip`

```sh
git clone https://github.com/username/avitoOption.git
cd avitoOption
python -m venv venv
source venv/bin/activate  # Для Linux/macOS
venv\Scripts\activate      # Для Windows
pip install -r requirements.txt
python avitoOption.py
```
