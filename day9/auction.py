from art import logo

print(logo)
print("\nWelcome to the secret auction!")


bids_list = {}

def winner_bid(bidding_record):
    highest_bid = 0.0
    for key in bidding_record:
        value_bid = bidding_record[key]
        if value_bid > highest_bid:
            highest_bid = value_bid
            winner = key
    print(f"The Highest Bid was {winner} with a bid of ${highest_bid}")

continue_bid = True
while continue_bid:
    name = input("What's your name?: ")
    bid = float(input("What's your bid?: $"))
    bids_list[name] = bid
    answer = input("Do you want to continue? 'Yes' or 'No': ").lower()

    if answer == "no":
        continue_bid = False
        winner_bid(bids_list)
        