import tkinter as tk
from tkinter import ttk

def handle_button_click(clicked_button_text):
    current_text = results_var.get()

    if clicked_button_text == "=":
        try:  # replace with python operators
            expression = current_text.replace("÷", "/").replace("x", "*")
            result = eval(expression)

            if isinstance(result, float) and result.is_integer():  # check if result is an integer (whole number)
                result = int(result)

            results_var.set(result)
        except ZeroDivisionError:  # handle division by zero
            results_var.set("Error: Division by zero")
        except Exception as e:  # handle invalid expressions
            results_var.set("Error: Invalid expression")

    elif clicked_button_text == "C":  # clear the display
        results_var.set("")
    elif clicked_button_text == "%":  # convert to decimal by dividing by 100
        try:
            expression = current_text.replace("÷", "/").replace("x", "*")
            current_number = eval(expression)
            results_var.set(current_number / 100)
        except Exception as e:
            results_var.set("Error")
    elif clicked_button_text == "+/-":  # convert number to negative or positive
        try:
            expression = current_text.replace("÷", "/").replace("x", "*")
            current_number = eval(expression)
            results_var.set(-current_number)
        except Exception as e:
            results_var.set("Error")
    elif clicked_button_text == ".":  # prevent multiple decimals
        if "." not in current_text:
            results_var.set(current_text + clicked_button_text)
    else:  # append the clicked button's text to the current text
        results_var.set(current_text + clicked_button_text)

# Function to handle keyboard input
def handle_key_press(event):
    key = event.char

    # Map keyboard keys to calculator buttons
    key_mappings = {
        "0": "0", "1": "1", "2": "2", "3": "3", "4": "4",
        "5": "5", "6": "6", "7": "7", "8": "8", "9": "9",
        "+": "+", "-": "-", "*": "x", "/": "÷", ".": ".",
        "=": "=", "\r": "=",  # Enter key
        "\x08": "C",  # Backspace key
        "%": "%"
    }

    if key in key_mappings:
        handle_button_click(key_mappings[key])

root = tk.Tk()
root.title("Calculator")

results_var = tk.StringVar()

# Create display widget
display = ttk.Entry(root, textvariable=results_var, font=("Arial", 20), justify='right')
display.grid(row=0, column=0, columnspan=4, sticky="nsew")

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("÷", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("x", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("C", 5, 0, 2), ("+/-", 5, 2), ("%", 5, 3)  # "C" button spans 2 columns
]

# Set up style for tkinter buttons
style = ttk.Style()
style.theme_use("default")
style.configure("TButton", font=("Arial", 20), width=10, height=5)

# Create and place buttons
for button_info in buttons:
    button_text, row, column = button_info[:3]
    colspan = button_info[3] if len(button_info) > 3 else 1  # Handle colspan for "C" button
    button = ttk.Button(root, text=button_text, command=lambda bt=button_text: handle_button_click(bt), style="TButton")
    button.grid(row=row, column=column, columnspan=colspan, sticky="nsew", ipadx=10, ipady=10, padx=5, pady=5)

# Ensure rows and columns expand proportionally
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

# Set window size
width = 500
height = 700
root.geometry(f"{width}x{height}")
root.resizable(False, False)  # prevent resizing of window

# Bind keyboard events
root.bind("<Key>", handle_key_press)  # handle keyboard input
root.bind("<Return>", lambda event: handle_button_click("="))  # if enter is hit, it is the same as clicking =
root.bind("<BackSpace>", lambda event: handle_button_click("C"))  # if backspace is hit, it is the same as clicking C

# Start the main loop
root.mainloop()