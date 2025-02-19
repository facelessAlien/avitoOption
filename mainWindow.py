import sys

from PySide6.QtGui import QIcon, QIntValidator
from PySide6.QtWidgets import QApplication, QPushButton, QTextEdit, QVBoxLayout, QDialog, QMainWindow

from ui.mainwindow import Ui_MainWindow

from check_proxy import get_ip, send_to_telegram
from save_and_loading import save_config, load_config


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('avitoOption - Настройки')

        # Подключаем кнопки
        self.ui.btn_check_proxy.clicked.connect(self.get_my_ip)
        self.ui.btn_start.clicked.connect(self.open_progress_window)
        self.ui.btn_donate.clicked.connect(self.show_donation_window)
        self.ui.btn_category.clicked.connect(self.category_window)
        self.ui.btn_check_tg_token.clicked.connect(self.check_tg)
        # Загружаем конфиг и заполняем UI
        self.config = load_config()
        self.load_config_to_ui()
        # Добавляем всплывающие подсказки (tooltip)
        self.ui.line_city.setToolTip(
            "Введите город поиска в транслитерации (русские слова, но латиницей) (например, вместо 'москва' -> moskva)")
        self.ui.line_search.setToolTip("Введите текст запроса (например, видеокарты nvidia)")
        self.ui.line_keywords.setToolTip("Ключевые слова через запятую (например: rtx, 4090, nvidia)")
        self.ui.line_black_list.setToolTip("Слова, указанные в этом поле (через запятую), гарантированно будут игнорировать объявления в которых хотя-бы одно из этих слов присутствует")
        self.ui.line_max_price.setToolTip("Введите максимальную цену (только число)")
        self.ui.line_min_price.setToolTip("Введите минимальную цену (только число)")
        self.ui.line_category.setToolTip("Здесь можно выбрать нужную вам категорию для более детального поиска, например если вы ищите товары для охоты, то можно выбрать эту категорию.\nВы так же можете найти нужную вам категорию на сайте и вставить ее в это поле самостоятельно: /ohota_i_rybalka")
        self.ui.line_page_parse_count.setToolTip("Введите количество страниц для парсинга")
        self.ui.line_pause.setToolTip("Введите паузу в секундах, такое кол-во времени парсер будет выжидать, прежде чем снова обновлять страницу для сбора данных в режиме мониторинга")
        self.ui.line_requests_pause.setToolTip("Введите паузу в секундах, такое кол-во времени парсер будет выжидать, прежде чем снова обновлять страницу для сбора данных")
        self.ui.checkBox_detail_cards_info.setToolTip("Переход на карточку товара и парсинг данных")
        self.ui.checkBox_headless.setToolTip("Скрытый режим (окно браузера не открывается)")
        self.ui.checkBox_update.setToolTip(
            "Каждый заданный интервал парсер проверяет на наличие новых объявлений, а так же мониторит изменение цен на уже спаршенных объявлениях")
        self.ui.checkBox_send_tg.setToolTip("Если включить данный чек бокс, то все данные будут отправлены в телеграм")
        self.ui.line_proxy.setToolTip(
            "Желательно ротационный прокси с российскими (СНГ) ip вдресами, чтобы ваш ip менялся каждый запрос или каждые несколько секунд")
        self.ui.line_tg_token.setToolTip("Ведите токен вашего телеграм бота и его chat id в формате 'token::chat_id'")
        # Подключаем сигналы для автоматического сохранения
        self.ui.line_city.editingFinished.connect(self.update_config)
        self.ui.line_search.editingFinished.connect(self.update_config)
        self.ui.line_keywords.editingFinished.connect(self.update_config)
        self.ui.line_black_list.editingFinished.connect(self.update_config)
        self.ui.line_max_price.editingFinished.connect(self.update_config)
        self.ui.line_min_price.editingFinished.connect(self.update_config)
        self.ui.line_page_parse_count.editingFinished.connect(self.update_config)
        self.ui.line_proxy.editingFinished.connect(self.update_config)
        self.ui.line_tg_token.editingFinished.connect(self.update_config)
        self.ui.line_pause.editingFinished.connect(self.update_config)
        self.ui.line_requests_pause.editingFinished.connect(self.update_config)
        self.ui.line_category.editingFinished.connect(self.update_config)

        self.ui.checkBox_detail_cards_info.stateChanged.connect(self.update_config)
        self.ui.checkBox_headless.stateChanged.connect(self.update_config)
        self.ui.checkBox_send_tg.stateChanged.connect(self.update_config)
        self.ui.checkBox_update.stateChanged.connect(self.update_config)
        # Когда `checkBox_update` включен → отключаем `checkBox_detail_cards_info`
        self.ui.checkBox_update.stateChanged.connect(self.toggle_checkboxes)

        # Когда `checkBox_detail_cards_info` включен → отключаем `checkBox_update`
        self.ui.checkBox_detail_cards_info.stateChanged.connect(self.toggle_checkboxes)

        self.ui.line_min_price.setValidator(QIntValidator())
        self.ui.line_max_price.setValidator(QIntValidator())
        self.ui.line_page_parse_count.setValidator(QIntValidator())
        self.ui.line_pause.setValidator(QIntValidator())
        self.ui.line_requests_pause.setValidator(QIntValidator())

        # Подключаем `toggle_checkboxes()` к чекбоксам
        self.ui.checkBox_update.stateChanged.connect(self.toggle_checkboxes)
        self.ui.checkBox_detail_cards_info.stateChanged.connect(self.toggle_checkboxes)

    def toggle_checkboxes(self):
        """Если один чекбокс включен, другой выключается + сбрасываем `line_pause` и обновляем конфиг"""

        sender = self.sender()  # Определяем, какой чекбокс изменился

        if sender == self.ui.checkBox_update:
            if self.ui.checkBox_update.isChecked():
                self.ui.checkBox_detail_cards_info.setChecked(False)  # Отключаем `checkBox_detail_cards_info`
            else:
                self.ui.line_pause.setText('0')  # Сбрасываем значение в 0
                self.config["pause"] = 0  # Обновляем в конфиге

        if sender == self.ui.checkBox_detail_cards_info:
            if self.ui.checkBox_detail_cards_info.isChecked():
                self.ui.checkBox_update.setChecked(False)  # Отключаем `checkBox_update`

        # Управление `line_pause`
        self.ui.line_pause.setEnabled(self.ui.checkBox_update.isChecked())

        # Обновляем конфиг
        self.config["update"] = self.ui.checkBox_update.isChecked()

        # Сохраняем изменения в конфиг
        save_config(self.config)

    def load_config_to_ui(self):
        """Заполняем UI данными из конфига"""
        self.ui.line_city.setText(self.config.get("city", ""))
        self.ui.line_search.setText(self.config.get("user_response", ""))

        # Преобразуем keywords в строку с пробелами
        keywords = self.config.get("keywords", [])
        self.ui.line_keywords.setText(", ".join(keywords))
        black_list = self.config.get("black_list", [])
        self.ui.line_black_list.setText(", ".join(black_list))
        self.ui.line_max_price.setText(str(self.config.get("max_price", "")))
        self.ui.line_min_price.setText(str(self.config.get("min_price", "")))
        self.ui.line_page_parse_count.setText(str(self.config.get("max_page", "")))
        self.ui.line_proxy.setText(str(self.config.get("proxy", "")))
        self.ui.line_tg_token.setText(str(self.config.get("telegram_bot_token", "")))
        self.ui.line_pause.setText(str(self.config.get("pause", "")))
        self.ui.line_requests_pause.setText(str(self.config.get("requests_pause", "")))
        self.ui.line_category.setText(str(self.config.get("categories", "")))
        self.ui.checkBox_detail_cards_info.setChecked(self.config.get("deep_search", False))
        self.ui.checkBox_headless.setChecked(self.config.get("headless", False))
        self.ui.checkBox_send_tg.setChecked(self.config.get("send_tg", False))
        self.ui.checkBox_update.setChecked(self.config.get("update", False))

    def update_config(self):
        """Обновляет конфиг при изменении значений в UI"""
        self.config["city"] = self.ui.line_city.text()
        self.config["user_response"] = self.ui.line_search.text()

        # Преобразуем введенные keywords в список (разделение по пробелу)
        self.config["keywords"] = self.ui.line_keywords.text().split(', ') if self.ui.line_keywords.text() else []
        self.config["black_list"] = self.ui.line_black_list.text().split(', ') if self.ui.line_black_list.text() else []
        self.config["categories"] = self.ui.line_category.text() if self.ui.line_category.text() else ''

        self.config["max_price"] = int(
            self.ui.line_max_price.text()) if self.ui.line_max_price.text().isdigit() else 9999999999
        # Проверяем max_price, если пусто или 0 → 9999999999
        max_price_text = self.ui.line_max_price.text().strip()
        self.config["max_price"] = int(max_price_text) if max_price_text.isdigit() and int(
            max_price_text) > 0 else 9999999999
        self.ui.line_max_price.setText(str(self.config["max_price"]))  # Обновляем поле UI

        # Проверяем min_price, если пусто → 0
        min_price_text = self.ui.line_min_price.text().strip()
        self.config["min_price"] = int(min_price_text) if min_price_text.isdigit() else 0
        self.ui.line_min_price.setText(str(self.config["min_price"]))  # Обновляем поле UI
        self.config["max_page"] = int(
            self.ui.line_page_parse_count.text()) if self.ui.line_page_parse_count.text().isdigit() else 1

        # Проверяем pause, если пусто → 0
        pause_text = self.ui.line_pause.text().strip()
        self.config["pause"] = int(pause_text) if pause_text.isdigit() else 0
        self.ui.line_pause.setText(str(self.config["pause"]))  # Обновляем поле UI

        # Проверяем requests_pause, если пусто → 0
        requests_pause_text = self.ui.line_requests_pause.text().strip()
        self.config["requests_pause"] = int(requests_pause_text) if requests_pause_text.isdigit() else 0
        self.ui.line_requests_pause.setText(str(self.config["requests_pause"]))  # Обновляем поле UI

        self.config["telegram_bot_token"] = self.ui.line_tg_token.text()
        self.config["proxy"] = self.ui.line_proxy.text()
        self.config["deep_search"] = self.ui.checkBox_detail_cards_info.isChecked()
        self.config["headless"] = self.ui.checkBox_headless.isChecked()
        self.config["send_tg"] = self.ui.checkBox_send_tg.isChecked()
        self.config["update"] = self.ui.checkBox_update.isChecked()

        save_config(self.config)  # Сохраняем изменения в конфиге

    def get_my_ip(self):
        """ Проверяем прокси """
        proxy = self.ui.line_proxy.text() if self.ui.line_proxy.text() else None
        res = get_ip(proxy)
        self.ui.line_current_ip.setText(res if res else 'прокси сломан')

    def check_tg(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Ошибка с телеграмом")
        dialog.setFixedSize(700, 300)  # Фиксированный размер окна

        layout = QVBoxLayout()

        # Текстовое поле с реквизитами (можно копировать)
        text_edit = QTextEdit()
        token, chat_id = self.ui.line_tg_token.text().split('::')[0], self.ui.line_tg_token.text().split('::')[1]
        res = send_to_telegram(message='Manchester United', token=token, chat_id=chat_id)
        if not res:
            text_edit.setPlainText("Не удалось отправить тестовой сообщение в телеграм")
            text_edit.setReadOnly(True)  # Делаем поле только для чтения, но с возможностью копирования

            # Кнопка закрытия
            btn_close = QPushButton("Закрыть")
            btn_close.clicked.connect(dialog.accept)

            # Добавляем виджеты в макет
            layout.addWidget(text_edit)
            layout.addWidget(btn_close)

            dialog.setLayout(layout)
            dialog.exec()

    def open_progress_window(self):
        """Закрываем главное окно и открываем окно с прогрессом"""
        from progWindow import ProgressWindow
        self.progress_window = ProgressWindow()
        self.progress_window.show()
        self.close()

    def category_window(self):
        from categoryWindow import CategoryWindow
        self.progress_window = CategoryWindow(self)
        self.progress_window.show()

    def show_donation_window(self):
        """Открывает окно с реквизитами для донатов (копируемый текст)"""
        dialog = QDialog(self)
        dialog.setWindowTitle("Спасибо за поддержку! 🙌")
        dialog.setFixedSize(700, 300)  # Фиксированный размер окна

        layout = QVBoxLayout()

        # Текстовое поле с реквизитами (можно копировать)
        text_edit = QTextEdit()
        text_edit.setPlainText(
            "Если вам нравится этот проект, вы можете поддержать разработчика! ☕\n\n"
            "💳 Карта: 2202 2080 6663 9379\n"
            "USDT TON: UQACgi8bKJJG53LzVJy9dxsmg7HOL4uo3pifh4VZZHL8BL2K\n"
            "USDT TRON TRC20: TXQxZ1HCM8kDgbrTWbTPfcvwxhwW4LYGAP\n"
            "USDT Solana SPL: 3BYjbouBhjEMhdq3ab9vjfhsqwuDfPJ51nUcYZLKuSi6\n"
            "USDT Ethereum ERC20: 0xF50f84859974DA36B01Bf49DfF07531D53c9c39b\n"
            "USDT BNB Smart Chain BEP20: 0x7D4B63edE11e351A282A24b495B372C91d23DABb\n"
            "\n\n"
            "Спасибо за вашу поддержку! ❤️"
        )
        text_edit.setReadOnly(True)  # Делаем поле только для чтения, но с возможностью копирования

        # Кнопка закрытия
        btn_close = QPushButton("Закрыть")
        btn_close.clicked.connect(dialog.accept)

        # Добавляем виджеты в макет
        layout.addWidget(text_edit)
        layout.addWidget(btn_close)

        dialog.setLayout(layout)
        dialog.exec()


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    app.setWindowIcon(QIcon('ico/avito.ico'))

    window.show()
    sys.exit(app.exec())
