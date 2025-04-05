# Radio buttons

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QButtonGroup
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
        self.initUI()

    def initUI(self):
        # Create radio buttons
        self.radio1 = QRadioButton("Visa", self)
        self.radio2 = QRadioButton("MasterCard", self)
        self.radio3 = QRadioButton("Amex", self)
        self.radio4 = QRadioButton("In-Store", self)
        self.radio5 = QRadioButton("Online", self)

        # Set positions for the radio buttons
        self.radio1.setGeometry(50, 50, 150, 30)
        self.radio2.setGeometry(50, 100, 150, 30)
        self.radio3.setGeometry(50, 150, 150, 30)
        self.radio4.setGeometry(250, 50, 150, 30)
        self.radio5.setGeometry(250, 100, 150, 30)

        # Create button groups
        self.payment_group = QButtonGroup(self)
        self.location_group = QButtonGroup(self)

        # Add buttons to the payment group
        self.payment_group.addButton(self.radio1)
        self.payment_group.addButton(self.radio2)
        self.payment_group.addButton(self.radio3)

        # Add buttons to the location group
        self.location_group.addButton(self.radio4)
        self.location_group.addButton(self.radio5)

        # Set default selections
        self.radio1.setAutoExclusive(False)  # Allow no selection in the payment group
        self.radio1.setChecked(False)       # No default selection for payment group
        self.radio2.setChecked(False)
        self.radio3.setChecked(False)

        self.radio4.setChecked(True)        # Default selection for location group
        self.radio5.setChecked(False)

        # Optional: Connect signals to slots to handle selection changes
        self.payment_group.buttonClicked.connect(self.payment_selected)
        self.location_group.buttonClicked.connect(self.location_selected)

    def payment_selected(self, button): # Methods to handle button clicks
        # This method is called when a payment method is selected
        print(f"Payment method selected: {button.text()}")

    def location_selected(self, button): # Methods to handle button clicks
        # This method is called when a location is selected
        print(f"Location selected: {button.text()}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())