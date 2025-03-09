import os
from art import logo

other_bidders = "yes"
auction_detail = {"name": [], "bid": []}
bigger_bid = 0
winner = ""
print(logo)
print("Welcome to the secret auction program.")

while other_bidders.lower() == "yes":
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    auction_detail["name"].append(name)
    auction_detail["bid"].append(bid)
    while True:
        other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
        if other_bidders.lower() in ["yes", "no"]:
            break
        print("Please enter 'yes' or 'no'.")
    os.system("cls" if os.name == "nt" else "clear")
    if other_bidders.lower() == "no":
        for i, bid in enumerate(auction_detail["bid"]):
            if bid > bigger_bid:
                bigger_bid = bid
                winner = auction_detail["name"][i]
        print(f"The winner is {winner} with a bid of ${bigger_bid}.")
        break
