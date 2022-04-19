import Menu
import gfx

menu = Menu.MENU
resources = Menu.resources
profit = Menu.profit
espresso_key = menu["espresso"]
latte_key = menu["latte"]
cappucino_key = menu["cappuccino"]
power_state = True

def money_collection():
    global profit
    total_value = 0
    collected_coins = {}
    #Could have done this section by using a list but found it a lot easier to just do it this way even through its redundant. 
    while total_value < menu[user_selection]["cost"]:
        collected_coins["collected_quarters"] = float(input("Please type in the number of Quarters inserted. "))
        collected_coins["collected_quarters"] *= .25 
        collected_coins["collected_dimes"] = float(input("Please type in the number of Dimes inserted. "))
        collected_coins["collected_dimes"] *= .10
        collected_coins["collected_nickles"] = float(input("Please type in the number of Nickles inserted "))
        collected_coins["collected_nickles"] *= .05
        collected_coins["collected_pennies"] = float(input("Please type in the number of Pennies inserted. "))
        collected_coins["collected_pennies"] *= .01
        #Collects all of the cash inserted and adds it up by taking the values from the dictionary for each value.
        for i in collected_coins:
            total_value += collected_coins[i]
        if total_value >= menu[user_selection]["cost"]:
            #Refund if statment
            if total_value > menu[user_selection]["cost"]:
                refund = total_value - menu[user_selection]["cost"]
                print(f"Please collect the remaining ${refund}")
            
            print("Vending")
            profit += float(total_value - refund)
            return True
        #if the amount inserted is less than the cost of the drink
        elif total_value < menu[user_selection]["cost"]:
            print("Not enough money to purchase this selection.")
            if input("Would you like to refund and choose another option? Yes or No ").lower() == "yes":
                return False

def resource_check(param_user_selection):
    #We plug the users selection into a for loop that will cycle through the ingredients and check if the resources are greater than the ing to make it
    failed_items = []
    failed_count = 0
    menu_ingredients = menu[param_user_selection]["ingredients"]
    for i in menu_ingredients:
        if menu_ingredients[i] > resources[i]:
            failed_count += 1
            failed_items.append(i)

    if failed_count == 1:
        print(f"Please refill {failed_items[0]} since it has depleted")
        return False
    elif failed_count == 2:
        print(f"Please refill {failed_items[0]} and {failed_items[1]} since they have depleted")
        return False
    elif failed_count == 3:
        print(f"Please refill {failed_items[0]}, {failed_items[1]}, and {failed_items[2]} since they have depleted")
        return False

    return True

def brew(param_user_selection):
    print(gfx.cup)
    menu_ingredients = menu[param_user_selection]["ingredients"]
    for i in menu_ingredients:
        resources[i] -= menu_ingredients[i]
    print(f"Here is your {user_selection}. Enjoy!")

while power_state == True:
    print(gfx.coffee)
    coffee_bool = False
    user_selection = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_selection in list(menu):
        print(f"You have chosen {user_selection}")
        coffee_bool = resource_check(user_selection)
    if user_selection not in list(menu):
        print("Please retype your selection")
    
    if coffee_bool:
        money_bool = money_collection()

    #No need to ask if its == True since its set to true and will go if it checks. 
    if coffee_bool and money_bool:
        brew(user_selection)
    elif user_selection == "off":
        print("Powering Down...")
        power_state = False
    
    elif user_selection == "report":
        print(f"The current avalible resources are as follows:\nWater: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nProfit: ${profit}")
