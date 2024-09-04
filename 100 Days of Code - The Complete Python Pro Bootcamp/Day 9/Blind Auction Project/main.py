# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

from art import logo
print(logo)
bidders = {}
print(bidders)
another_bidder = True

def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for high_bidder in bidding_dictionary:
        price = bidding_dictionary[high_bidder]
        if price > highest_bid:
            highest_bid = price
            winner = high_bidder

    print(f"The highest bidder is: {winner} with a bid of {highest_bid}")


while another_bidder:
    name = input("Please type in your name\n")
    bid = int(input("Please type in your bidding price\n"))
    bidders[name] = bid
    if input("Is there another bidder? Type 'yes or 'no'.\n") == "yes":
        another_bidder = True
        print("\n" * 20)
    else:
        another_bidder = False
        print(bidders)
        find_highest_bidder(bidders)



