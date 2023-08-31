import os

bid_continue = True
bids = {}

def find_highest_bidder(bids_dictionary):
    highest_bid = 0
    for bidder in bids_dictionary:
        bid_amount = bids_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} and won with bid of ${highest_bid}")

print("****************Welcome to the secret auction program.****************\n")
while bid_continue:
    name = input("What is your name?: ")
    price = int(input("What's your bid?: $"))
    bids[name] = price
    anyotherbidders = input("Are there any other bidder? Type 'yes' or 'no'.\n")
    if anyotherbidders == "no":
        bid_continue = False
        print(bids)
        find_highest_bidder(bids)
    else: os.system('clear')



