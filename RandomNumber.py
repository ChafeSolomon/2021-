import random as rand

#Functions
def func(usernum): 
    usernum = int(input("Please guess a number between 0-10. "))
    if randomnumber > usernum:
        print("Try guessing again with a number higher than your guess. ")
        
    elif randomnumber < usernum:
        print("Try guessing a number lower than your guess. ")

    elif usernum > 10:
        print("That number is not even in range my dude... try again.")
    
    return(usernum)  
def whileloop():
    global usernum
    global randomnumber
    usernum = ""
    randomnumber = rand.randrange(0,10)

    if usernum == "":
        print("Welcome to the number generator!")
        pass

    while usernum != randomnumber:
        usernum = func(usernum)

    while usernum == randomnumber:
        print("Great work! You guessed correctly. ")
        answer = input("Would you like to continue? ")
        if answer == 'Yes':
            whileloop()

        else:
            print("Thank you for playing")
            break

#Compare number

whileloop()




