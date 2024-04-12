import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget,
                               QLabel, QLineEdit)
from PySide6.QtGui import QShortcut, QKeySequence
from LoginScreen import Ui_MainWindow
from LimitedScreen import Ui_Form
from UnlimitedScreen import Ui_Form2


class TelaLogin(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.shortcut = QShortcut(QKeySequence("Ctrl+Shift+Up"), self)
        self.shortcut.activated.connect(self.secretCodeVisible)

        self.setWindowTitle("Login")
        self.lbSecretCode.setVisible(False)
        self.leSecretCode.setVisible(False)

        self.btnLogin.clicked.connect(self.login)
        self.btnCancel.clicked.connect(self.quitApp)

    def secretCodeVisible(self):
        self.lbSecretCode.setVisible(True)
        self.leSecretCode.setVisible(True)

    def login(self):
        name = self.leName.text()
        password = self.lePassword.text()
        secretCode = self.leSecretCode.text()

        # Change this screen to your most accessible screen
        if name == "admin" and password == "admin" and secretCode == "secret":
            self.close()
            self.windowUnlimited = UnlimitedScreen()
            self.windowUnlimited.show()

        # Change this screen to your screen that has less access
        elif name == "admin" and password == "admin":
            self.close()
            self.windowLimited = LimitedScreen()
            self.windowLimited.show()

    def quitApp(self):
        QApplication.quit()


# Change this screen to your screen that has less access
class LimitedScreen(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)


# Change this screen to your most accessible screen
class UnlimitedScreen(QWidget, Ui_Form2):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwindow = TelaLogin()
    mainwindow.show()
    sys.exit(app.exec())
