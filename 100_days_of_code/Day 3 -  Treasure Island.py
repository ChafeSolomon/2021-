#ascii is just some art for the top of the script.
ascii = '''

           |`-.._____..-'|
           :  > .  ,  <  :
           `./ __`' __ \,'
            | (|_) (|_) |
            ; _  .  __  :
            `.,' - `-. ,'
              `, `_  .'
              /       \
             /         :
            :          |_
           ,|  .    .  | \
          : :   \   |  |  :
          |  \   :`-;  ;  |
          :   :  | /  /   ;
           :-.'  ;'  / _,'`------.         
'''
print(ascii)
print("Welcome to Cat run...")
print("Your mission is to slip out the door before your owners see you.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

direction = input("You run around the house and see you can go two ways... left or right towards the front door.\nWhich way do you go? ").lower()

#Begin Directionals
if direction == 'left':
  direction = input("You see the kids running down the hallway. Do you run or wait for them to pass? ").lower()
  if direction == 'wait':
    print("The kids pass you by not noticing you were standing there to begin with.\n")
    direction = input("The backdoor is in sight! however you can take 3 paths to get there.\nLeft, Right, Forward. Which way do you go? ").lower()
    if direction == 'left':
      print(f"The kids have spotted you going {direction}... GAME OVER")

    elif direction == 'right':
      print(f"The kids have spotted you going {direction}... GAME OVER")
    elif direction == 'forward':
      print(f"The kids have spotted you going {direction}.But you slid under the table and out the back door... YOU JUMP THE GATE TO FREEDOM!!!!\nCongrats you are now free! ")
    else:
      print(f"The kids have spotted you going {direction}... GAME OVER")

  else:
    print("The kids saw movement and ran towards you... they pick you up and lock you in your cage. GAME OVER")
else:
  print("Sorry, The kids saw you coming down the hallway and put you in your cage...  GAMEOVER")
