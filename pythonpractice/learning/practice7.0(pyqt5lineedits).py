# Line edits


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QFormLayout

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.line_edit = QLineEdit(self)
        self.button = QPushButton("Submit", self)
        self.initUI()

    def initUI(self):
        self.line_edit.setPlaceholderText("Enter text here...")

        layout = QHBoxLayout()
        layout.addWidget(self.line_edit)
        layout.addWidget(self.button)

        container = QWidget(self)
        container.setLayout(layout)
        container.setGeometry(50, 50, 400, 100)

        self.line_edit.setFixedHeight(50)
        self.button.setFixedHeight(50)

        self.button.setStyleSheet("font-size: 20px;"
                       "font-family: Arial;"
                       "background-color: lightblue;"
                       "color: black;"
                       "border: 2px solid black;"
                       "border-radius: 5px;")
        self.line_edit.setStyleSheet("font-size: 20px;"
                         "font-family: Arial;"
                         "background-color: white;"
                         "color: black;"
                         "border: 2px solid black;"
                         "border-radius: 5px;"
                         "padding: 10px;")
        
        self.line_edit.setPlaceholderText("Enter your name here...")
        self.button.clicked.connect(self.on_button_click)

    def on_button_click(self):
        text = self.line_edit.text()
        print(f"Button clicked! Name entered: {text}")
        self.line_edit.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())