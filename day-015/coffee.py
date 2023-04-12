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

# Requirements

# - Print report
# - Check resources sufficient
# - Proccess Coins
# - Check transaction successful
# - Make coffee

choice = ""


while choice != "off":
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    if choice == "report":
        print_report(resources, money)
    elif choice == "off":
        print("Powering off.")
    elif choice in MENU:
        print(f"{choice}")
    else:
        print("Error creating HOT JAVA LAVA.")