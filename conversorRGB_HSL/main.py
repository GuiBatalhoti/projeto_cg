from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QFileDialog, QComboBox, QLineEdit
from PyQt5 import uic
from PyQt5.QtGui import QPixmap, qRgb, qRed, qGreen, qBlue, QColor, QImage

import sys
import os


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        #uipath = os.path.dirname(os.path.realpath(__file__)) + "/colorConversion.ui"
        uipath = 'conversorRGB_HSL\colorConversion.ui'
        uic.loadUi(uipath, self)

        self.red = self.findChild(QLineEdit, "red")
        self.green = self.findChild(QLineEdit, "green")
        self.blue = self.findChild(QLineEdit, "blue")

        self.hue = self.findChild(QLineEdit, "hue")
        self.sat = self.findChild(QLineEdit, "sat")
        self.light = self.findChild(QLineEdit, "light")

        self.buttonRGBtoHSL = self.findChild(QPushButton, "RGBtoHSL")
        self.buttonHSLtoRGB = self.findChild(QPushButton, "HSLtoRGB")

        self.buttonRGBtoHSL.clicked.connect(self.rgb_to_hsl)
        self.buttonHSLtoRGB.clicked.connect(self.hsl_to_rgb)
        
        self.show()
    
    def rgb_to_hsl(self):

        r = float(self.red.text())/255
        g = float(self.green.text())/255
        b = float(self.blue.text())/255
        #print(r,g,b)
        high = max(r, g, b)
        low = min(r, g, b)
        h, s, l = ((high + low) / 2,)*3

        if high == low:
            h = 0.0
            s = 0.0
        else:
            d = high - low
            s = d / (2 - high - low) if l > 0.5 else d / (high + low)
            h = {
                r: (g - b) / d + (6 if g < b else 0),
                g: (b - r) / d + 2,
                b: (r - g) / d + 4,
            }[high]
            h *= 60

        self.hue.setText(str(round(h, 2)))
        self.sat.setText(str(round(s, 2)))
        self.light.setText(str(round(l, 2)))
        #return round(h, 2), round(s, 2), round(l, 2)


    def clamp(self, value, min_value, max_value):
        return max(min_value, min(max_value, value))

    def saturate(self, value):
        return self.clamp(value, 0.0, 1.0)

    def hue_to_rgb(self, h):
        r = abs(h * 6.0 - 3.0) - 1.0
        g = 2.0 - abs(h * 6.0 - 2.0)
        b = 2.0 - abs(h * 6.0 - 4.0)
        return self.saturate(r), self.saturate(g), self.saturate(b)

    def hsl_to_rgb(self):
        h = float(self.hue.text())
        s = float(self.sat.text())
        l = float(self.light.text())

        r, g, b = self.hue_to_rgb(h)
        c = (1.0 - abs(2.0 * l - 1.0)) * s
        r = (r - 0.5) * c + l
        g = (g - 0.5) * c + l
        b = (b - 0.5) * c + l

        #print(r,g,b)
        self.red.setText(str(round(g * 255, 0)))
        self.green.setText(str(round(r * 255, 0)))
        self.blue.setText(str(round(b * 255, 0)))

if __name__ == '__main__':
	# Initialize The App
	app = QApplication(sys.argv)
	UIWindow = UI()
	app.exec_()
