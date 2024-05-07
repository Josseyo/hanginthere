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
print("HANGMAN\n")

#Main game loop
while True:
    print(f"Current Guess: {guess}")
    print(f"Wrong Guesses: {wrong_letters}")

    letter = input("\nEnter a letter: ").upper()

    # Check if the letter is in the word
    if letter in word:
        temp = ""
        for index in range(len(word)):
            if letter == word[index]:
                temp += letter
            elif guess[index] != "-":
                temp += guess[index]
            else:
                temp += "-"
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
    
    


