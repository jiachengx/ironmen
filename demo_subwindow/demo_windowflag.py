from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import *
from p3 import Ui_MainWindow
from p2s import Ui_Form as Ui_second
from p3s import Ui_Form as Ui_third
from PySide2.QtCore import Qt

import sys


class ThirdWindow(QWidget):
    def __init__(self):
        super(ThirdWindow, self).__init__()
        self.ui = Ui_third()
        self.ui.setupUi(self)
        self.ui.label.setStyleSheet("background-color: yellow")


class SecondWindow(QWidget):
    def __init__(self):
        super(SecondWindow, self).__init__()
        self.ui = Ui_second()
        self.ui.setupUi(self)
        self.ui.label.setStyleSheet("background-color: green")
        self.third = ThirdWindow()
        self.ui.pushButton.clicked.connect(lambda: self.third.show())


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # On Top
        # self.setWindowFlags(Qt.WindowStaysOnTopHint)
        # On Bottom
        self.setWindowFlags(Qt.WindowStaysOnBottomHint)
        self.second = SecondWindow()
        self.ui.pushButton.clicked.connect(lambda: self.second.show())


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
