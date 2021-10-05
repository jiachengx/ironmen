import sys
from PySide2.QtCore import *
from PySide2.QtWidgets import QApplication, QMainWindow, QMenu


class MainWindow(QMainWindow):
     def __init__(self):
         super(MainWindow, self).__init__()
         self.resize(500, 400)
         self.setWindowTitle('Window context')
         self.setContextMenuPolicy(Qt.CustomContextMenu)
         self.customContextMenuRequested.connect(self.right_menu)

     def right_menu(self, pos):
         menu = QMenu()
         hello_opt = menu.addAction('Hello Hello')
         goodbye_opt = menu.addAction('881')
         exit_opt = menu.addAction('Close')
         hello_opt.triggered.connect(lambda: print('Hello Hello'))
         goodbye_opt.triggered.connect(lambda: print('881'))
         exit_opt.triggered.connect(lambda: exit())

         menu.exec_(self.mapToGlobal(pos))


if __name__ == '__main__':
     app = QApplication([])
     window = MainWindow()
     window.show()
     sys.exit(app.exec_())
