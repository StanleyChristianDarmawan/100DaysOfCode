import os
from art import logo

clear = lambda: os.system('cls')

print(logo)

bidders_dictionary = {}

continueProgram = True
while continueProgram:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bidders_dictionary[name] = bid
    anyOtherBidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if anyOtherBidders == "yes":
        clear()
    else:
        continueProgram = False
        highestBid = 0
        highestBidPerson = ""
        for name in bidders_dictionary:
            if bidders_dictionary[name] > highestBid:
                highestBid = bidders_dictionary[name]
                highestBidPerson = name
            
        print(f"The winner is {highestBidPerson} with a bid of {bidders_dictionary[highestBidPerson]}")


