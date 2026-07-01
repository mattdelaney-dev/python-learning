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
    "profit": 0
}
# Main code


def compare_price(drink, cost):
    money = drink["cost"]
    if cost >= money:
        return True
    else:
        return False

def compare_resources(drink):
    ingredients = drink["ingredients"]

    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry that's not enough {item}")
            return False

    return True

def make_coffee(drink):
    ingredients = drink["ingredients"]

    for item in ingredients:
        resources[item] -= ingredients[item]

coffe_on = True

while coffe_on:
    coffe_type = input("What would you like? (espresso/latte/cappuccino): ")
    if coffe_type == "off":
        coffe_on = False
    elif coffe_type == "report":
        for key in resources:
            print(f"{key.title()}: {resources[key]}")
    elif coffe_type in MENU:
        if compare_resources(MENU[coffe_type]):
            print("Please insert coins.\n")
            quarters = int(input("How many quarters? "))
            dimes = int(input("How many dimes? "))
            nickles = int(input("How many nickles? "))
            pennies = int(input("How many pennies? "))
            costs = (0.25 * quarters) + (0.1 * dimes) + (0.05 * nickles) + (0.01 * pennies)
            if not compare_price(MENU[coffe_type], costs):
                print("Sorry that's not enough money")
            else:
                print("You have enough!")
                resources["profit"] += MENU[coffe_type]["cost"]
                make_coffee(MENU[coffe_type])
                print(f"Here is your {coffe_type}!")
                change = costs - MENU[coffe_type]["cost"]
                print(f"Here is ${round(change, 2)} in change.")

