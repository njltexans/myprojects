# Python Weather App that pulls in real time weather data from OpenWeatherMap API

import sys
import os
import requests
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter city name:", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temp_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)

        self.initUI()

        # Connect the button click to the get_weather method
        self.get_weather_button.clicked.connect(self.get_weather)

        # Connect the "Enter" key press to the get_weather method
        self.city_input.returnPressed.connect(self.get_weather)

    def initUI(self):
        self.setWindowTitle("Weather App")

        # Create a vertical layout
        vbox = QVBoxLayout()

        # Add widgets to the layout
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temp_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)

        # Center-align all widgets
        self.city_label.setAlignment(Qt.AlignCenter)  # Center-align the city label
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temp_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        # Set object names for labels
        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.temp_label.setObjectName("temp_label")
        self.description_label.setObjectName("description_label")
        self.emoji_label.setObjectName("emoji_label")

        # Set the layout for the main widget
        self.setLayout(vbox)

        # Apply styles
        self.setStyleSheet("""
            QLabel, QPushButton {
                font-family: Arial;
            }
            QLabel#city_label {
                font-size: 40px;
                font-style: italic;
            }
            QLineEdit#city_input {
                font-size: 30px;
                padding: 10px;
            }
            QPushButton {
                font-size: 30px;
                font-weight: bold;
                background-color: #003300; /* Default dark green */
                color: white;
                padding: 10px;
                border: 2px solid #003300;
                border-radius: 3px;
            }
            QPushButton:hover {
                background-color: #006600; /* Lighter green on hover */
            }
            QPushButton:pressed {
                background-color: #009900; /* Even lighter green when clicked */
            }
            QLabel#temp_label {
                font-size: 40px;
                font-weight: bold;
            }
            QLabel#description_label {
                font-size: 30px;
            }
            QLabel#emoji_label {
                font-family: "Apple Color Emoji"; /* Use a font that supports emojis */
                font-size: 60px;
            }
        """)

        #Connect signal to slot

        self.get_weather_button.clicked.connect(self.get_weather)

    def get_weather(self):
        api_key = os.getenv("WEATHER_API_KEY")
        if not api_key:
            raise ValueError("API key not found. Please set the WEATHER_API_KEY environment variable.")
        city = self.city_input.text()
        if not city:
            self.display_error("Please enter a city name.", emoji="⚠️")
            return

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses (HTTP errors)
            data = response.json()

            if data["cod"] == 200:
                self.display_weather(data)

        except requests.exceptions.HTTPError as http_error:
            if response.status_code == 404:
                self.display_error("City not found", emoji="🌍")
            elif response.status_code == 401:
                self.display_error("Invalid API key", emoji="🔑")
            else:
                self.display_error(f"An error occurred while fetching the weather data.\n{http_error}", emoji="❗")
            print(f"HTTPError: {http_error}")  # Log the error to the terminal

        except requests.exceptions.ConnectionError as conn_error:
            self.display_error("Connection error: Please check your internet connection.", emoji="📡")
            print(f"ConnectionError: {conn_error}")  # Log the error to the terminal

        except requests.exceptions.Timeout as timeout_error:
            self.display_error("Timeout error: The request timed out. Please try again later.", emoji="⏳")
            print(f"TimeoutError: {timeout_error}")  # Log the error to the terminal

        except requests.exceptions.TooManyRedirects as redirect_error:
            self.display_error("Too many redirects: Please check the URL.", emoji="🔄")
            print(f"TooManyRedirects: {redirect_error}")  # Log the error to the terminal

        except requests.exceptions.RequestException as req_error:
            self.display_error("An unexpected error occurred. Please try again later.", emoji="❓")
            print(f"RequestException: {req_error}")  # Log the error to the terminal

    def display_error(self, message, emoji="❌"):
        self.temp_label.setStyleSheet("color: red; font-size: 30px;")
        self.temp_label.setText(message)
        self.emoji_label.setText(emoji)  # Display the emoji for the error
        self.description_label.setText("")  # Clear the description label

    def display_weather(self, weather_data):
        self.temp_label.setStyleSheet("font-size: 75px;")
        temperature = weather_data["main"]["temp"]
        temperature = (temperature * 9/5) - 459.67  # Convert from Kelvin to Fahrenheit
        temperature = round(temperature, 2)
        weather_id = weather_data["weather"][0]["id"]
        weather_description = weather_data["weather"][0]["description"]
        self.description_label.setText(weather_description.capitalize())  # Capitalize the first letter

        self.temp_label.setText(f"{temperature:.0f} °F")  # Display temperature
        self.emoji_label.setText(self.get_weather_emoji(weather_id)) # Display weather emoji
        self.description_label.setText(weather_description.capitalize()) # Display weather description

    @staticmethod
    def get_weather_emoji(weather_id):
        if weather_id >= 200 and weather_id <= 232:
            return ""
        
        elif 300 <= weather_id <= 321:
            return "🌦️"
        
        elif 500 <= weather_id <= 531:
            return "🌧️"
        
        elif 600 <= weather_id <= 622:
            return "❄️"
        
        elif 701 <= weather_id <= 741:
            return "🌁"
        
        elif weather_id == 762:
            return "🌋"
        
        elif weather_id == 771: 
            return "💨"
        
        elif weather_id == 781:
            return "🌪️"
        
        elif weather_id == 800:
            return "☀️"
        
        elif 801 <= weather_id <= 804:
            return "☁️"
        
        else:
            return "🤷‍♂️"
        # Default emoji for unknown weather conditions


if __name__ == '__main__':
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())