# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'categories.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDialog, QLineEdit,
    QListView, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1228, 733)
        Dialog.setStyleSheet(u"/* \u041e\u0441\u043d\u043e\u0432\u043d\u043e\u0435 \u043e\u043a\u043d\u043e */\n"
"QMainWindow {\n"
"    background-color: #1E1E1E;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"/* \u0421\u043f\u0438\u0441\u043e\u043a \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0439 */\n"
"QListWidget {\n"
"    background-color: #2E2E2E;\n"
"    border: 2px solid #3A3A3A;\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"    font-size: 16px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QListWidget::item {\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"    background-color: #0078D7;\n"
"    color: white;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"/* \u0421\u043a\u0440\u043e\u043b\u043b\u0431\u0430\u0440 */\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #2E2E2E;\n"
"    width: 8px;\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #5A5A5A;\n"
"    min-height: 20px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover "
                        "{\n"
"    background: #7A7A7A;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical,\n"
"QScrollBar::sub-line:vertical {\n"
"    background: none;\n"
"    border: none;\n"
"}\n"
"\n"
"/* \u0412\u044b\u0434\u0435\u043b\u0435\u043d\u043d\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442 */\n"
"QListWidget::item:hover {\n"
"    background-color: #4A4A4A;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"/* \u041e\u043a\u043d\u043e \u0434\u0438\u0430\u043b\u043e\u0433\u0430 */\n"
"QDialog {\n"
"    background-color: #1E1E1E;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"/* \u041f\u043e\u043b\u044f \u0432\u0432\u043e\u0434\u0430 */\n"
"QLineEdit {\n"
"    background-color: #2E2E2E;\n"
"    border: 2px solid #3A3A3A;\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"    padding: 5px;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #0078D7;\n"
"}\n"
"\n"
"/* \u041a\u043d\u043e\u043f\u043a\u0438 */\n"
"QPushButton {\n"
"    background-color: #0078D7;\n"
"    color: white;\n"
"    border-radius: "
                        "5px;\n"
"    padding: 8px;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #005FA3;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #004A7C;\n"
"}\n"
"")
        self.listWidget_total_categories_2 = QListWidget(Dialog)
        self.listWidget_total_categories_2.setObjectName(u"listWidget_total_categories_2")
        self.listWidget_total_categories_2.setGeometry(QRect(412, 10, 771, 711))
        font = QFont()
        self.listWidget_total_categories_2.setFont(font)
        self.listWidget_total_categories_2.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.listWidget_total_categories_2.setViewMode(QListView.ViewMode.ListMode)
        self.listWidget_total_categories_2.setUniformItemSizes(False)
        self.listWidget_total_categories_2.setSortingEnabled(False)
        self.listWidget_total_categories = QListWidget(Dialog)
        self.listWidget_total_categories.setObjectName(u"listWidget_total_categories")
        self.listWidget_total_categories.setGeometry(QRect(10, 10, 400, 711))
        self.listWidget_total_categories.setMaximumSize(QSize(400, 16777215))
        self.listWidget_total_categories.setFont(font)
        self.listWidget_total_categories.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.listWidget_total_categories.setViewMode(QListView.ViewMode.ListMode)
        self.listWidget_total_categories.setUniformItemSizes(False)
        self.listWidget_total_categories.setSortingEnabled(False)
        self.lineEdit_search = QLineEdit(Dialog)
        self.lineEdit_search.setObjectName(u"lineEdit_search")
        self.lineEdit_search.setGeometry(QRect(940, 10, 241, 31))
        self.line_found_count = QLineEdit(Dialog)
        self.line_found_count.setObjectName(u"line_found_count")
        self.line_found_count.setGeometry(QRect(940, 40, 231, 31))
        self.line_found_count.setReadOnly(True)
        self.btn_down = QPushButton(Dialog)
        self.btn_down.setObjectName(u"btn_down")
        self.btn_down.setGeometry(QRect(940, 80, 71, 31))
        self.btn_up = QPushButton(Dialog)
        self.btn_up.setObjectName(u"btn_up")
        self.btn_up.setGeometry(QRect(1020, 80, 71, 31))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.lineEdit_search.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u043f\u043e\u0438\u0441\u043a", None))
        self.line_found_count.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u043a\u043e\u043b-\u0432\u043e \u0441\u043e\u0432\u043f\u0430\u0434\u0435\u043d\u0438\u0439", None))
        self.btn_down.setText(QCoreApplication.translate("Dialog", u"\u0412\u041d\u0418\u0417", None))
        self.btn_up.setText(QCoreApplication.translate("Dialog", u"\u0412\u0412\u0415\u0420\u0425", None))
    # retranslateUi

