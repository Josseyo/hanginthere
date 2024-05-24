import random
import os
from words import categories
from men import men
from colorama import Fore, Style, Back, init

# Initialize colorama for cross-platform color support
init(autoreset=True)


def display_instructions():
    """
    Displays the instructions for the Hangman game.
    Clears the screen, prints the welcome message,
    instructions, and waits for the user to press Enter
    to start the game.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    print()
    print("********************* Welcome to Hangman! **********************")
    print()
    print("* " * 33)
    print("*" * 64)
    print()
    print(" -The objective of the game is to guess the hidden word.")
    print(" -You have 6 lives. Each incorrect guess will cost you a life.")
    print(" -Try to guess the word before you run out of lives!")
    print()
    print("*" * 64)
    print("* " * 33)
    print()
    # Wait for Enter to start the game
    print(" To start the game press: Enter")
    print("                         ******* ")
    input()


def random_word():
    """
    Selects a random category and a random word
    from the categories dictionary. Returns the
    category and the word in uppercase.
    """
    category = random.choice(list(categories.keys()))
    word = random.choice(categories[category])
    return category.upper(), word.upper()


def generate_blanks(word):
    """
    Generates a string of blanks based on the length
    of the word. Non-alphabetic characters are kept
    as is.
    """
    return "".join("_" if char.isalpha() else char for char in word)


def get_guess(used_letters):
    """
    Prompts the user to guess a letter and validates
    the input. Ensures the guess is a single letter
    that hasn't been used before.
    """
    while True:
        guess = input("Guess: \n").upper()
        if len(guess) != 1:
            print(Fore.RED + "  Guess must be only one letter\n")
        elif not guess.isalpha():
            print(Fore.RED + "  Guess must be a letter\n")
        elif guess in used_letters:
            print(Fore.RED + "  You've already used that one\n")
        else:
            return guess


def reveal_letters(blanks, word, guess, used_letters):
    """
    -Reveals the letters in the word that match the user's guess.
    -If the letter has already been revealed, it prints a message
    and returns the unchanged blanks.
    -Otherwise, it updates the blanks and adds the guess to the
    used_letters list.
    """
    if guess in blanks:
        print(f" {guess} has already been revealed in the word.")
        used_letters.append(guess)
        return blanks
    else:
        used_letters.append(guess)

    return "".join(char if char.upper() == guess
                   else blanks[i] for i, char in enumerate(word))


def draw_guy(lives):
    """
    Prints the hangman diagram based on the number of
    remaining lives.
    """
    return men()[6 - lives]


def display_status(category, blanks, lives, used_letters):
    """
    Clears the screen and displays the current game status,
    including the category, the word with blanks, the used
    letters, and the remaining lives.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

    print()
    print(f" The category is: {Fore.YELLOW}{category}")
    print(f" The word is: {Fore.YELLOW}{blanks}")
    print(f" Used letters: {Fore.RED}{''.join(used_letters)}")
    print(f" Lives: {Fore.GREEN}{lives}")

    print(draw_guy(lives))
    print("* " * 25)


def gameplay():
    """
    The main game loop.
    -Selects a random word, initializes the game and then enters a loop
    where the user guesses letters.
    -Updates the game state, displays the updated status, and checks for win
    or loss conditions.
    """
    category, word = random_word()
    blanks = generate_blanks(word)
    lives = 6
    used_letters = []
    display_status(category, blanks, lives, used_letters)

    while True:
        guess = get_guess(used_letters)
        if guess == 'SOLVED':
            print(f"The word is: {word}")
            break
        if guess in word:
            blanks = reveal_letters(blanks, word, guess, used_letters)
        else:
            lives -= 1
            used_letters.append(guess)

        # Clear the screen
        os.system('cls' if os.name == 'nt' else 'clear')
        # Display updated status
        display_status(category, blanks, lives, used_letters)

        if '_' not in blanks:
            print(f" The word is: {Fore.YELLOW + word}\n")
            print(Fore.GREEN + " Lucky day. You live!\n")
            print("* " * 25)
            break
        if lives < 1:
            print(f" The word is: {Fore.YELLOW + word}\n")
            print(Fore.RED + " So sorry. You lose...\n")
            print("* " * 25)
            break


def play_again():
    """ Prompts the user to play the game again or quit."""
    start_over = input(
        Fore.GREEN + " Hit 'y' to play again!"
        " Or any other key to quit.\n").lower()
    if start_over == "y":
        main()
    else:
        print(Fore.YELLOW + "\n Welcome back! See you next time.")
        exit()


def main():
    """
    The entry point of the script.
    -Clears the screen, calls the display_instructions(), gameplay(),
    and play_again() functions.
    -Handles the KeyboardInterrupt exception to exit the script.
    """
    # Clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')

    try:
        display_instructions()
        gameplay()
        play_again()
    except KeyboardInterrupt:
        print(Fore.YELLOW + "\n Welcome back! See you next time.")

        exit()


if __name__ == "__main__":

    main()
