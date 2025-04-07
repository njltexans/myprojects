# Python banking program

# 1) Show balance
# 2) Deposit
# 3) Withdraw

balance = 0
is_running = True

def show_balance():
    print(f"Your balance is: ${balance:.2f}")


def deposit():
    amount = float(input("Enter how much you would like to deposit: "))

    if amount < 0:
        print("Invalid amount. Please try again.")
        return 0
    else:
        return amount

def withdraw():
    amount = float(input("Enter how much you would like to withdraw: "))

    if amount > balance:
        print("Insufficient funds. Please try again.")
        return 0
    elif amount < 0:
        print("Amount must be greater than 0. Please try again.")
        return 0
    else:
        return amount    

def main():
    while is_running:
        print("Welcome to Noah's Superbank")
        print("1. Show balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice (1-4):")

        if choice == "1":
            show_balance()
        elif choice == "2":
            deposit() += balance
        elif choice == "3":
            balance -= withdraw()
        elif choice == "4":
            is_running = False
        else:
            print("Invalid choice. Please try again.")

    print("Thank you for using Noah's Superbank, have a superrific day!")

if __name__ == "__main__": # Run the program or import it
    main()
            


