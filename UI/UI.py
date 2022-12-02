# import PyQt6

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QCheckBox, QVBoxLayout
from PyQt6.QtGui import QPixmap
from PyQt6.uic.properties import QtWidgets


class MainWindow(QWidget):
    def __init__(self):
       super().__init__()
       self.initializeUI()

    def initializeUI(self):
        self.setGeometry(200,100,400,300) # (x,y,width,height)
        self.setWindowTitle("Whiteboard Scanner/Eraser")

        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        scan_label = QLabel("Scan", self)
        scan_label.move(15, 15)
        scan_cb = QCheckBox(self)
        scan_cb.move(50, 17)
        erase_label = QLabel("Erase", self)
        erase_label.move(15, 35)
        erase_cb = QCheckBox(self)
        erase_cb.move(50, 37)


if __name__ == '__main__':
    app = QApplication(sys.argv)    # -d for debugging, otherwise empty for production
    window = MainWindow()
    sys.exit(app.exec())