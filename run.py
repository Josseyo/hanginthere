
# Hangman

import os
import random
from words import categories


def get_user_name():
    while True:
        name = input("Enter your name\n.").capitalize()
        if name.isalpha() and len(name) > 1:
             return name
        else:
            print("Your name can only contain letters")
            print("and contain at least two letters.\n")

user_name = get_user_name()
# Initialize/
def random_word():
    category = random.choice(list(categories.keys()))
    word = random.choice(categories[category])
    return category.upper(), word.upper()

category, word = random_word()
guess = "-" * len(word)
wrong_letters = ""

#Print header
print("Welcome to HANGMAN\n")  
print("""
       -------
       |/     
       |    
       |     
       |    
       |---------- 
   0   |         |
  /|\\  |         | 
   |   |         |  
  | |  |         | """)


#Main game loop
while True:
    print(f"\nCategory: {category}")
    print(f"\nCurrent guess: {guess}")
    print(f"\nWrong Guesses: {wrong_letters}")

    #Ask player for a letter and validate
    while True:
        letter = input("\nEnter a letter: ").upper()
        if letter.isalpha() and len(letter) == 1:
            break
        else:
            print("Invalid entry. Enter a single letter.\n")

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
        -------
        |     
        |    
        |     
        |    
        |----------   
        |         |  /..
        |         |    -
        |         | //|//
        |         |   |
        |         | // //""")
        break

    # Print the hangman
    if len(wrong_letters) == 1:
        print("4 lifes left. Try again...")
        print("""
        -------
        |     0
        |    
        |     
        |    
        |----------
        |         |  
        |         |
        |         |
        |         |""")
    elif len(wrong_letters) == 2:
        print("No worries, 3 lifes left...")
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
    elif len(wrong_letters) == 3:
        print("Be careful, only 2 lifes left...")
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
    elif len(wrong_letters) == 4:
        print("Last chance...")
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
    elif len(wrong_letters) == 5:
        print("So sorry...Better luck next time!")
        print("""
        -------
        |     |
        |    0
        |    /|\\
        |     |
        |--  | | --
        |   \\     |
        |    \\    |""")
        break
