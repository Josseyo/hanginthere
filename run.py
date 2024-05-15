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
        guess = input("guess: ")
        if len(guess) != 1:
            print("guess must be one character")
        elif not guess.isalpha():
            print("guess must be a letter")
        elif guess in used_letters:
            print("you've already used that one")
        else:
            return guess.upper()

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
    print(category)
    print(blanks)
    print(f"{lives=}")
    print(f"{used_letters}")
    print(draw_guy(lives))


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
                print("You win")
                break

            if guess in word:
                blanks = reveal_letters(blanks, word, guess)
            else:
                lives -= 1
                used_letters += guess

            if "_" not in blanks:
                display_status(category, blanks, lives, used_letters)
                print("You win")
                break

            if lives < 1:
                blanks = word
                display_status(category, blanks, lives, used_letters)
                print("You lose")
                break
    
def play_again():
    start_over = input('hit y to play again or any other key to exit: ')
    if start_over.lower() == "y":
        main()
    else:
        exit()


def main():
    category, word = random_word()
    blanks = generate_blanks(word)
    lives = 6
    used_letters = ""
    display_status(category, blanks, lives, used_letters)
    gameplay()
    play_again()


main()
