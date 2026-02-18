import sys
from machine_data import MENU, resources

profit = 0

def print_report():
    """Gives the current status of the coffee machine resources"""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")

def check_resources(drink):
    """Returns True when ordered drink can be made, False if ingredients are insufficient."""
    selected_drink = MENU[drink]
    for item_needed in selected_drink["ingredients"]:
        if selected_drink["ingredients"][item_needed] > resources[item_needed]:
            print(f"Sorry there is not enough {item_needed}.")
            return False
    return True

def update_resources(drink, cost):
    """Updates the coffee machine resources after each successful transaction"""
    for item in MENU[drink]["ingredients"]:
        resources[item] -= MENU[drink]["ingredients"][item]
    global profit
    profit += cost

def order_summary(drink, cost, total_coins, change):
    """Displays a summary of your order in a neatly formatted style"""
    print(f"============== DIGITAL COFFEE MACHINE ==============\n"
          f"\t ordered drink   : {drink}\n"
          f"\t total bill      : ${cost}\n"
          f"\t coins inserted  : ${total_coins}\n"
          f"\t customer change : ${change} in change.\n"
          f"\t Preparing your {drink}. Please wait ⌛️...\n"
          f"\t Here is your {drink} ☕️.Enjoy!\n"
          f"====================================================\n")

def process_transaction(paid_amount, drink):
    """Checks if paid amount is enough for the drink requested"""
    cost_of_drink = MENU[drink]["cost"]
    if paid_amount < cost_of_drink:
        print("Sorry that's not enough money. Money refunded.")
    elif paid_amount >= cost_of_drink:
        change = round(paid_amount - cost_of_drink, 2)
        update_resources(drink, cost_of_drink)
        order_summary(drink, cost_of_drink, paid_amount, change)

def process_coins(drink):
    """Takes a drink as a parameter and prompts users to insert coins"""
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01

    # Calling method to process payment
    process_transaction(total, drink)

machine_status = True

while machine_status:
    # TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt
    if user_input == "off":
        machine_status = False
        sys.exit(0)

    # TODO: 3. Print report
    elif user_input == "report":
        print_report()

    # TODO: 4. Check the user’s input to decide what to do next
    elif user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
        if check_resources(user_input):
            process_coins(user_input)
