"""
Created by: Shingai Dzinotyiweyi

Task 2: Number Guessing Game
Write a program that randomly generates a number between 1 and 100. The user has to guess
the number, and the program will give feedback if the guess is too high or too low.

Objectives:
✅ - Use the random module to generate a random number.
✅ - Give the user multiple attempts to guess the number.
✅ - Provide appropriate feedback (e.g., "Too high" or "Too low").
✅ - Exit the game if the user guesses correctly or after a maximum number of attempts.
"""

import random

def start_game():
    """
    This function starts the guessing game with x attempts based on the user's difficulty
    """

    # Setting the game's target
    target = random.randint(0, 10)
    retry = True
    attempts = 0

    difficulty = int(input("Select Difficulty (Numbers Only):\n"
                       "1. Easy: (10 Attempts)\n"
                       "2. Medium: (5 Attempts)\n"
                       "3. Hard: (3 Attempts)\n"
                       "4. All or Nothing (1 Attempt)\n: "))

    if difficulty == 1:
        attempts = 10

    elif difficulty == 2:
        attempts = 5

    elif difficulty == 3:
        attempts = 3

    elif difficulty == 4:
        attempts = 1
    else:
        print("Invalid Entry!")
        exit()

    print("\n----------------------------\n")

    while retry and attempts > 0:

        print("Attempts left:", attempts)
        user_input = int(input("Guess the number between 1 - 10: "))

        if user_input < target:
            print("....higher\n\n")
        elif user_input > target:
            print("....lower\n\n")
        else:
            print("DING DING ✅")
            print("\n-----------------------\n")
            break

        # Reduce attempts until 0
        attempts -= 1
        if attempts == 0:
            print("Game Over!\nThe number was:", target)

    user_input = int(input("\nPlay Again? (Numbers Only)\n"
                           "1. Yes\n"
                           "2. No\n: "))

    # Recursively start the game again....because why not :)
    if user_input == 1:
        print("\n-----------------------\n")
        start_game()

    # Ends the game
    else:
        print("Thanks for playing...")
        exit()

# Calls function to start the game
start_game()