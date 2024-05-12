import os
import random
from words import categories

def random_word():
    category = random.choice(list(categories.keys()))
    word = random.choice(categories[category])
    return category.upper(), word.upper()

def generate_blanks(word):
    return "_" * len(word)

def get_guess(used_letters):
    while True:
        guess = input("guess")
        if len(guess) != 1:
            print("guess must be one character")
        elif not guess.isalpha():
            print("guess must be a letter")
        elif guess in used_letters:
            print("you've already used that one")
        else:
            return guess.upper()

def reveal_letters(blanks, word, guess):
    blanks = list(blanks)
    for i, char in enumerate(word):
        if char == guess:
            blanks[i] = guess
    return "".join(blanks) 

def draw_guy(lives):
    print(f"{lives=}")

def main():
    word = random_word()
    blanks = generate_blank(word)
    lives = 6
    used_letter = ""

    while True:
        print(blanks)

        guess = get_guess(used_letters)

        if guess in word:
            blanks = reveal_letters(blanks, word, guess
        else:
            lives -= 1
            print(draw_guy(lives))
            used_letters += guess

        if "_" not in blanks:
            print(word)
            print("you win")
            break

        if lives < 1:
            print(word)
            print("You lose")
            break


main()



import os
import random
from words import categories
import colorama
from colorama import init, Fore, Back, Style
init(autoreset=True)

def get_user_name():
    while True:
        name = input("Enter your name\n").upper()
        if name.isalpha() and len(name) > 1:
            return name
        else:
            print(Fore.RED + 'Your name can only contain letters')
            print(Fore.RED + 'and contain at least two letters.\n')

user_name = get_user_name()
print(f"Welcome {user_name} to the big hangman day.")
print("May the luck be with you...")
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

# Initialize/
def random_word():
    category = random.choice(list(categories.keys()))
    word = random.choice(categories[category])
    return category.upper(), word.upper()

category, word = random_word()
guess = "-" * len(word)
wrong_letters = ""


#Main game loop
while True:
    print(f"\nCategory: {category}")
    print(f"\nCorrect guess: {guess}")
    print(f"\nWrong Guesses: {wrong_letters}\n")

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
        |    los

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
    """
