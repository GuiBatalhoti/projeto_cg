from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLineEdit
from PyQt5 import uic
import sys


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi('casinha/janela.ui', self)
        self.show()


if __name__ == '__main__':
	# Initialize The App
	app = QApplication(sys.argv)
	UIWindow = UI()
	app.exec_()