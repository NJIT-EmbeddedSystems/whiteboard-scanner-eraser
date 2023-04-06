# import PyQt6

import sys
import buttons

from PyQt6.QtWidgets import (QApplication, QWidget, \
                             QLabel, QCheckBox, QPushButton, QHBoxLayout,
                             QTabWidget, QFormLayout, QGridLayout, QPlainTextEdit)

# from PyQt6.QtGui import QPixmap
from PyQt6.uic.properties import QtWidgets
from PyQt6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(200, 100, 600, 450)  # (x,y,width,height)
        self.setWindowTitle("Whiteboard Scanner/Eraser")
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        main_layout = QGridLayout(self)
        self.setLayout(main_layout)
        tab = QTabWidget(self)

        # Main tab with scan, button, and log
        main_tab = QWidget(self)
        layout = QFormLayout()
        main_tab.setLayout(layout)

        header_label = QLabel("Select options:", self)
        header_label.setWordWrap(True)
        scan_check = QCheckBox(self)
        erase_check = QCheckBox(self)
        execute_button = QPushButton("EXECUTE")
        empty_label = QLabel("", self)

        layout.addRow(header_label)
        layout.addRow("Scan ", scan_check)
        layout.addRow("Erase ", erase_check)
        layout.addRow(execute_button)

        # Trying to add a space for the log
        layout.addRow("", empty_label)
        log_window = QPlainTextEdit()
        layout.addRow(log_window)

        # Live camera tab
        camera_tab = QWidget(self)
        layout = QHBoxLayout()
        camera_tab.setLayout(layout)

        # Setting tab windows
        tab.addTab(main_tab, "Scan / Erase")
        tab.addTab(camera_tab, "Live Cameras")
        main_layout.addWidget(tab, 0, 0, 2, 1)

        # Altering background color, size of buttons, checkboxes, text, etc.
        app.setStyleSheet("QLabel{font: 15pt;} QCheckBox::indicator{width: 20px; height: 20px}"
                          "QPushButton{font: bold 22px}")
        self.setStyleSheet("background-color: lightblue;")

if __name__ == '__main__':
    app = QApplication(sys.argv)  # -d for debugging, otherwise empty for production
    window = MainWindow()
    sys.exit(app.exec())