# import PyQt6

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QCheckBox, QVBoxLayout, QPushButton
from PyQt6.QtGui import QPixmap, QFont
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
        header_label = QLabel("Select options:", self)
        header_label.setWordWrap(True)
        header_label.move(15, 10)
        header_label.setFont(QFont('Times', 20))

        # scan checkbox
        scan_label = QLabel("Scan", self)
        scan_label.move(15, 55)
        scan_label.setFont(QFont('Times', 18))
        scan_cb = QCheckBox(self)
        scan_cb.move(84, 58)
        scan_cb.setStyleSheet("""QCheckBox::indicator{width: 20px; height: 20px}""")

        # erase checkbox
        erase_label = QLabel("Erase", self)
        erase_label.move(15, 95)
        erase_label.setFont(QFont('Times', 18))
        erase_cb = QCheckBox(self)
        erase_cb.move(84, 98)
        erase_cb.setStyleSheet("""QCheckBox::indicator{width: 20px; height: 20px}""")

        # Execute button
        self.button = QPushButton("EXECUTE", self)
        self.button.setFont(QFont('Times', 15))
        self.button.setGeometry(140, 200, 120, 60)
        # self.button.clicked.connect(self.execClicked())
        # add buttonClicked() def


if __name__ == '__main__':
    app = QApplication(sys.argv)    # -d for debugging, otherwise empty for production
    window = MainWindow()
    sys.exit(app.exec())