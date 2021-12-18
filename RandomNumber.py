import random as rand

#Generate random number
randomnumber = rand.randrange(0,10)
usernum = ""

#Functions
def func(usernum): 
    usernum = int(input("Guess a number. "))
    if randomnumber > usernum:
        print("Try guessing again with a number higher than your guess. ")
        
    elif randomnumber < usernum:
        print("Try guessing a number lower than your guess. ")

    elif usernum > 10:
        print("That number is not even in range my dude... try again.")
    
    return(usernum)
    
def whileloop():
    while usernum != randomnumber:
        print(usernum)
        usernum = func(usernum)

whileloop()

#Compare number

if usernum == randomnumber:
    print("Great work! You guessed correctly. ")
    answer = input("Answer ")
    if answer == 'Yes':
        whileloop()
    
    else:
        exit[0]




