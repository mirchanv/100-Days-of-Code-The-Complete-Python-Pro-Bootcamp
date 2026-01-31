import art

print(art.logo)

def get_highest_bidder():
    winner = ""
    max_bid = 0

    for key in all_auction_bids:
        if all_auction_bids[key] > max_bid:
            winner = key
            max_bid = all_auction_bids[key]
    print(f"The winner is {winner} with a bid of ${max_bid}")

print("Welcome to the secret auction program")
all_auction_bids = {}
should_continue = True

while should_continue:
    name = input("What is your name?: ")
    bid = float(input("What is your bid?: $"))
    all_auction_bids[name] = bid
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.")

    if other_bidders.lower() == "no":
        should_continue = False
        get_highest_bidder()
    else:
        print("\n" * 20)





