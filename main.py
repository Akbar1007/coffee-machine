from menu.menu import Menu
from coffee_maker.coffee_maker import CoffeeMaker
from money_machine.money_machine import MoneyMachine

my_money_machine = MoneyMachine()
my_coffee_maker = CoffeeMaker()
my_menu = Menu()

is_on = True
print("Welcome to coffee machine.")

while is_on:
    options = my_menu.get_items()
    choice = input(f"What would you like? {options}: ")
    if choice == 'off':
        is_on = False
        print("Coffee machine is turned off.")
    elif choice == 'report':
        print("")
        my_coffee_maker.report()
        my_money_machine.report()
    else:
        drink = my_menu.find_drink(choice)
        if my_coffee_maker.is_resource_sufficient(drink) and my_money_machine.make_payment(drink.cost):
            my_coffee_maker.make_coffee(drink)
