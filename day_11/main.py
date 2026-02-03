import random
from art import logo

def deal_card():
    """
    :return: returns a new random card from the deck
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """
    calculates score of given card deck
    :param cards: list of cards
    :return: score of hand
    """
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(user_score, computer_score):
    """
    :param user_score:
    :param computer_score:
    :return: prints the result based on the scores provided
    """
    if user_score == computer_score:
        print("It's a draw 😬")
    elif computer_score == 0:
        print("Blackjack! Computer wins 😎")
    elif user_score == 0:
        print("Blackjack! You win 😎")
    elif user_score > 21:
        print("Bust! You went over. You lose 😭")
    elif computer_score > 21:
        print("Bust! You win.")
    elif user_score > computer_score:
        print("You win!")
    else:
        print("Computer wins!")

def start_game():
    print(logo)
    user_cards = []
    computer_cards = []
    user_score = -1
    computer_score = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    compare(user_score, computer_score)

    play_again = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

    if play_again == "y":
        start_game()
    else:
        print("Blackjack will miss you! See you soon.")
        exit()

start_game()