# Creating a stopwatch using python and CSS like properties

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QHBoxLayout

from PyQt5.QtCore import QTimer, QTime, Qt

class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0, 0, 0, 0)
        self.time_label = QLabel("00:00:00.00", self)
        self.start_button = QPushButton("Start", self)
        self.stop_button = QPushButton("Stop", self)
        self.reset_button = QPushButton("Reset", self)
        self.timer = QTimer(self)
        self.initUI()


    def initUI(self):
        self.setWindowTitle("Noah's Super Stopwatch")

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        vbox.addWidget(self.start_button)
        vbox.addWidget(self.stop_button)
        vbox.addWidget(self.reset_button)

        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter)

        hbox = QHBoxLayout()

        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)

        vbox.addLayout(hbox)

        self.setStyleSheet("""
            QWidget {
            background-color: #003300; /* Deeper, darker green background */
            color: #FFFFFF;
            font-family: 'Optimist';
            font-size: 35px;
            font-weight: bold;
            }
            QLabel {
            background-color: #000000; /* Black background for the numbers */
            color: #FFFFFF; /* White text for contrast */
            border-radius: 10px;
            padding: 20px;
            font-weight: bold;
            }
            QPushButton {
            background-color: #000000; /* Black background for the buttons */
            color: #FFFFFF; /* White text for contrast */
            border-radius: 15px;
            padding: 20px;
            font-weight: bold;
            }
            QPushButton:hover {
            background-color: #333333; /* Dark gray background on hover */
            }
        """)

        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update_time)


    def start(self):
        self.timer.start(10)

    def stop(self):
        self.timer.stop()

    def reset(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.time_label.setText(self.format_time())

    def format_time(self):
        hours = self.time.hour()
        minutes = self.time.minute()
        seconds = self.time.second()
        milliseconds = self.time.msec() // 10  # Convert milliseconds to tenths of a second
        return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:02}"
        
    def update_time(self):
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.format_time())

        # Update the label with the formatted time
        self.time_label.setText(self.format_time())
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    stopwatch = Stopwatch()
    stopwatch.show()
    sys.exit(app.exec_())