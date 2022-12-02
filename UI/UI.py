# import PyQt6

import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QPixmap

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
        hello_label = QLabel(self)
        hello_label.setText("Hello")
        hello_label.move(105,15)

if __name__ == '__main__':
    app = QApplication(sys.argv)    # -d for debugging, otherwise empty for production
    window = MainWindow()
    sys.exit(app.exec())