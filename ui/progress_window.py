# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'progress_window.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTextEdit, QWidget)

class Ui_ProgressWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1131, 814)
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
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer_3 = QSpacerItem(462, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 1, 3, 1, 1)

        self.btn_json = QPushButton(self.centralwidget)
        self.btn_json.setObjectName(u"btn_json")

        self.gridLayout.addWidget(self.btn_json, 2, 0, 1, 1)

        self.btn_xlsx = QPushButton(self.centralwidget)
        self.btn_xlsx.setObjectName(u"btn_xlsx")

        self.gridLayout.addWidget(self.btn_xlsx, 2, 1, 1, 1)

        self.btn_setting = QPushButton(self.centralwidget)
        self.btn_setting.setObjectName(u"btn_setting")

        self.gridLayout.addWidget(self.btn_setting, 0, 0, 1, 1)

        self.text_output = QTextEdit(self.centralwidget)
        self.text_output.setObjectName(u"text_output")
        self.text_output.setReadOnly(True)

        self.gridLayout.addWidget(self.text_output, 3, 0, 1, 4)

        self.btn_stop = QPushButton(self.centralwidget)
        self.btn_stop.setObjectName(u"btn_stop")
        self.btn_stop.setMinimumSize(QSize(82, 0))

        self.gridLayout.addWidget(self.btn_stop, 1, 1, 1, 1)

        self.btn_start = QPushButton(self.centralwidget)
        self.btn_start.setObjectName(u"btn_start")

        self.gridLayout.addWidget(self.btn_start, 1, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(463, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1131, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_json.setText(QCoreApplication.translate("MainWindow", u"json", None))
        self.btn_xlsx.setText(QCoreApplication.translate("MainWindow", u"xlsx", None))
        self.btn_setting.setText(QCoreApplication.translate("MainWindow", u"\u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.btn_stop.setText(QCoreApplication.translate("MainWindow", u"\u0441\u0442\u043e\u043f", None))
        self.btn_start.setText(QCoreApplication.translate("MainWindow", u"\u0441\u0442\u0430\u0440\u0442", None))
    # retranslateUi

