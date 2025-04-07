# Using PyQt5 to create a simple GUI application
# Introduction

import sys # provides access to system-specific parameters and functions

from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QGridLayout, QWidget, QVBoxLayout, QLabel, QPushButton #importing the necessary classes from PyQt5

from PyQt5.QtGui import QIcon # importing the QIcon class to set an icon for the window

from PyQt5.QtGui import QFont # importing the QFont class to set a font for the text

from PyQt5.QtCore import Qt # importing the Qt class to set the alignment of the text 

from PyQt5.QtGui import QPixmap # importing the QPixmap class to set an image for the label


class MainWindow(QMainWindow):
     def __init__(self):
        super().__init__()
        self.setWindowTitle("Very Cool First PyQt5 Application") # setting the title of the window
        self.setGeometry(100, 100, 600, 400) # setting the position and size of the window (x, y, width, height)
        #self.setWindowIcon(QIcon("icon.png")) # setting the icon of the window (I am not doing this but this is how I would if I was)

        label = QLabel("Hello, self!") # creating a label widget
        label.setFont(QFont("Arial", 40)) # setting the font of the label text (font name, font size)
        label.setGeometry(50, 50, 500, 100) # setting the position and size of the label (x, y, width, height)
        label.setStyleSheet("color: white;"
                            "background-color: black;") # setting the color of the label text
        
        #label.setAlignment(Qt.AlignTop) # setting the alignment of the label text to top
        #label.setAlignment(Qt.AlignCenter) # setting the alignment of the label text to center
        #label.setAlignment(Qt.AlignLeft) # setting the alignment of the label text to left
        #label.setAlignment(Qt.AlignRight) # setting the alignment of the label text to right
        #label.setAlignment(Qt.AlignBottom) # setting the alignment of the label text to bottom

        label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) # setting the alignment of the label text to center (horizontally and vertically), the vertical bar enables us to combine the two alignments

        pixmap = QPixmap("icon.png") # creating a QPixmap object to load an image
        label.setPixmap(pixmap) # setting the pixmap of the label to the loaded image

        label.setScaledContents(True) # setting the label to scale the image to fit the label size
        label.setGeometry(50, 50, label.width(), label.height()) # setting the position and size of the label (x, y, width, height), for the image this time




def main():
    app = QApplication(sys.argv) # creating an instance of the QApplication class
    window = MainWindow() # creating an instance of the MainWindow class
    window.show() # displaying the window
    sys.exit(app.exec_()) # starting the event loop and exiting when the application is closed

if __name__ == "__main__":
    main()