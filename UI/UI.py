# import PyQt6

import sys
import buttons

from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, \
                             QCheckBox, QPushButton, QLineEdit, QVBoxLayout)

# from PyQt6.QtGui import QPixmap
from PyQt6.uic.properties import QtWidgets
from PyQt6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(200, 100, 400, 350)  # (x,y,width,height)
        self.setWindowTitle("Whiteboard Scanner/Eraser")
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        Vlayout = QVBoxLayout()

        header_label = QLabel("Select options:", self)
        header_label.setWordWrap(True)
        Vlayout.addWidget(header_label)

        # scan checkbox
        scan_label = QLabel("Scan", self)
        Vlayout.addWidget(scan_label)
        scan_cb = QCheckBox(self)
        Vlayout.addWidget(scan_cb)

        # erase checkbox
        erase_label = QLabel("Erase", self)
        Vlayout.addWidget(erase_label)
        erase_cb = QCheckBox(self)
        Vlayout.addWidget(erase_cb)

        # save location entry
        saveLocation_label = QLabel("Save Location:", self)
        Vlayout.addWidget(saveLocation_label)
        self.saveLocation_edit = QLineEdit(self)
        Vlayout.addWidget(self.saveLocation_edit)

        # Execute button
        self.button = QPushButton("EXECUTE", self)
        Vlayout.addWidget(self.button)
        # self.button.clicked.connect(self.execClicked())
        # add buttonClicked() def

        app.setStyleSheet("QLabel{font: 15pt;} QCheckBox::indicator{width: 20px; height: 20px}"
                          "QPushButton{font: bold 20px} QLineEdit{height: 20px}")
        self.setStyleSheet("background-color: lightblue;")
        self.setLayout(Vlayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)  # -d for debugging, otherwise empty for production
    window = MainWindow()
    sys.exit(app.exec())