# CSS


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QMainWindow
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QFormLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button1 = QPushButton("Button 1")
        self.button2 = QPushButton("Button 2")
        self.button3 = QPushButton("Button 3")
        self.initUI()

    def initUI(self):
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        hbox = QHBoxLayout()

        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)

        central_widget.setLayout(hbox)

        self.setStyleSheet("""
            QPushButton {
            font-size: 20px;
            font-family: Arial;
            padding: 15px 50px;
            margin: 10px;
            border: 2px solid #000;
            border-radius: 10px;
            background-color: #f0f0f0;
            color: #000;
            text-align: center;  
            }
            QPushButton#button1 {
            background-color: red;
            }
            QPushButton#button1:hover {
            background-color: #ff6666; /* Lighter red */
            }
            QPushButton#button2 {
            background-color: green;
            }
            QPushButton#button2:hover {
            background-color: #66ff66; /* Lighter green */
            }
            QPushButton#button3 {
            background-color: blue;
            }
            QPushButton#button3:hover {
            background-color: #6666ff; /* Lighter blue */
            }
        """)
        self.button1.setObjectName("button1")
        self.button2.setObjectName("button2")
        self.button3.setObjectName("button3")

    def on_button_click(self, button_number):
        print(f"Button {button_number} was clicked!")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())