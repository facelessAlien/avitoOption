# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1191, 918)
        MainWindow.setStyleSheet(u"QWidget {\n"
"    background-color: #1e1e1e;\n"
"    color: #ffffff;\n"
"    font-family: Arial, sans-serif;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    background-color: #2b2b2b;\n"
"    border: 1px solid #555;\n"
"    border-radius: 4px;\n"
"    padding: 6px;\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #00aaff;\n"
"    background-color: #333;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #007acc;\n"
"    border: 1px solid #005f99;\n"
"    border-radius: 4px;\n"
"    padding: 6px;\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #005f99;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #004080;\n"
"}\n"
"\n"
"QLabel {\n"
"    color: #bbbbbb;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QCheckBox {\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 16px;\n"
"    height: 16px;\n"
"    border: 1px solid #007acc;\n"
"    background: #2b2b2b;\n"
"}\n"
"\n"
"QCheckBox::indicator:c"
                        "hecked {\n"
"    background: #007acc;\n"
"    border: 1px solid #005f99;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_5 = QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.verticalSpacer = QSpacerItem(20, 99, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer, 13, 1, 1, 2)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_5.addWidget(self.line, 5, 0, 1, 3)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.line_page_parse_count = QLineEdit(self.centralwidget)
        self.line_page_parse_count.setObjectName(u"line_page_parse_count")

        self.gridLayout.addWidget(self.line_page_parse_count, 5, 0, 1, 1)

        self.line_city = QLineEdit(self.centralwidget)
        self.line_city.setObjectName(u"line_city")

        self.gridLayout.addWidget(self.line_city, 0, 0, 1, 1)

        self.btn_category = QPushButton(self.centralwidget)
        self.btn_category.setObjectName(u"btn_category")
        self.btn_category.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.btn_category, 1, 2, 1, 1)

        self.line_min_price = QLineEdit(self.centralwidget)
        self.line_min_price.setObjectName(u"line_min_price")

        self.gridLayout.addWidget(self.line_min_price, 4, 0, 1, 1)

        self.line_search = QLineEdit(self.centralwidget)
        self.line_search.setObjectName(u"line_search")
        self.line_search.setMaximumSize(QSize(1000, 16777215))

        self.gridLayout.addWidget(self.line_search, 1, 0, 1, 1)

        self.line_keywords = QLineEdit(self.centralwidget)
        self.line_keywords.setObjectName(u"line_keywords")

        self.gridLayout.addWidget(self.line_keywords, 2, 0, 1, 1)

        self.line_max_price = QLineEdit(self.centralwidget)
        self.line_max_price.setObjectName(u"line_max_price")

        self.gridLayout.addWidget(self.line_max_price, 4, 1, 1, 1)

        self.line_category = QLineEdit(self.centralwidget)
        self.line_category.setObjectName(u"line_category")

        self.gridLayout.addWidget(self.line_category, 1, 1, 1, 1)

        self.line_black_list = QLineEdit(self.centralwidget)
        self.line_black_list.setObjectName(u"line_black_list")

        self.gridLayout.addWidget(self.line_black_list, 3, 0, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout, 1, 0, 1, 3)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.gridLayout_5.addWidget(self.label, 0, 1, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.line_proxy = QLineEdit(self.centralwidget)
        self.line_proxy.setObjectName(u"line_proxy")

        self.gridLayout_3.addWidget(self.line_proxy, 0, 0, 1, 1)

        self.line_current_ip = QLineEdit(self.centralwidget)
        self.line_current_ip.setObjectName(u"line_current_ip")

        self.gridLayout_3.addWidget(self.line_current_ip, 0, 1, 1, 1)

        self.btn_check_proxy = QPushButton(self.centralwidget)
        self.btn_check_proxy.setObjectName(u"btn_check_proxy")
        self.btn_check_proxy.setMaximumSize(QSize(200, 16777215))

        self.gridLayout_3.addWidget(self.btn_check_proxy, 1, 0, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_3, 7, 0, 1, 3)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_5.addWidget(self.line_2, 9, 0, 1, 3)

        self.horizontalSpacer = QSpacerItem(370, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer, 2, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_3, 4, 1, 1, 2)

        self.btn_start = QPushButton(self.centralwidget)
        self.btn_start.setObjectName(u"btn_start")
        self.btn_start.setMinimumSize(QSize(200, 0))
        self.btn_start.setMaximumSize(QSize(200, 16777215))

        self.gridLayout_5.addWidget(self.btn_start, 14, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_4, 8, 1, 1, 2)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_5.addWidget(self.label_2, 6, 1, 1, 1)

        self.btn_donate = QPushButton(self.centralwidget)
        self.btn_donate.setObjectName(u"btn_donate")

        self.gridLayout_5.addWidget(self.btn_donate, 15, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.line_pause = QLineEdit(self.centralwidget)
        self.line_pause.setObjectName(u"line_pause")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_pause.sizePolicy().hasHeightForWidth())
        self.line_pause.setSizePolicy(sizePolicy)
        self.line_pause.setMinimumSize(QSize(250, 0))
        self.line_pause.setMaximumSize(QSize(250, 16777215))
        self.line_pause.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly)

        self.gridLayout_2.addWidget(self.line_pause, 2, 1, 1, 1)

        self.checkBox_headless = QCheckBox(self.centralwidget)
        self.checkBox_headless.setObjectName(u"checkBox_headless")

        self.gridLayout_2.addWidget(self.checkBox_headless, 3, 0, 1, 1)

        self.checkBox_detail_cards_info = QCheckBox(self.centralwidget)
        self.checkBox_detail_cards_info.setObjectName(u"checkBox_detail_cards_info")

        self.gridLayout_2.addWidget(self.checkBox_detail_cards_info, 0, 0, 1, 2)

        self.checkBox_update = QCheckBox(self.centralwidget)
        self.checkBox_update.setObjectName(u"checkBox_update")

        self.gridLayout_2.addWidget(self.checkBox_update, 2, 0, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_2, 2, 0, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_5.addWidget(self.label_3, 10, 1, 1, 1)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.line_tg_token = QLineEdit(self.centralwidget)
        self.line_tg_token.setObjectName(u"line_tg_token")
        self.line_tg_token.setMinimumSize(QSize(500, 0))

        self.gridLayout_4.addWidget(self.line_tg_token, 0, 0, 1, 2)

        self.btn_check_tg_token = QPushButton(self.centralwidget)
        self.btn_check_tg_token.setObjectName(u"btn_check_tg_token")
        self.btn_check_tg_token.setMaximumSize(QSize(200, 16777215))

        self.gridLayout_4.addWidget(self.btn_check_tg_token, 1, 0, 1, 1)

        self.checkBox_send_tg = QCheckBox(self.centralwidget)
        self.checkBox_send_tg.setObjectName(u"checkBox_send_tg")

        self.gridLayout_4.addWidget(self.checkBox_send_tg, 1, 1, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_4, 11, 0, 1, 3)

        self.horizontalSpacer_2 = QSpacerItem(370, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_2, 2, 2, 1, 1)

        self.line_requests_pause = QLineEdit(self.centralwidget)
        self.line_requests_pause.setObjectName(u"line_requests_pause")
        self.line_requests_pause.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_5.addWidget(self.line_requests_pause, 3, 0, 1, 1)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setReadOnly(True)

        self.gridLayout_5.addWidget(self.lineEdit, 15, 2, 1, 1)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_5.addWidget(self.label_4, 15, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1191, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.line_page_parse_count.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u043a\u043e\u043b-\u0432\u043e \u0441\u0442\u0440\u0430\u043d\u0438\u0446 \u0434\u043b\u044f \u043f\u0430\u0440\u0441\u0438\u043d\u0433\u0430", None))
        self.line_city.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0440\u043e\u0434 \u043f\u043e\u0438\u0441\u043a\u0430. \u041d\u0430\u043f\u0440\u0438\u043c\u0435\u0440: moskva", None))
        self.btn_category.setText(QCoreApplication.translate("MainWindow", u"\u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438", None))
        self.line_min_price.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u043c\u0438\u043d. \u0446\u0435\u043d\u0430", None))
        self.line_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0442\u0435\u043a\u0441\u0442 \u0437\u0430\u043f\u0440\u043e\u0441\u0430", None))
        self.line_keywords.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u043a\u043b\u044e\u0447\u0435\u0432\u043e\u0435 \u0441\u043b\u043e\u0432\u043e1, \u043a\u043b\u044e\u0447\u0435\u0432\u043e\u0435 \u0441\u043b\u043e\u0432\u043e2 \u0438 \u0442\u0434..", None))
        self.line_max_price.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u043c\u0430\u043a\u0441. \u0446\u0435\u043d\u0430", None))
        self.line_category.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044e \u0438\u0437 \u0441\u043f\u0438\u0441\u043a\u0430 \u0438\u043b\u0438 \u0432\u0441\u0442\u0430\u0432\u044c\u0442\u0435 url \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438", None))
        self.line_black_list.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0441\u043b\u043e\u0432\u0430 \u0434\u043b\u044f \u0447\u0435\u0440\u043d\u043e\u0433\u043e \u0441\u043f\u0438\u0441\u043a\u0430 \u0447\u0435\u0440\u0435\u0437 \u0437\u0430\u043f\u044f\u0442\u0443\u044e", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u043f\u043e\u0438\u0441\u043a\u0430", None))
        self.line_proxy.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u043f\u0440\u043e\u043a\u0441\u0438 login:password@host:port", None))
        self.line_current_ip.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u043d\u0430\u0448 ip ", None))
        self.btn_check_proxy.setText(QCoreApplication.translate("MainWindow", u"\u043f\u0440\u043e\u0432\u0435\u0440\u0438\u0442\u044c \u043f\u0440\u043a\u043e\u0441\u0438", None))
        self.btn_start.setText(QCoreApplication.translate("MainWindow", u"\u043e\u043a\u043d\u043e \u043f\u0430\u0440\u0441\u0438\u043d\u0433\u0430", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u043f\u043e\u0438\u0441\u043a\u0430", None))
        self.btn_donate.setText(QCoreApplication.translate("MainWindow", u"\u2615 \u041f\u043e\u0434\u0434\u0435\u0440\u0436\u0430\u0442\u044c \u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u0447\u0438\u043a\u0430", None))
        self.line_pause.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u043f\u0430\u0443\u0437\u0430 \u0432 \u0441\u0435\u043a\u0443\u043d\u0434\u0430\u0445, \u043d\u0430\u043f\u0440\u0438\u043c\u0435\u0440: 10000", None))
        self.checkBox_headless.setText(QCoreApplication.translate("MainWindow", u"\u0441\u043a\u0440\u044b\u0442\u044b\u0439 \u0440\u0435\u0436\u0438\u043c", None))
        self.checkBox_detail_cards_info.setText(QCoreApplication.translate("MainWindow", u"\u0434\u0435\u0442\u0430\u043b\u044c\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435 \u0438\u0437 \u043a\u0430\u0440\u0442\u043e\u0447\u0435\u043a", None))
        self.checkBox_update.setText(QCoreApplication.translate("MainWindow", u"\u0440\u0435\u0436\u0438\u043c \u043c\u043e\u043d\u0438\u0442\u043e\u0440\u0438\u043d\u0433\u0430", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0432\u0437\u0430\u0438\u043c\u043e\u0434\u0435\u0439\u0441\u0442\u0432\u0438\u0435 \u0441 \u0442\u0435\u043b\u0435\u0433\u0440\u0430\u043c-\u0431\u043e\u0442", None))
        self.line_tg_token.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0442\u043e\u043a\u0435\u043d \u0442\u0435\u043b\u0435\u0433\u0440\u0430\u043c \u0431\u043e\u0442\u0430 \u0438 \u0447\u0430\u0442 id", None))
        self.btn_check_tg_token.setText(QCoreApplication.translate("MainWindow", u"\u043f\u0440\u043e\u0432\u0435\u0440\u0438\u0442\u044c \u0442\u043e\u043a\u0435\u043d", None))
        self.checkBox_send_tg.setText(QCoreApplication.translate("MainWindow", u"\u043e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c \u0432 \u0442\u0435\u043b\u0435\u0433\u0440\u0430\u043c", None))
        self.line_requests_pause.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u043f\u0430\u0443\u0437\u0430 \u0432 \u0441\u0435\u043a\u0443\u043d\u0434\u0430\u0445 \u043c\u0435\u0436\u0434\u0443 \u0437\u0430\u043f\u0440\u043e\u0441\u043e\u0432", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"https://github.com/Duff89/parser_avito", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0410\u041d\u041d\u042b\u0419 \u041f\u0420\u041e\u0415\u041a\u0422 \u0411\u042b\u041b \u0412\u0414\u041e\u0425\u041d\u041e\u0412\u041b\u0415\u041d \u041f\u0420\u041e\u0415\u041a\u0422\u041e\u041c >>>>>", None))
    # retranslateUi

