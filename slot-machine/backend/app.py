from flask import Flask, request, jsonify
from flask_cors import CORS  # ✅ Added CORS support to allow frontend requests
import random
import os

app = Flask(__name__)
CORS(app)  # ✅ Allow frontend (GitHub Pages) to call the API

# Define slot machine parameters
MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100
ROWS = 3
COLS = 3

symbol_count = {
    "A": 2, 
    "B": 4, 
    "C": 6, 
    "D": 8
}

symbol_value = {
    "A": 5, 
    "B": 4, 
    "C": 3, 
    "D": 2 
}

# Slot machine logic
def check_winnings(slots, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = slots[0][line]
        for column in slots:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        all_symbols.extend([symbol] * symbol_count)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    
    return columns

# Flask API routes
@app.route("/spin", methods=["POST"])
def spin():
    data = request.get_json()
    balance = data.get("balance", 0)
    lines = data.get("lines", 1)
    bet = data.get("bet", 1)

    total_bet = bet * lines

    if total_bet > balance:
        return jsonify({"error": f"Insufficient funds. Current balance: ${balance}"}), 400

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)

    new_balance = balance + (winnings - total_bet)

    return jsonify({
        "reels": [[column[row] for column in slots] for row in range(len(slots[0]))],
        "winnings": winnings,
        "winning_lines": winning_lines,
        "new_balance": new_balance
    })

@app.route('/')
def home():
    return "Slot Machine API is running!"

# Ensure Flask runs on the correct port for Render
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
