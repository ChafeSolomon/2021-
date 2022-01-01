import random as rand
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

uanswer = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")

random_answer = rand.randint(0,2)
random_answer = str(random_answer)

if uanswer == '0':
    if random_answer == '1':
        print(f"{rock}\nComputer Answer:\n{paper}\nYou Lose")
    elif random_answer == '2':
        print(f"{rock}\nComputer Answer:\n{scissors}\nYou Win")
    else:
        print(f"{rock}\nComputer Answer:\n{rock}\nYou Tied")

if uanswer == '1':
    if random_answer == '2':
        print(f"{paper}\nComputer Answer:\n{scissors}\nYou Lose")
    elif random_answer == '0':
        print(f"{paper}\nComputer Answer:\n{rock}\nYou Win")
    else:
        print(f"{paper}\nComputer Answer:\n{paper}\nYou Tied")

if uanswer == '2':
    if random_answer == '0':
        print(f"{scissors}\nComputer Answer:\n{rock}\nYou Lose")
    elif random_answer == '1':
        print(f"{scissors}\nComputer Answer:\n{paper}\nYou Win")
    else:
        print(f"{scissors}\nComputer Answer:\n{scissors}\nYou Tied")





