import json
import os

from PySide6.QtGui import QColor
from PySide6.QtWidgets import QMainWindow, QListWidgetItem

from save_and_loading import CONFIG_FILE
from ui.categories import Ui_Dialog


class CategoryWindow(QMainWindow):
    def __init__(self, main_window):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("avitoOption - Выберите категорию")

        self.main_window = main_window  # Ссылка на главное окно настроек

        # Загружаем основные категории (файлы JSON в папке "categories")
        self.categories_map = self.load_main_categories()
        self.ui.listWidget_total_categories.addItems(self.categories_map.keys())

        # Подключаем события клика
        self.ui.listWidget_total_categories.itemClicked.connect(self.load_subcategories)
        self.ui.listWidget_total_categories_2.itemClicked.connect(self.set_category)

        # Подключаем поиск по категориям
        self.ui.lineEdit_search.textChanged.connect(self.filter_categories)

        # Храним изначальный список элементов
        self.original_items = []

    def load_main_categories(self):
        """Сканирует папку 'categories' и находит все JSON-файлы, создавая карту категорий"""
        categories = {}
        categories_path = "categories"

        if os.path.exists(categories_path):
            for file in os.listdir(categories_path):
                if file.endswith(".json"):
                    category_name = file.replace(".json", "")  # Убираем .json из названия
                    categories[category_name.capitalize()] = os.path.join(categories_path, file)

        return categories

    def load_subcategories(self, item):
        """Загружает подкатегории в listWidget_total_categories_2"""
        category_name = item.text()

        if category_name in self.categories_map:
            json_path = self.categories_map[category_name]

            with open(json_path, "r", encoding="utf-8") as file:
                categories = json.load(file)

            self.ui.listWidget_total_categories_2.clear()
            self.original_items = []  # Сбрасываем сохраненные элементы

            for subcategory in categories.keys():
                list_item = QListWidgetItem(subcategory)
                self.ui.listWidget_total_categories_2.addItem(list_item)
                self.original_items.append(subcategory)  # Сохраняем для поиска

            self.current_json_path = json_path

    def set_category(self, item):
        """Устанавливает выбранную категорию в line_category и обновляет config.json"""
        with open(self.current_json_path, "r", encoding="utf-8") as file:
            categories = json.load(file)

        subcategory_name = item.text()
        if subcategory_name in categories:
            category_url = categories[subcategory_name]

            # Устанавливаем в поле line_category в главном окне
            self.main_window.ui.line_category.setText(category_url)

            # Обновляем config.json
            self.update_config(category_url)

    def update_config(self, category_url):
        """Обновляет config.json, подставляя новую категорию"""
        if os.path.exists(CONFIG_FILE):
            try:
                with open(CONFIG_FILE, "r", encoding="utf-8") as file:
                    config = json.load(file)
            except json.JSONDecodeError:
                config = {}
        else:
            config = {}

        # Обновляем значение ключа "categories"
        config["categories"] = category_url

        # Сохраняем изменения
        with open(CONFIG_FILE, "w", encoding="utf-8") as file:
            json.dump(config, file, indent=4, ensure_ascii=False)

    def filter_categories(self):
        """Фильтрует подкатегории в listWidget_total_categories_2, выделяет совпадения и прокручивает к первому найденному."""
        search_text = self.ui.lineEdit_search.text().strip().lower()
        found_items = []
        count = self.ui.listWidget_total_categories_2.count()

        for i in range(count):
            item = self.ui.listWidget_total_categories_2.item(i)

            if not search_text:
                # Сбрасываем фон и цвет текста
                item.setBackground(QColor("transparent"))
                item.setForeground(QColor("white"))  #
            else:
                if search_text in item.text().lower():
                    item.setBackground(QColor("#FFD700"))  # Жёлтый фон
                    item.setForeground(QColor("black"))
                    found_items.append(item)
                else:
                    item.setBackground(QColor("transparent"))
                    item.setForeground(QColor("white"))

        if found_items:
            self.ui.listWidget_total_categories_2.scrollToItem(found_items[0])

    def reset_category_colors(self):
        """Сбрасывает все выделения, если строка поиска пустая"""
        self.ui.listWidget_total_categories_2.clear()
        for item_text in self.original_items:
            self.ui.listWidget_total_categories_2.addItem(QListWidgetItem(item_text))
