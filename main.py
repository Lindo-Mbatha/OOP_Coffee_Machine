from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

x = True

menu = Menu()
coffeemaker = CoffeeMaker()
money_machine = MoneyMachine()

while x is True:
    options = menu.get_items()
    answer = input(f"What would like? ({options})? ").lower()

    if answer == "report":
        coffeemaker.report()
        money_machine.report()
    elif answer == "off":
        x = False
        print("The Coffee Machine is Off.")
    elif answer == "espresso" or "latte" or "cappuccino":
        drink = menu.find_drink(answer)
        coffeemaker.is_resource_sufficient(drink)
        money_machine.make_payment(drink.cost)
        coffeemaker.make_coffee(drink)
    else:
        print("Invalid input, please try again.")
