import random
import os
from words import categories
from men import men


def random_word():
    category = random.choice(list(categories.keys()))
    word = random.choice(categories[category])
    return category.upper(), word.upper()


def generate_blanks(word):
    """
    Generates a string of blanks based on the length of the word.
    """
    blanks = ""
    for char in word:
        if char.isalpha():
            blanks += "_"
    return blanks


def get_guess(used_letters):
    """
    Prompts the user to guess a letter and validates the input.
    """
    while True:
        guess = input("Guess: \n").upper()
        if len(guess) != 1:
            print("Guess must be only one letter\n")
        elif not guess.isalpha():
            print("Guess must be a letter\n")
        elif guess in used_letters:
            print("You've already used that one\n")
        else:
            return guess

def reveal_letters(blanks, word, guess):
    """
    Reveals the letters in the word that match the user's guess.
    """
    blanks = list(blanks)
    for i, char in enumerate(word):
        if char == guess:
            blanks[i] = guess
    return "".join(blanks)


def draw_guy(lives):
    """
    Prints the hangman diagram based on the number of remaining lives.
    """
    return men()[6 - lives]


def display_status(category, blanks, lives, used_letters):
    os.system("clear")
    print()
    print(f"The category is: {category}")
    print()
    print(f"The word is: {blanks}")
    print()
    print(f"Used letters: {used_letters}")
    print()
    print(f"{lives=}")
    print()
    print(draw_guy(lives))
    print("***************************")


def display_instructions():
    os.system("clear")
    print("Welcome to Hangman!")
    print()
    print("*************************************************************")
    print()
    print("-The objective of the game is to guess the hidden word.")
    print("-You have 6 lives. Each incorrect guess will cost you a life.")
    print("-Try to guess the word before you run out of lives!")
    print()
    print("*************************************************************")
    print() 
    print("Press Enter to start the game.")
    print("      *****                   ")
    input()


def gameplay():
    category, word = random_word()
    blanks = generate_blanks(word)
    lives = 6
    used_letters = ""

    while True:
        display_status(category, blanks, lives, used_letters)

        guess = get_guess(used_letters)

        if guess == "SOLVED":
            # function for game over summary
            display_status(category, blanks, lives, used_letters)
            print("You win\n")
            print("********************")
            break

        if guess in word:
            blanks = reveal_letters(blanks, word, guess)
        else:
            lives -= 1
            used_letters += guess

        if "_" not in blanks:
            display_status(category, blanks, lives, used_letters)
            print("Lucky day. You live!\n")
            print("********************")
            break

        if lives < 1:
            blanks = word
            display_status(category, blanks, lives, used_letters)
            print("So sorry. You lose...\n")
            print("********************")
            break
    

def play_again():
    start_over = input("Hit y to play again or any other key to quit \n")
    if start_over.lower() == "y":
        main()
    else:
        exit()


def main():
    display_instructions()
    category, word = random_word()
    blanks = generate_blanks(word)
    lives = 6
    used_letters = ""
    #get_guess(used_letters)
    display_status(blanks, lives, used_letters)
    gameplay()
    play_again()


main()
