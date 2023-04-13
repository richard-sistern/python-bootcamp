# Requirements

# - Print report
# - Check resources sufficient
# - Proccess Coins
# - Check transaction successful
# - Make coffee

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0

def print_report(resources, money):
    """Prints a status report to screen"""

    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")

def check_resources(order):
    """Returns True if sufficient resources for order, otherwise False"""

    for item in order:
        if order[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        
    return True

def take_coins():
    """Returns total money from inserted coins"""
    print("Please insert coins.")

    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01

    return total

def sell_soul_for_coffee(payment, drink_cost):
    """Returns True when payment accepted, otherwise False."""
    if payment >= drink_cost:
        change = round(payment - drink_cost, 2)
        print(f"Here is ${change} in change.")
        
        global money
        money += drink_cost
        
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        
        return False
    
def make_a_brew(order_ingredients):
    """Deduct coffee ingredients from total resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]

choice = ""


while choice != "off":
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    if choice == "report":
        print_report(resources, money)
    elif choice == "off":
        print("Powering off.")
    elif choice in MENU:
        order = MENU[choice]
        if check_resources(order["ingredients"]):
            payment = take_coins()

            if sell_soul_for_coffee(payment, order["cost"]):
                make_a_brew(order["ingredients"])
                print(f"Here is your {choice} ☕️. Enjoy!")    
    else:
        print("Error creating HOT JAVA LAVA.")