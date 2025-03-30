import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget,
                               QLabel, QLineEdit)
from PySide6.QtGui import QShortcut, QKeySequence
# Import the login screen interface
from interface.py.LoginScreen import Ui_MainWindow
# Import the limited screen interface
from interface.py.LimitedScreen import Ui_Form
# Import the unlimited screen interface
from interface.py.UnlimitedScreen import Ui_Form2


class TelaLogin(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        # Shortcut to show the secret code
        self.shortcut = QShortcut(QKeySequence("Ctrl+Shift+Up"), self)
        self.shortcut.activated.connect(self.secretCodeVisible)

        self.setWindowTitle("Login")
        self.lbSecretCode.setVisible(False)  # Initially hide the secret code
        self.leSecretCode.setVisible(False)  # Initially hide the secret code

        # Connect buttons to corresponding methods
        self.btnLogin.clicked.connect(self.login)
        self.btnCancel.clicked.connect(self.quitApp)

    def secretCodeVisible(self):
        # Make the secret code label and
        # field visible when the shortcut is triggered
        self.lbSecretCode.setVisible(True)
        self.leSecretCode.setVisible(True)

    def login(self):
        name = self.leName.text()
        password = self.lePassword.text()
        secretCode = self.leSecretCode.text()
        secretCodeCheckVisible = self.leSecretCode.isVisible()

        # Check credentials and redirect to appropriate screens

        # Change this screen to your most accessible screen
        if name == "admin" and password == "admin" and secretCode == "secret":
            self.close()
            self.windowUnlimited = UnlimitedScreen()
            self.windowUnlimited.show()

        elif (name == "admin" and
              password == "admin" and
              secretCode != "secret" and
              secretCodeCheckVisible):

            self.lbStatusBar.setText("Incorrect Secret Code")

        elif (name != "admin" and
              password != "admin" and
              secretCode == "secret" and
              secretCodeCheckVisible):

            self.lbStatusBar.setText("Incorrect User or Password")

        # Change this screen to your screen that has less access
        elif name == "admin" and password == "admin":
            self.close()
            self.windowLimited = LimitedScreen()
            self.windowLimited.show()

        else:
            self.lbStatusBar.setText("Invalid Credentials")

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
