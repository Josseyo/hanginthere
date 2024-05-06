# Hangman
# Credit Tokyo ed-tech
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import os
os.system ("clear")

# Initialize
word = "YOMACO"
guess = "------"
wrong_letters = ""

#Print header
print("HANGMAN/n")

#Main game loop
while True:
    print(f"Current Guess: {guess}")

    letter = input("Enter a letter: ").upper()

    # Check if the letter is in the word
    if letter in word:
        print("CORRECT, GOOD GUESS!")
    else:
        print("WRONG, TRY AGAIN")

