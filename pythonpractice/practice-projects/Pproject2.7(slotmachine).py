# Python slot machine project



import random
import time

def spin_row():
    symbols = ["🍒", "🍊", "🍋", "🍉", "🍇"]

    results = []
    for symbol in range(3):
        results.append(random.choice(symbols)) # random.choice() returns a random element from the given sequence, the append to empty list results
    return results

def print_row(row):
    # Display the slot machine row
    print("*" * 15)
    print(" | ".join(row))
    print("*" * 15)

def get_payout(row, bet):
    # Check for a winning combination
    if row[0] == row[1] == row[2]:
        payout = bet * 2
    elif row[0] == row[1] or row[0] == row[2] or row[1] == row[2]:
        payout = bet * 1
    elif row[0] == "🍉":
        return bet * 800
    elif row[0] == "🍋":
        return bet * 5
    elif row[0] == "🍇":
        return bet * 3
    else:
        payout = 0
    return payout
    

def main():
    balance = 100

    print("***********************************")
    print("Welcome to Noah's Notorious Slots!")
    print("Symbols: 🍒  🍊  🍋  🍉  🍇 ")
    print("***********************************")

    symbols = ["🍒", "🍊", "🍋", "🍉", "🍇"]

    while balance > 0:
        print(f"Current balance: ${balance:.2f}")

        bet = input("Enter your bet amount:$ ")

        if not bet.isdigit():
            print("Please enter a valid bet amount.")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient funds.")
            continue

        if bet <= 0:
            print("Bet must be more than zero.")
            continue

        # Deduct the bet from the balance
        balance -= bet

        # Generate a random slot machine row
        row = []
        print("Spiinnnniinnngggg....")
        for i in range(3, 0, -1):
            print(f"{i}...", end="", flush=True)
            time.sleep(1)
        print()  # Move to the next line after the countdown

        row = spin_row()  # Generate the row using the spin_row function

        # Print the row
        print_row(row)

        # Payout logic
        payout = get_payout(row, bet)

        if payout > 0:
            print(f"Congratulations! You won ${payout:.2f}!")
            balance += payout
        else:
            print("You didn't win anything this time. Better luck next spin!")

    print("Game over! You're out of money.")

if __name__ == "__main__":
    main()


