# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

from art import logo

print(logo)
input("Press Enter to continue...")

continue_flag = True
all_bids = {}
maxbid = 0
maxbidname = ""

while continue_flag:
    name = input("Enter bidder's name: ")
    bid = int(input("Enter bidder's bid: "))
    if bid > maxbid:
        maxbid = bid
        maxbidname = name
    all_bids[name] = bid

    if input("Are there any other bidders? Type 'yes or 'no'.") == 'no':
        continue_flag = False
    else: print("\n"*50)

print(f"The name of the highest bidder is {maxbidname} with {maxbid}$")
