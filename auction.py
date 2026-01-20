import art
print(art.logo)



end_of_bids = False
user_list = {}

while end_of_bids == False:
    user = input("What is your name?: ").lower()
    bid_amount = int(input("What is your bid?: $"))

    while True:

        others = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
        if others in ["yes", "no"]:
            break
    if others == "yes":
        user_list[user] = bid_amount
        print("\n" * 100)
        continue
    elif others == "no":
        user_list[user] = bid_amount
        highest_bidder = max(user_list, key=user_list.get)
        highest_bid = user_list[highest_bidder]

        print(f"The user with the winning bid is: {highest_bidder} with a bid of {highest_bid}")
        end_of_bids = True
