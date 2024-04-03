# Silent Auction

from art import logo
import os

print(logo)
print("Welcome to the secret auction program.")

bidders = {}
continue_auction = True

def find_highest_bidder(bids):
    highest_bidder = ''
    highest_bid = 0
    for name in bids:
        if bids[name] > highest_bid:
            highest_bidder = name
            highest_bid = bids[name]
    print(f"The winner is {highest_bidder} with a bid of ${bids[highest_bidder]}")

while continue_auction:
    name = input("What is you name?: ")
    bid = int(input("What's you bid?: $"))
    
    bidders[name] = bid

    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")

    if more_bidders != 'yes':
        continue_auction = False

    os.system('cls')

find_highest_bidder(bidders)