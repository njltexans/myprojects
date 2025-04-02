# Python hangman game

import random
import string

# List of words to be guessed
words = ["python", "codingissuperduperfun", "Noahissupercoolandawesome", "javascript"]

# Hangman stages
HANGMAN_PICS = [
    """
      ------
      |    |
      |
      |
      |
      |
    --------
    """,
    """
      ------
      |    |
      |    
      |
      |
      |
    --------
    """,
    """
      ------
      |    |
      |    O
      |    |
      |
      |
    --------
    """,
    """
      ------
      |    |
      |    O
      |   /|
      |
      |
    --------
    """,
    """
      ------
      |    |
      |    O
      |   /|\\
      |   /
      |
    --------
    """,
    """
      ------
      |    |
      |    O
      |   /|\\
      |   / \\
      |
    --------
    """,
    """
      ------
      |    |
      |    O
      |   /|\\
      |   / \\
      | YOU LOSE!
    --------
    """
]

def choose_word(words):
    """Randomly choose a word from the list of words."""
    return random.choice(words)

def display_word(word, guessed_letters):
    """Display the word with guessed letters revealed and others as underscores."""
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def hangman():
    """Main function to play the hangman game."""
    word_to_guess = choose_word(words)  # Randomly select a word
    guessed_letters = set()  # Set to store guessed letters
    attempts_left = len(HANGMAN_PICS) - 1  # Number of incorrect guesses allowed

    print("Welcome to Hangman!")
    print("You have", attempts_left, "attempts to guess the word.")

    while attempts_left > 0:
        print(HANGMAN_PICS[len(HANGMAN_PICS) - 1 - attempts_left])
        print("\nWord to guess:", display_word(word_to_guess, guessed_letters))
        print("Guessed letters:", " ".join(sorted(guessed_letters)))
        print("Attempts left:", attempts_left)

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word_to_guess:
            print("Good guess!")
            if all(letter in guessed_letters for letter in word_to_guess):
                print("\nCongratulations! You guessed the word:", word_to_guess)
                break
        else:
            print("Wrong guess.")
            attempts_left -= 1

    if attempts_left == 0:
        print(HANGMAN_PICS[-1])
        print("\nGame over! The word was:", word_to_guess)

# Start the game
if __name__ == "__main__":
    hangman()
    # ASCII art is already used in the hangman stages above. No additional changes are needed for ASCII art.