# TODO-1: Ask the user for input
from art import logo
print(logo)
name=input("What is your name? ")
bid=input("What is your bid?: $ ")


# TODO-2: Save data into dictionary {name: price}
bid_data={
    name:bid
}

# print(bid_data)
# TODO-3: Whether if new bids need to be added
continue_bidding=True
while continue_bidding==True:
    bid_check = input("Are there any other bidders? Type 'yes or 'no'.")
    bid_check = bid_check.upper()
    print(bid_check)

    if bid_check == "YES":
        print("\n" * 20)
        name = input("What is your name? ")
        bid = input("What is your bid?: $ ")
        bid_data[name] = bid
    # print(bid_data)
    else:
        continue_bidding=False
# TODO-4: Compare bids in dictionary
highest_bid=max(bid_data,key=bid_data.get)
# print(highest_bid)
# print(bid_data[highest_bid])

print(f"The winner is {highest_bid} with a bid of $ {bid_data[highest_bid]}")

