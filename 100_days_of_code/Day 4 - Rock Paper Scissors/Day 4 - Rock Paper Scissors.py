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
images = [rock,paper,scissors]
#Write your code below this line 👇

uanswer = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")

random_answer = rand.randint(0,2)
random_answer = str(random_answer)

if uanswer == '0':
    if random_answer == '1':
        print(f"{images[0]}\nComputer Answer:\n{images[1]}\nYou Lose")
    elif random_answer == '2':
        print(f"{images[0]}\nComputer Answer:\n{images[2]}\nYou Win")
    else:
        print(f"{images[0]}\nComputer Answer:\n{images[0]}\nYou Tied")

if uanswer == '1':
    if random_answer == '2':
        print(f"{images[1]}\nComputer Answer:\n{images[2]}\nYou Lose")
    elif random_answer == '0':
        print(f"{images[1]}\nComputer Answer:\n{images[0]}\nYou Win")
    else:
        print(f"{images[1]}\nComputer Answer:\n{images[1]}\nYou Tied")

if uanswer == '2':
    if random_answer == '0':
        print(f"{images[2]}\nComputer Answer:\n{images[0]}\nYou Lose")
    elif random_answer == '1':
        print(f"{images[2]}\nComputer Answer:\n{images[1]}\nYou Win")
    else:
        print(f"{images[2]}\nComputer Answer:\n{images[2]}\nYou Tied")





