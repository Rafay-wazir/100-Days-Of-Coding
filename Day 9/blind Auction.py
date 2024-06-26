from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo

print(logo)

bids = {}

bidding_finished = False


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The Winner Is {winner} With A Bid Of ${highest_bid}")


while not bidding_finished:
    name = input("What's Your Name?: ")
    price = int(input("What's Your Bid?: $"))
    bids[name] = price
    print(bids)
    should_continue = input("Are There Any Other Bidders? Type 'yes'or no. ")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        clear()
