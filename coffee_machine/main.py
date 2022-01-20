from random import choice


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

FLAG_ON = True
money = 0

def show_report():
    print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g")
    print(f"Money: ${money}")

def check_resource_sufficient(ingredients):
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_payment(money_received,bill):
    if money_received >= bill:
        change = round(money_received - bill,2)
        print(f"Here is ${change} in change.")
        global money
        money = money + bill
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(choice, ingredients):
    for item in ingredients:
         resources[item] -= ingredients[item]
    print(f"Here is your {choice} ☕️. Enjoy!")   

def process_coins():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


while FLAG_ON:
    user_response = input("What would you like? (espresso/latte/cappuccino):").lower()
    if user_response == "off":
        FLAG_ON = False
    elif user_response == "report":
        show_report()
    else:
        drink = MENU[user_response]
        if check_resource_sufficient(drink["ingredients"]):
            if process_payment(process_coins(),drink["cost"]):
                make_coffee(user_response, drink["ingredients"])

