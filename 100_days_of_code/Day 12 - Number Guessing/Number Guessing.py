import logo
import random

play = True

def main(param_game_mode):
    """Argument takes the game mode then sets the number of tries allowed to the user."""
    if param_game_mode == "easy":
        tries_allowed = 10
    elif param_game_mode == "hard":
        tries_allowed = 5
    compare(tries_allowed)

def compare(param_tries_allowed):
    """Allows user to guess until they're out of guesses."""
    while param_tries_allowed > 0:
        guess = int(input("Make a guess: "))
        if guess == random_number:
            print("You guessed correctly!")
            return
        elif guess > random_number:
            param_tries_allowed -= 1
            print(f"You have guessed too high!\nYou have {param_tries_allowed} attempts to guess the number.")
            
        elif guess < random_number:
            param_tries_allowed -= 1
            print(f"You have guessed too low!\nYou have {param_tries_allowed} attempts to guess the number.")
           
        else:
            param_tries_allowed -= 1
            print(f"Try guessing again\nYou have {param_tries_allowed} attempts to guess the number.")
            
            

while play == True:
    print(logo.logo)
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
    game_mode = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    random_number = random.randint(0,101)
    main(game_mode)
    answer = input("Would you like to play again? ").lower
    if answer == "yes":
        play = True
    elif answer == "no":
        play = False
    else:
        play = False