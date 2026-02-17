from game_data import data
from art import logo, vs
import random
import art

asked_data = []

def format_account_data(account):
    """Takes an account as input and return a printable format"""
    return f"{account["name"]}, a {account["description"]}, from {account["country"]}"

def is_asked_before(account):
    """Takes an account as input and checks if it has been used during the game"""
    for acc in asked_data:
        if acc == account:
            return True
    return False

def start_game():
    account_a = random.choice(data)
    game_over = False
    score = 0

    # make the game repeatable
    while not game_over:
        print(logo)

        if score > 0:
            print(f"You're right! Your score is: {score}")

        # adding selectionA to asked data to keep track of all game_data used
        asked_data.append(account_a)

        # generating random game data
        account_b = random.choice(data)

        # if generated data is same as comparing data or the data has been asked before then re-generate
        while account_b == account_a or is_asked_before(account_b):
            account_b = random.choice(data)

        print(f"Compare A: {format_account_data(account_a)}")
        print(vs)
        print(f"Against B: {format_account_data(account_b)}")

        # get answer from user
        answer = input("Who has more followers? Type 'A' or 'B': ").upper()

        # check if user is correct
        if answer == "A" and account_a["follower_count"] > account_b["follower_count"]:
            score += 1
            print("\n" * 20)
        elif answer == "B" and account_b["follower_count"] > account_a["follower_count"]:
            score += 1
            print("\n" * 20)
        else:
            game_over = True
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")

        # making account at position B become the next account at position A
        account_a = account_b

start_game()
