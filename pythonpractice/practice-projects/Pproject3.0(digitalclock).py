# Creating a digital clock using python and CSS like properties

import sys
import time
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.timelabel = QLabel("12:00:00", self)
        self.timer = QTimer(self)
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('Digital Clock')
        self.setGeometry(100, 100, 300, 100)
        self.timelabel.setAlignment(Qt.AlignCenter)
        self.timelabel.setStyleSheet("font-size: 48px; font-family: 'Optimist'; color: #FFFFFF; background-color: #000000;")
        
        layout = QVBoxLayout()
        layout.addWidget(self.timelabel)
        self.setLayout(layout)

        self.timer.timeout.connect(self.updateTime)
        self.timer.start(1000)

        self.updateTime()  # Initialize the time display immediately

    def updateTime(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.timelabel.setText(current_time)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())