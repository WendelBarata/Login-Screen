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
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(415, 274)
        MainWindow.setWindowFlags(Qt.FramelessWindowHint)  # NEED TO ADD THIS CODE
        MainWindow.setAttribute(Qt.WA_TranslucentBackground)  # NEED TO ADD THIS CODE
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 20, 361, 241))
        self.widget.setStyleSheet(u"QWidget#widget {\n"
"background: rgb(0, 11, 26);\n"
"border-radius: 10px;\n"
"}")
        self.btnLogin = QPushButton(self.widget)
        self.btnLogin.setObjectName(u"btnLogin")
        self.btnLogin.setGeometry(QRect(180, 185, 71, 31))
        font = QFont()
        font.setBold(True)
        self.btnLogin.setFont(font)
        self.btnLogin.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnLogin.setStyleSheet(u"background: rgb(13, 134, 255);\n"
"border: none; \n"
"color: rgb(200, 200, 210);\n"
"font-size: 18px; \n"
"border-radius: 4px;\n"
"")
        self.btnCancel = QPushButton(self.widget)
        self.btnCancel.setObjectName(u"btnCancel")
        self.btnCancel.setGeometry(QRect(260, 185, 71, 31))
        self.btnCancel.setFont(font)
        self.btnCancel.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnCancel.setStyleSheet(u"background: rgb(13, 134, 255);\n"
"border: none; \n"
"color: rgb(200, 200, 210);\n"
"font-size: 18px; \n"
"border-radius: 4px;\n"
"")
        self.lbTitle = QLabel(self.widget)
        self.lbTitle.setObjectName(u"lbTitle")
        self.lbTitle.setGeometry(QRect(0, 10, 361, 41))
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        self.lbTitle.setFont(font1)
        self.lbTitle.setStyleSheet(u"color: rgb(13, 134, 255);\n"
"")
        self.lbTitle.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.lbName = QLabel(self.widget)
        self.lbName.setObjectName(u"lbName")
        self.lbName.setGeometry(QRect(21, 60, 51, 41))
        self.lbName.setStyleSheet(u"QLabel#lbName {\n"
"	image: url(:/icons_app/user_icon.png);\n"
"    border: none;\n"
"    border-top-left-radius: 3px;\n"
"    border-bottom-left-radius: 3px;\n"
"    border-bottom: 2px solid rgba(240, 244, 250, 200);\n"
"    padding-bottom: 7px;\n"
"    background: rgb(0, 22, 50);\n"
"}")
        self.lbPassword = QLabel(self.widget)
        self.lbPassword.setObjectName(u"lbPassword")
        self.lbPassword.setGeometry(QRect(21, 120, 49, 41))
        self.lbPassword.setStyleSheet(u"QLabel#lbPassword {\n"
"    image: url(:/icons_app/password_icon.png);\n"
"    border: none;\n"
"    border-top-left-radius: 3px;\n"
"    border-bottom-left-radius: 3px;\n"
"    border-bottom: 2px solid rgba(240, 244, 250, 200);\n"
"    padding-bottom: 7px;\n"
"    background: rgb(0, 22, 50);\n"
"}")
        self.lbSecretCode = QLabel(self.widget)
        self.lbSecretCode.setObjectName(u"lbSecretCode")
        self.lbSecretCode.setGeometry(QRect(21, 180, 49, 41))
        self.lbSecretCode.setStyleSheet(u"QLabel#lbSecretCode {\n"
"    image: url(:/icons_app/secretcode_icon.png);\n"
"    border: none;\n"
"    border-top-left-radius: 3px;\n"
"    border-bottom-left-radius: 3px;\n"
"    border-bottom: 2px solid rgba(240, 244, 250, 200);\n"
"    padding-bottom: 7px;\n"
"    background: rgb(0, 22, 50);\n"
"}")
        self.leName = QLineEdit(self.widget)
        self.leName.setObjectName(u"leName")
        self.leName.setGeometry(QRect(70, 60, 261, 41))
        font2 = QFont()
        self.leName.setFont(font2)
        self.leName.setStyleSheet(u"QLineEdit#leName {\n"
"    border: none;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"    border-bottom: 2px solid rgba(240, 244, 250, 200);\n"
"    font-size: 14px;\n"
"    color: rgb(240, 244, 250);\n"
"    padding-bottom: 7px;\n"
"    background: rgb(0, 22, 50);\n"
"}\n"
"\n"
"QLineEdit#leName:focus {\n"
"    border-color: rgb(13, 134, 255);\n"
"}\n"
"")
        self.lePassword = QLineEdit(self.widget)
        self.lePassword.setObjectName(u"lePassword")
        self.lePassword.setGeometry(QRect(70, 120, 261, 41))
        self.lePassword.setStyleSheet(u"QLineEdit#lePassword {\n"
"    border: none;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"    border-bottom: 2px solid rgba(240, 244, 250, 200);\n"
"    font-size: 14px;\n"
"    color: rgb(240, 244, 250);\n"
"    padding-bottom: 7px;\n"
"    background: rgb(0, 22, 50);\n"
"}\n"
"\n"
"QLineEdit#lePassword:focus {\n"
"    border-color: rgb(13, 134, 255);\n"
"}\n"
"")
        self.lePassword.setEchoMode(QLineEdit.EchoMode.Password)
        self.leSecretCode = QLineEdit(self.widget)
        self.leSecretCode.setObjectName(u"leSecretCode")
        self.leSecretCode.setGeometry(QRect(70, 180, 101, 41))
        self.leSecretCode.setStyleSheet(u"QLineEdit#leSecretCode {\n"
"    border: none;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"    border-bottom: 2px solid rgba(240, 244, 250, 200);\n"
"    font-size: 14px;\n"
"    color: rgb(240, 244, 250);\n"
"    padding-bottom: 7px;\n"
"    background: rgb(0, 22, 50);\n"
"}\n"
"\n"
"QLineEdit#leSecretCode:focus {\n"
"    border-color: rgb(13, 134, 255);\n"
"}\n"
"")
        self.leSecretCode.setEchoMode(QLineEdit.EchoMode.Password)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btnLogin.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.btnCancel.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.lbTitle.setText(QCoreApplication.translate("MainWindow", u"LOGIN", None))
        self.lbName.setText("")
        self.lbPassword.setText("")
        self.lbSecretCode.setText("")
        self.leName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type your user", None))
        self.lePassword.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type your password", None))
        self.leSecretCode.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Secret Code", None))
    # retranslateUi

