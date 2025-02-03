import random

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


def check_winnings(slots, lines, bet, values): #function to check winnings
    winnings = 0 #initializes winnings to zero
    winning_lines = []
    for line in range(lines): #for loop to check each line
        symbol = slots[0][line] #assigns first column value to symbol
        for column in slots:
            symbol_to_check = column[line] #assigns column value to symbol_to_check
            if symbol != symbol_to_check: #if statement to check if symbol is not equal to symbol_to_check
                break
        else: #if symbol is equal to symbol_to_check, prints message below and calculates winnings
            print("You win!")
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines #returns winnings to main program


def get_slot_machine_spin(rows, cols, symbols): #function to generate slot machine values
    all_symbols = [] #empty list to store all symbols
    for symbol, symbol_count in symbols.items():
        for i in range(symbol_count):
            all_symbols.append(symbol)



    columns = [] #empty list to store columns
    for col in range(cols):
        column = []
        current_symbols = all_symbols[:] #copy of all symbols so we can remove symbols from it using slice operator
        for row in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value) #removes symbol from current symbols list
            column.append(value)
        
        columns.append(column) #appends column to columns list
    return columns #returns columns list to main program



def print_slot_machine(columns): #function to print slot machine values
    for row in range(len(columns[0])): #for loop to print each row
        for i, column in enumerate(columns): #for loop to print each column:
            if i != len(columns) - 1:
                print(column[row], "|", end=" ")
            else:
                print(column[row])



def deposit(): #collects user input for deposit amount
    while True:
        amount = input("How much do you want to deposit? $") #while loop to ask user for amount
        if amount.isdigit(): #if statement to check if input is valid number
            amount = int(amount) #converts input to integer
            if amount > 0: #checks if amount is greater than zero
                break #breaks loop if amount is valid
            else: #if amount is not greater than zero, prints invalid entry message below and loops back to ask user for amount
                print("Invalid entry. Amount must be greater than zero.")
        else: #if input is not a number, prints message below and loops back to ask user for amount
            print("Please enter a number.")
    return amount  #returns valid amount to main program



def get_number_of_lines(): #collects user input for number of lines 1 through 3
    while True:
        lines = input(
            "Enter the number of lines you want to bet on (1-" + str(MAX_LINES) + ")? ") #while loop to ask user for amount of lines user wants to bet
        if lines.isdigit(): #if statement to check if input is valid number
            lines = int(lines) #converts input to integer
            if 1 <= lines <= MAX_LINES: #checks if entry is within vald range
                break #breaks loop if amount is valid
            else: #if amount is not valid, prints invalid entry message below and loops back to ask user for amount
                print("Please enter valid number of lines.")
        else: #if input is not a number, prints message below and loops back to ask user for amount
            print("Please enter a number.")
    return lines  #returns valid amount to main program



def get_bet(): #collects user input for bet amount
    while True:
        amount = input("Enter the amount you want to bet ($" + str(MIN_BET) + "-" + str(MAX_BET) + "): ") #while loop to ask user for bet amount
        if amount.isdigit(): #if statement to check if input is valid number
            amount = int(amount) #converts input to integer
            if MIN_BET <= amount <= MAX_BET: #checks if bet is within valid range
                break #breaks loop if amount is valid
            else: #if amount is not valid, prints invalid entry message below and loops back to ask user for amount
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.") #f-string to print message with variables
        else: #if input is not a number, prints message below and loops back to ask user for amount
            print("Please enter a number.")
    return amount  #returns valid amount to main program

def spin(balance):
    lines = get_number_of_lines() #calls get_number_of_lines function and assigns return value to lines variable
    while True: 
        bet = get_bet() #calls get_bet function and assigns return value to bet variable
        total_bet = bet * lines #calculates total bet by multiplying bet and lines

        if total_bet > balance: #if statement to check if total bet is more than current balance
            print(f"Insufficient funds. Your current balance is ${balance}") #prints message if total bet is more than balance
        else:
            break #breaks loop if total bet is less than or equal to balance

    print(f"You are betting ${bet} on {lines} lines. Total bet is currently: ${total_bet}") #prints bet and lines to check if they are correct

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count) #calls get_slot_machine_spin function and assigns return value to slots variable
    print_slot_machine(slots) #calls print_slot_machine function to print slot machine values
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value) #calls check_winnings function and assigns return value to winnings variable
    print (f"You won ${winnings}") #prints winnings
    print(f"You won on:", *winning_lines) #prints winning lines using a splat (unpacking operator) listing lines user won on
    return winnings - total_bet #returns winnings minus total bet to main program from this spin



def main(): #main function to run program
    balance = deposit() #calls deposit function and assigns return value to balance variable   
    while True: #while loop to run game
        print(f"Your balance is ${balance}") #prints balance
        play = input("Press enter to play! (q to quit)") #asks user to press enter to spin
        if play == "q":
            break
        balance += spin(balance) #adds winnings to balance
        play_again = input("Do you want to play again? (y/n): ") #asks user if they want to play again
        if play_again.lower() != "y": #if statement to check if user input is not "y"
            break #breaks loop if user input is not "y"
    print(f"Thanks for playing! You left with ${balance}") #prints message when user quits game, shares balance

main() #calls main function to run program

