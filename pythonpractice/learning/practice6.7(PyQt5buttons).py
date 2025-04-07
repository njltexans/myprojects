#PyQt5 buttons

import sys # provides access to system-specific parameters and functions
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QGridLayout, QWidget, QVBoxLayout, QLabel, QPushButton # importing the necessary classes from PyQt5
from PyQt5.QtGui import QIcon # importing the QIcon class to set an icon for the window
from PyQt5.QtGui import QFont # importing the QFont class to set a font for the text
from PyQt5.QtCore import Qt # importing the Qt class to set the alignment of the text
from PyQt5.QtGui import QPixmap # importing the QPixmap class to set an image for the label

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Very Cool First PyQt5 Application") # setting the title of the window
        self.setGeometry(700, 300, 500, 500) # setting the position and size of the window (x, y, width, height)
        self.button = QPushButton("Click Me PLEEAASSEE!", self) # creating a button widget
        self.label = QLabel("Hello", self) # creating a label widget
        self.initUI()

    def initUI(self):
        self.button.setGeometry(150, 200, 200, 100)
        self.button.setStyleSheet("font-size: 15px;")
        self.button.clicked.connect(self.on_click)

        self.label.setGeometry(150, 100, 200, 100) # setting the position and size of the label (x, y, width, height)
        self.label.setStyleSheet("font-size: 30px; color: blue;") # setting the color of the label text

    def on_click(self):
        self.label.setText("Button Clicked!")
        self.label.setStyleSheet("font-size: 20px; color: red;")



if __name__ == "__main__":
    app = QApplication(sys.argv) # creating an instance of the QApplication class
    window = MainWindow() # creating an instance of the MainWindow class
    window.show() # displaying the window
    sys.exit(app.exec_()) # starting the event loop and exiting when the application is closed

