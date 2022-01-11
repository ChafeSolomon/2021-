import random
card_options = ["J", 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
cards = {"user_cards":[],"dealer_cards":[]}
user_cards = cards["user_cards"]
dealer_cards = cards["dealer_cards"]
check_winner = False

def card_generator(arg_hit_me):
    user_cards.append(random.choice(card_options))
    dealer_cards.append(random.choice(card_options))
    if "J" in user_cards or "J" in dealer_cards:
        if "J" in dealer_cards:
            j = dealer_cards.index("J")
            j_replace = random.choice(range(2,10))
            dealer_cards[j] = j_replace
            print(f"You currently have {user_cards} is you possession")

        
        if "J" in user_cards:
            j = user_cards.index("J")
            j_replace = int(input("1 or 11? "))
            user_cards[j] = j_replace
            print(f"You currently have {user_cards} is you possession")


    
    arg_hit_me = input("Would you like another card? Type: Hit or Stand... ").lower()
    if arg_hit_me == "hit":
        print(f"You currently have {user_cards} is you possession")
    return arg_hit_me

def main_function():
    hit = True
    hit_me = "hit"
    while hit == True:
        
        hit_me = card_generator(hit_me)
        
        #We should have a dictionary that we can pull from.
        if hit_me == "hit":
            check_winner = False
            hit = calculate(check_winner,hit)
            

        elif hit_me == "stand":
            check_winner = True
            hit = calculate(check_winner,hit)
            


def calculate(arg_check_winner,hit):
    user_card_value = 0
    dealer_card_value = 0
    for n in user_cards:
        user_card_value += n

    for n in dealer_cards:
        dealer_card_value += n

    if arg_check_winner == True:
        if user_card_value > dealer_card_value:
            print(f"You Win! Your Hand: {user_card_value} Dealer Hand: {dealer_card_value}")

        elif user_card_value < dealer_card_value:
            print(f"You Lose! Your Hand: {user_card_value} Dealer Hand: {dealer_card_value}")
            
        hit = False
        return hit


    if user_card_value == 21:
        print(f"You Win! Your Hand: {user_card_value} Dealer Hand: {dealer_card_value}")
        hit = False
    elif user_card_value > 21:
        print(f"You Lose! Your Hand: {user_card_value} Dealer Hand: {dealer_card_value}")
        hit = False
    elif dealer_card_value == 21:
        print(f"You Lose! Your Hand: {user_card_value} Dealer Hand: {dealer_card_value} ")
        hit = False
        
    elif dealer_card_value > 21:
        print(f"You Win! Your Hand: {user_card_value} Dealer Hand: {dealer_card_value}")  
        hit = False

    return hit



main_function()



	