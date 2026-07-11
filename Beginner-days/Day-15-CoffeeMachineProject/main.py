import time
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

def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.10
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def is_transaction_successful(drink_cost):
    """Returns True if the transaction is successful, False otherwise."""
    money_received = process_coins()
    if money_received >= drink_cost:
        change = money_received - drink_cost
        print(f"Here is ${change:.2f} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return is_transaction_successful(drink_cost)

machine_on = True
money = 0.00

while machine_on:
    while (drink_name := input(f"What would you like?\n- 'Espresso = {MENU['espresso']['cost']}$'\n- 'Latte = {MENU['latte']['cost']}$'\n- 'Cappuccino = {MENU['cappuccino']['cost']}$'\n").lower()) not in ['espresso', 'latte', 'cappuccino', 'off']:
        if drink_name == "report":
            print("\n----------------------------------")
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}")
            print(f"Money: ${money:.2f}")
            print("----------------------------------\n")
        else:
            print("Invalid input. Please enter 'Espresso', 'Latte', or 'Cappuccino'.")
    

    if drink_name == "off":
        machine_on = False
        print("Thank you for using the coffee machine. Goodbye!")
    else:
        drink = MENU[drink_name]
        print(f"\nYou have selected {drink_name}.")
        print("Cost: ${:.2f}".format(drink["cost"]))
        print("\nChecking resources...")
        
        if is_resource_sufficient(drink["ingredients"]):
            print("Resources are sufficient. Please insert coins.\n")
            if is_transaction_successful(drink["cost"]):
                money += drink["cost"]
                for item in drink["ingredients"]:
                    resources[item] -= drink["ingredients"][item]
                    if resources[item] == 0:
                        print(f"Sorry, we are out of {item}.")
                    print(f"\nServing {item}...", end="")
                    time.sleep(1)
                print(f"\n\nHere is your {drink_name}. Enjoy!")

        answer = input("\nWould you like to order another drink? (yes/no)\n").lower()
        if answer == "no" or answer == "off":
            machine_on = False
            print("Thank you for using the coffee machine. Goodbye!")
        