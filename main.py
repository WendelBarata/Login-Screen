import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from LoginScreen import Ui_MainWindow

class TelaLogin(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwindow = TelaLogin()
    mainwindow.show()
    sys.exit(app.exec())
