# Generating random numbers in Python

import random # Importing the random module, give access to random number generation

# print(help(random)) # Displaying what we can do with the random module

low = 1
high = 100 #you can replace numbers with variables 

number = random.randint(1, 100) # Generating a random integer between 1 and 100
print(number)

# Generating a random float between 0 and 1
number = random.random() 

options = ['rock', 'paper', 'scissors']
choice = random.choice(options) # Selecting a random item from the list
print(choice)


cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
random.shuffle(cards) # Shuffling the list
print(cards)

#Building a random number generator miniproject

low = 1
high = 100
guesses = 0
number = random.randint(low, high)
print(f'Guess a number between {low} and {high}:')

while True:
    guess = int(input('Enter a number: '))
    guesses += 1

    if guess == number:
        print(f'Congrats! You guessed the number in {guesses} guesses')
        break
    elif guess > number:
        print('Too high')
    else:
        print('Too low')

print("Thanks for playing!")


