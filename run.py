import random
import os
from words import categories
from men import men
from colorama import Fore, Style, Back, init

init(autoreset=True)


def display_instructions():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Welcome to Hangman!")
    print()
    print("*" * 72)
    print()
    print("-The objective of the game is to guess the hidden word.")
    print("-You have 6 lives. Each incorrect guess will cost you a life.")
    print("-Try to guess the word before you run out of lives!")
    print()
    print("*" * 72)
    print()
    print("Press Enter to start the game.")
    print("*" * 10)
    input()  # Wait for Enter to start the game

def random_word():
    category = random.choice(list(categories.keys()))
    word = random.choice(categories[category])
    return category.upper(), word.upper()


def generate_blanks(word):
    """ Generates a string of blanks based on the length of the word. """
    return "".join("_" if char.isalpha() else char for char in word)


def get_guess(used_letters):
    """ Prompts the user to guess a letter and validates the input. """
    while True:
        guess = input("Guess: \n").upper()
        if len(guess) != 1:
            print(Fore.RED + "Guess must be only one letter\n")
        elif not guess.isalpha():
            print(Fore.RED + "Guess must be a letter\n")
        elif guess in used_letters:
            print(Fore.RED + "You've already used that one\n")
        else:
            return guess

def reveal_letters(blanks, word, guess, used_letters):
    """ Reveals the letters in the word that match the user's guess. """
    if guess in blanks:
        print(f"{guess} has already been revealed in the word.")
        used_letters.append(guess)
        return blanks
    else:
        used_letters.append(guess)
        return "".join(char if char.upper() == guess else blanks[i] for i, char in enumerate(word))


def draw_guy(lives):
    """ Prints the hangman diagram based on the number of remaining lives. """
    return men()[6 - lives]

def display_status(category, blanks, lives, used_letters):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"The category is: {category}")
    print(f"The word is: {blanks}")
    print(f"Used letters: {''.join(used_letters)}")
    print(f"{lives=}")
    print(draw_guy(lives))
    print("*" * 25)


def gameplay():
    category, word = random_word()
    blanks = generate_blanks(word)
    lives = 6
    used_letters = []
    display_status(category, blanks, lives, used_letters)

    while True:
        guess = get_guess(used_letters)
        if guess == 'SOLVED':
            print(f"The hidden word is: {word}")
            break
        if guess in word:
            blanks = reveal_letters(blanks, word, guess, used_letters)
        else:
            lives -= 1
            used_letters.append(guess)
        
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
        display_status(category, blanks, lives, used_letters)  # Display updated status

        if '_' not in blanks:
            print(f"The hidden word is: {word}")
            print(Fore.GREEN + "Lucky day. You live!\n")
            print("* " * 20)
            break
        if lives < 1:
            print(f"The hidden word is: Fore.YELLOW + {word}")
            print(Fore.RED + "So sorry. You lose...\n")
            print("* " * 20)
            break


def play_again():
    start_over = input("Hit y to play again or any other key to quit \n").lower()
    if start_over == "y":
        main()
    else:
        exit()

def main():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen

    try:
        display_instructions()
        gameplay()
        play_again()
    except KeyboardInterrupt:
        exit()

if __name__ == "__main__":
    main()