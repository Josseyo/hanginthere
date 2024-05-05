# Your code goes here.
# You can delete these comments, but do not change the name of this file
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

    letter = input("Please enter a letter: ").upper()

    # Check if the letter is in the word
    if letter in word:
        print("GOOD GUESS!")
    else:
        print("BAD GUESS")