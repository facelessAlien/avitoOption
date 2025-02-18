import json

# Путь к конфигурационному файлу
CONFIG_FILE = "config.json"


def load_config():
    """Загружаем конфиг из JSON-файла"""
    try:
        with open(CONFIG_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}  # Если файл не найден или поврежден, возвращаем пустой словарь


def save_config(data):
    """Сохраняем конфиг в JSON-файл"""
    with open(CONFIG_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
