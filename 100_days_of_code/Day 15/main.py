import resource
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()
power_state = True

while power_state == True:
    user_selection = input("What would you like? (espresso/latte/cappuccino): ").lower()
    drink_order = menu.find_drink(user_selection)


    if user_selection in menu.get_items():
        print(f"You have chosen {user_selection}")
        if coffee_maker.is_resource_sufficient(drink_order):
            if money_machine.make_payment(drink_order.cost):
                print("Brewing up some coffee")
                coffee_maker.make_coffee(drink_order)
                print("Success")

    elif user_selection not in menu.get_items():
        print("Please retype your selection")
    


    if user_selection == "off":
        print("Powering Down...")
        power_state = False
    
    if user_selection== "report":
        coffee_maker.report()
        money_machine.report()
