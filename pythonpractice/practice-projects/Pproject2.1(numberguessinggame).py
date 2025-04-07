# Creating a number guessing game practice project


import random

lowest = 1
highest = 1000
answer = random.randint(lowest, highest) #access random module and use randint function to generate a random number between lowest and highest
guesses = 0
running = True #once user wins, we will set "is running" to false to stop the game

print("AHOY THERE! Welcome to Captain Noah's Nautical Number Guessing Game! The finest guessing game in all the seven seas!")
print(f"Now guess a number between {lowest} and {highest}. Savvy?")

while running: # while running is true, the game will continue to run
    guess = input("Give me ye guess matey: ")

    if guess.isdigit(): #check if the input is a number
        guess = int(guess)  # Convert guess to an integer for comparison
        guesses += 1
        if guess == answer:
            print(f"YO-HO-HO! You've guessed the number and have the smarts to join my swashbucklin crew! And it only took ye {guesses} tries!")
            running = False
        elif guess < answer:
            print("Arrgh that guess be too low, try a higher number savvy!")
        else:
            print("Avast! That guess be too high, try a lower number ye scallywag!")
    else:
        print("Arrr, that isn't a number matey!")
        print(f"Please enter a NUMBER between {lowest} and {highest}")
