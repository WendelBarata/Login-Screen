# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_screen.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(415, 512)
        MainWindow.setWindowFlags(Qt.FramelessWindowHint)  # NEED TO ADD THIS CODE
        MainWindow.setAttribute(Qt.WA_TranslucentBackground)  # NEED TO ADD THIS CODE
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 20, 361, 461))
        self.widget.setStyleSheet(u"background:  blue\n"
"")
        self.btnLogin = QPushButton(self.widget)
        self.btnLogin.setObjectName(u"btnLogin")
        self.btnLogin.setGeometry(QRect(30, 390, 141, 51))
        self.btnCancel = QPushButton(self.widget)
        self.btnCancel.setObjectName(u"btnCancel")
        self.btnCancel.setGeometry(QRect(190, 390, 141, 51))
        self.lbTitle = QLabel(self.widget)
        self.lbTitle.setObjectName(u"lbTitle")
        self.lbTitle.setGeometry(QRect(0, 0, 361, 41))
        self.lbName = QLabel(self.widget)
        self.lbName.setObjectName(u"lbName")
        self.lbName.setGeometry(QRect(30, 80, 49, 16))
        self.lbPassword = QLabel(self.widget)
        self.lbPassword.setObjectName(u"lbPassword")
        self.lbPassword.setGeometry(QRect(30, 150, 49, 16))
        self.lbSecretCode = QLabel(self.widget)
        self.lbSecretCode.setObjectName(u"lbSecretCode")
        self.lbSecretCode.setGeometry(QRect(30, 340, 49, 16))
        self.leName = QLineEdit(self.widget)
        self.leName.setObjectName(u"leName")
        self.leName.setGeometry(QRect(150, 90, 113, 22))
        self.lePassword = QLineEdit(self.widget)
        self.lePassword.setObjectName(u"lePassword")
        self.lePassword.setGeometry(QRect(150, 150, 113, 22))
        self.leSecretCode = QLineEdit(self.widget)
        self.leSecretCode.setObjectName(u"leSecretCode")
        self.leSecretCode.setGeometry(QRect(140, 340, 113, 22))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btnLogin.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.btnCancel.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.lbTitle.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.lbName.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.lbPassword.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.lbSecretCode.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

