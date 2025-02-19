import json
import sys
from datetime import datetime

import pandas as pd

from PySide6.QtCore import QThread, Signal
from PySide6.QtWidgets import QFileDialog, QMainWindow

from ui.progress_window import Ui_ProgressWindow
from mainWindow import MainWindow

from save_and_loading import load_config
from run_file import run


class ParserThread(QThread):
    """Поток для запуска парсера"""
    log_signal = Signal(str)
    finished_signal = Signal()
    data_collected = Signal(dict)  # Сигнал для передачи данных в GUI

    def __init__(self, parent_window):
        super().__init__()
        self.running = True
        self.parent_window = parent_window

    def run(self):
        """Запускаем парсер в отдельном потоке"""
        sys.stdout = self
        try:
            # Отключаем кнопки во время парсинга
            self.parent_window.ui.btn_setting.setEnabled(False)
            self.parent_window.ui.btn_json.setEnabled(False)
            self.parent_window.ui.btn_xlsx.setEnabled(False)
            self.parent_window.ui.btn_stop.setEnabled(True)
            self.parent_window.ui.btn_start.setEnabled(False)

            self.log_signal.emit("⏳ Парсинг запущен...")
            run(self)  # Передаём thread в парсер

        except Exception as e:
            self.log_signal.emit(f"❌ Ошибка: {str(e)}")

        finally:
            sys.stdout = sys.__stdout__
            # Включаем кнопки после завершения парсинга
            self.parent_window.ui.btn_setting.setEnabled(True)
            self.parent_window.ui.btn_json.setEnabled(True)
            self.parent_window.ui.btn_xlsx.setEnabled(True)
            self.parent_window.ui.btn_stop.setEnabled(False)
            self.parent_window.ui.btn_start.setEnabled(True)

            self.finished_signal.emit()

    def write(self, text):
        """Передаём вывод парсера в GUI"""
        if text.strip():
            self.log_signal.emit(text.strip())

    def flush(self):
        pass

    def stop(self):
        """Останавливаем парсер"""
        self.running = False


class ProgressWindow(QMainWindow):
    """Окно с прогрессом парсинга"""

    def __init__(self):
        super().__init__()
        self.ui = Ui_ProgressWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("avitoOption - Процесс сбора данных")

        # Подключаем кнопки
        self.ui.btn_setting.clicked.connect(self.setting_window)
        self.ui.btn_start.clicked.connect(self.start)
        self.ui.btn_stop.clicked.connect(self.stop_parser)
        self.ui.btn_json.clicked.connect(self.save_to_json)
        self.ui.btn_xlsx.clicked.connect(self.save_to_xlsx)

        # Храним все данные парсинга
        self.data = []
        self.thread = ParserThread(self)
        # Создаём поток для парсинга
        self.thread.log_signal.connect(self.update_log)
        self.thread.finished_signal.connect(self.on_parsing_finished)
        self.thread.data_collected.connect(self.collect_data)  # Получаем данные из парсера

    def setting_window(self):
        """Закрываем текущее окно и возвращаемся в настройки"""
        self.main_window = MainWindow()
        self.main_window.show()
        self.close()

    def start(self):
        """Запускаем парсер в отдельном потоке"""
        self.data = []  # Очищаем данные перед началом
        self.thread.running = True
        self.thread.start()

    def stop_parser(self):
        """Останавливаем парсер"""
        self.ui.text_output.append("⚠️ Остановка парсинга...")
        self.thread.stop()

    def update_log(self, text):
        """Обновляем лог в реальном времени"""
        self.ui.text_output.append(text)

    def collect_data(self, parsed_data):
        """Получаем данные из парсера и сохраняем в self.data"""
        self.data.append(parsed_data)

    def on_parsing_finished(self):
        """Вызывается после завершения парсинга"""
        self.ui.text_output.append("✅ Парсинг завершен!")

    def save_to_json(self):
        """Сохраняем данные в JSON-файл"""
        if not self.data:
            self.ui.text_output.append("⚠️ Нет данных для сохранения!")
            return

        # Загружаем название запроса из конфига
        config = load_config()
        user_query = config.get("user_response", "Запрос").strip()

        # Формируем название файла
        current_time = datetime.now().strftime("%d.%m.%Y %H-%M")
        filename = f"{user_query} ({current_time}).json"

        # Спрашиваем у пользователя, куда сохранить файл
        filepath, _ = QFileDialog.getSaveFileName(self, "Сохранить JSON", filename, "JSON Files (*.json)")
        if filepath:
            with open(filepath, "w", encoding="utf-8") as file:
                json.dump(self.data, file, indent=4, ensure_ascii=False)
            self.ui.text_output.append(f"✅ Данные сохранены в {filepath}")

    def save_to_xlsx(self):
        """Сохраняем данные в XLSX-файл"""
        if not self.data:
            self.ui.text_output.append("⚠️ Нет данных для сохранения!")
            return

        # Загружаем название запроса из конфига
        config = load_config()
        user_query = config.get("user_response", "Запрос").strip()

        # Формируем название файла
        current_time = datetime.now().strftime("%d.%m.%Y %H-%M")
        filename = f"{user_query} ({current_time}).xlsx"

        # Спрашиваем у пользователя, куда сохранить файл
        filepath, _ = QFileDialog.getSaveFileName(self, "Сохранить XLSX", filename, "Excel Files (*.xlsx)")
        if filepath:
            df = pd.DataFrame(self.data)  # Создаём DataFrame из списка словарей
            df.to_excel(filepath, index=False)  # Сохраняем в XLSX без индексов
            self.ui.text_output.append(f"✅ Данные сохранены в {filepath}")
