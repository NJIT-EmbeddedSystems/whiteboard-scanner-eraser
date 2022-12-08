# import PyQt6

import sys
import buttons

from PyQt6.QtWidgets import (QApplication, QWidget, QLabel,\
                             QCheckBox, QPushButton) 
# not used: qvboxlayout
# from PyQt6.QtGui import QPixmap
from PyQt6.uic.properties import QtWidgets
from PyQt6.QtCore import Qt


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
        header_label = QLabel("Select options:", self)
        header_label.setWordWrap(True)
        header_label.move(15,10)

        # scan checkbox
        scan_label = QLabel("Scan", self)
        scan_label.move(15, 30)
        scan_cb = QCheckBox(self)
        scan_cb.move(60, 30)
        
        # erase checkbox
        erase_label = QLabel("Erase", self)
        erase_label.move(15, 50)
        erase_cb = QCheckBox(self)
        erase_cb.move(60, 50)

        # Execute button
        self.button = QPushButton("EXECUTE",self)
        self.button.resize(120, 60)
        self.button.move(155,200)
        #self.button.clicked.connect(self.execClicked()) 
        # add buttonClicked() def


if __name__ == '__main__':
    app = QApplication(sys.argv)    # -d for debugging, otherwise empty for production
    window = MainWindow()
    sys.exit(app.exec())