MENU = {
    "espresso": {
        "ingredients": {
            "Water": 50,
            "Coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "Water": 200,
            "Milk": 150,
            "Coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "Water": 250,
            "Milk": 100,
            "Coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0
resources = {
    "Water": 300,
    "Milk": 200,
    "Coffee": 100,
}


def generate_report():
    """Prints Resources Report"""
    for key in resources:
        if key == "Water" or key == "Milk":
            print(f"{key}: {resources[key]}ml")
        elif key == "Coffee":
            print(f"{key}: {resources[key]}g")
    print(f"Money: ${profit}")


def is_resource_sufficient(drink_ingredients):
    """Returns True if resources are sufficient else it will return False"""
    for item in drink_ingredients:
        if drink_ingredients[item] >= resources[item]:
            print(f"Sorry, There is not enough {item}.")
            return False
    return True


def process_coins():
    """Returns total calculates from coins inserted"""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when payment is accepted or False if money is insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, ingredients):
    """Deduct the ingredients from the resources"""
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {drink_name}, Enjoy")


is_on = True
while is_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == "off":
        is_on = False
    elif user_choice == "report":
        generate_report()
    else:
        drink = MENU[user_choice]
        # print(drink)
        if is_resource_sufficient(drink["ingredients"]):
            money = process_coins()
            cost_of_drink = drink["cost"]
            if is_transaction_successful(money, cost_of_drink):
                profit += money
                make_coffee(user_choice, drink["ingredients"])


