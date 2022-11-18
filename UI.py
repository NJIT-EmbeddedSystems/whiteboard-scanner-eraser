import sys
import PyQt6

from PyQt6.QtWidgets import QApplication, QWidget

class EmptyWindow(QWidget):
    def __init__(self):
       super().__init__()
       self.initializeUI()

       def initializeUI(self):
        self.setGeometry(200,100,400,300)
        self.setWindowTitle("Whiteboard Scanner/Eraser")
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)    # -d for debugging, otherwise empty for production
    window = EmptyWindow()
    sys.exit(app.exec_())