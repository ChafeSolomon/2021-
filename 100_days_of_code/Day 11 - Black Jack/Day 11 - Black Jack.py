import random
from art import logo
card_options = ["J", 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
cards = {"user_cards":[],"dealer_cards":[]}
user_cards = cards["user_cards"]
dealer_cards = cards["dealer_cards"]


def card_generator(hit):
    check_winner = False
    hit_me = "hit"
    while hit == True:

        if hit_me == "hit":
            user_cards.append(random.choice(card_options))
            dealer_cards.append(random.choice(card_options))
            if "J" in user_cards or "J" in dealer_cards:
                if "J" in dealer_cards:
                    j = dealer_cards.index("J")
                    j_replace = random.choice(range(2,10))
                    dealer_cards[j] = j_replace
                    print(f"You currently have {user_cards} in you possession")

                
                if "J" in user_cards:
                    j = user_cards.index("J")
                    j_replace = int(input("The Dealer has pulled a Jack from the Deck... would you like it to be 1 or 11? "))
                    user_cards[j] = j_replace
                    print(f"You currently have {user_cards} in you possession")

            hit,check_winner,hit_me = calculate(hit,check_winner,hit_me)
        
        elif hit_me == "stand":
            print(hit)
            check_winner = True
            hit,check_winner,hit_me = calculate(hit,check_winner,hit_me)


        
    return(hit)

def calculate(hit,check_winner,hit_me):
    user_card_value = sum(user_cards)
    dealer_card_value = sum(dealer_cards)
    print(f"You currently have {user_cards} in you possession")
    print(hit)

    if user_card_value > 21 or dealer_card_value == 21:
        print(f"You Lose! Your Hand: {user_card_value} Dealer Hand: {dealer_card_value}")
        hit = False
        hit_me = "stand"
        
           
    elif dealer_card_value > 21 or user_card_value == 21:
        print(f"You Win! Your Hand: {user_card_value} Dealer Hand: {dealer_card_value}")  
        hit = False
        hit_me = "stand"
        
       
    elif check_winner == True:
        if user_card_value > dealer_card_value:
            print(f"You Win! Your Hand: {user_card_value} Dealer Hand: {dealer_card_value}")
            hit = False
            
            
        elif user_card_value < dealer_card_value:
            print(f"You Lose! Your Hand: {user_card_value} Dealer Hand: {dealer_card_value}")
            hit = False
            

    if hit_me == "hit":  
        hit_me = input("Would you like another card? Type: Hit or Stand... ").lower()
                
                
        
    return(hit,check_winner,hit_me)

def main_function():
    hit = True
    
    while hit == True:
        hit = card_generator(hit)
        
print(logo)
main_function()



	