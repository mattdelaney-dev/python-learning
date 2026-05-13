import art
print(art.logo)

bids = {}
game_over = True

def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}.")

while game_over:
    user_name = input("What is your name?:")
    user_bid = input("What is your bid?:")
    bids[user_name] = user_bid
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n").lower
    if should_continue == "no":
        game_over = False
        find_highest_bidder(bids)

    elif should_continue == "yes":
        print("\n" * 20)