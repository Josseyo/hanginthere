import random
from words import words

def random_word():
    return random.choice(words)

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
    print(f"lives remaining: {lives}")

def main():
    word = random_word()
    blanks = generate_blanks(word)
    lives = 6
    used_letters = ""

    while True:
        print(blanks)
        print(f"{used_letters=}")

        guess = get_guess(used_letters)

        if guess in word:
            blanks = reveal_letters(blanks, word, guess)
        else:
            lives -= 1
            print(draw_guy(lives))
            used_letters += guess

        if "_" not in blanks:
            print(f"The word was: {word}")
            print("you win")
            break

        if lives < 1:
            print(f"The word was: {word}")
            print("You lose")
            break

if __name__ == "__main__":
    main()
