# python 3.8.1
# Hangman
# Credit Tokyo ed-tech
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import os
os.system ("clear")
import random
from words import categories

# Initialize
def random_word():
    category = random.choice(list(categories.keys()))
    word = random.choice(categories[category])
    return category.upper(), word.upper()

category, word = random_word()
guess = "-" * len(word)
wrong_letters = ""

#Print header
print("HANGMAN\n")  
print("""
-------
|     
|    
|     
|    
|----------
|         |
|         |
|         |""")

#Main game loop
while True:
    print(f"\nCategory: {category}")
    print(f"Current guess: {guess}")
    print(f"\nWrong Guesses: {wrong_letters}")

    letter = input("\nEnter a letter: ").upper()


    # Check if the letter is in the word
    if letter in word:
        temp = ""
        for index, char in enumerate(word):
            if char == letter:
                temp += letter
            else:
                temp += guess[index]
        guess = temp
    else:
        wrong_letters += letter
    
    # Check for a winner
    if word == guess:
        print("Happy day! You win!")
    # print the hangman
        print("""
      o
    //|//
      |
    // //
    """)
        exit()

    # Print the hangman
    if len(wrong_letters) == 0:
        print("""
    -------
    |     
    |    
    |     
    |    
    |----------
    |         |
    |         |
    |         |""")

    # Print the hangman
    if len(wrong_letters) == 1:
        print("""
    -------
    |     0
    |    
    |     
    |    
    |----------
    |         |
    |         |
    |         |""")

    # Print the hangman
    if len(wrong_letters) == 2:
        print("""
    -------
    |     0
    |     |
    |     |
    |    
    |----------
    |         |
    |         |
    |         |""")

    # Print the hangman
    if len(wrong_letters) == 3:
        print("""
    -------
    |     0
    |    \\|/
    |     |
    |    
    |----------
    |         |
    |         |
    |         |""")
    
    # Print the hangman
    if len(wrong_letters) == 4:
        print("""
    -------
    |     0
    |    \\|/
    |     |
    |    / \\
    |----------
    |         |
    |         |
    |         |""")

     # Print the hangman
    if len(wrong_letters) == 5:
        print("""
    -------
    |     |
    |    0
    |    /|\\
    |     |
    |--  | | --
    |   \\     |
    |    \\    |""")
        print("Sorry, better luck next time...")
        exit()
    
    


