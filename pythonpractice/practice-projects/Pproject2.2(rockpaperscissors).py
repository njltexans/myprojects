# rock paper scissors game practice project

import random   

options = ["rock", "paper", "scissors"] #list of options for the game
player = None #player choice
cpu = random.choice(options) #cpu choice

player = input("Choose: rock, paper, or scissors: ").lower() #player input

while player not in options: #while player input is not in the options list
    print("No cheating! Choose a valid option: rock, paper, or scissors")
    player = input("Choose: rock, paper, or scissors: ").lower() #player input

print(f"CPU chose: {cpu}") #print cpu choice
print(f"Player chose: {player}") #print player choice


if player in options: #check if player input is in the options list
    if player == cpu: #if player and cpu choice are the same
        print("It's a tie!")
    elif player == "rock":
        if cpu == "paper":
            print("You lose!")
        else:
            print("You win!")
    elif player == "paper":
        if cpu == "rock":
            print("You win!")
        else:
            print("You lose!")
    elif player == "scissors":
        if cpu == "rock":
            print("You lose!")
        else:
            print("You win!")

while True:  # Infinite loop to allow unlimited plays
    print("Play again? Y/N")  # Prompt user to play again
    play_again = input().lower()  # User input
    if play_again != "y":  # If user input is not "y"
        print("Thanks for playing!")  # Print message
        break  # Exit the loop

    # Reset CPU choice and player input for the next round
    cpu = random.choice(options)
    player = input("Choose: rock, paper, or scissors: ").lower()

    while player not in options:  # Validate player input
        print("No cheating! Choose a valid option: rock, paper, or scissors")
        player = input("Choose: rock, paper, or scissors: ").lower()

    print(f"CPU chose: {cpu}")
    print(f"Player chose: {player}")

    if player == cpu:
        print("It's a tie!")
    elif player == "rock":
        if cpu == "paper":
            print("You lose!")
        else:
            print("You win!")
    elif player == "paper":
        if cpu == "rock":
            print("You win!")
        else:
            print("You lose!")
    elif player == "scissors":
        if cpu == "rock":
            print("You lose!")
        else:
            print("You win!")



