import random
from items import items
from logo import logo


score = 0
high_score = 0
play = True

def main():
    # create a dictionary that stores the information we are comparing.
    global items
    print(logo)
    
    while play == True:
        options = {}
        # set a value for the 1st object and 2nd object randomly. 
        option_one = random.choice(list(items))
        option_two = random.choice(list(items))
        option_one_key = items[option_one]
        option_two_key = items[option_two]

        # while loop that prevents it picking two of the exact same option
        if score > 0:
            option_one = correct_answer
            option_one_key = items[option_one]

        while option_one_key == option_two_key:
            option_two = random.choice(list(items))
            option_two_key = items[option_two]     

        if play == True:
            # compare_value = compare(option_one_key,option_two_key)


            options[option_one] = option_one_key
            options[option_two] = option_two_key

            correct_answer = game(option_one,option_two,options)

        else:
            return
    print(f"Thank you for playing!\nYour score is {score}! The current High Score is {high_score}")
    
def game(option_one,option_two,options):
    global high_score
    global score
    global play
    
    print(f"Based off the two options! Do you think that {option_two} has a Higher or Lower amount of googe searches than {option_one}?")
    
    
    # prompt the user asking for which choice is correct. 
    user_responce = input("Sooooo Higher or Lower? ").lower()
    if user_responce == "higher":
        if options[option_two] > options[option_one]:
            print(f"You are correct! Here are the resuts!\n{options}\nLets move on. ")
            score += 1
            correct_answer = option_two
            return correct_answer
        else:
            if score > high_score:
                high_score = score
            print("You Lose")
            play = False
            return

    elif user_responce == "lower":
        if items[option_two] < items[option_one]:
            print(f"You are correct! Here are the resuts!\n{options}\nLets move on. ")
            score += 1
            correct_answer = option_one
            return correct_answer
        else:
            print("You lose")
            if score > high_score:
                high_score = score
            play = False
            return


print("Welcome to Higher or Lower!")
main()
while input("Would you like to play again? ").lower() == "yes":
    play = True
    score = 0
    main()
