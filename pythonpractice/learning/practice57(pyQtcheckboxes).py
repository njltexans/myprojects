# PyQt5 checkboxes

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.checkbox = QCheckBox("Do you like pizza?", self)
        self.initUI()

    def initUI(self):
        self.checkbox.setGeometry(50, 50, 200, 50)
        self.checkbox.setStyleSheet("font-size: 20px;"
                                    "font-family: Arial;"
                                    "color: #000000;"
                                    "background-color: #ffffff;")
        
        self.checkbox.setChecked(False)
        self.checkbox.stateChanged.connect(self.checkbox_changed)

    def checkbox_changed(self, state):
        if state == Qt.Checked:
            print("You like pizza don't you squidward ;)")
        else:
            print("You don't like pizza do you squidward :(")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())