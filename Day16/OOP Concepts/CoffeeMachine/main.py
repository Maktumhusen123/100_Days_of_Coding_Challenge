from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menuobject = Menu()
coffe_maker_obj = CoffeeMaker()
money_machine_obj = MoneyMachine()

print("Welcome to Coffee Machine")
is_on = True
while is_on:
    choice = input(f"What do you like to have?({menuobject.get_items()}report): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffe_maker_obj.report()
        money_machine_obj.report()
    else:
        drink = menuobject.find_drink(choice)
        if coffe_maker_obj.is_resource_sufficient(drink) and money_machine_obj.make_payment(drink.cost):
            coffe_maker_obj.make_coffee(drink)



