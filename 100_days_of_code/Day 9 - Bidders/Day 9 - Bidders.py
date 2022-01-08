import art
#HINT: You can call clear() to clear the output in the console.
bidders = {}
def new_bidder(key,value):
    # information = {key:value}
    # bidders.append(information)
    bidders[key] = value
    print(bidders)


def calculation():
    largest_bidder = ""
    largest_bid = 0
    for key in bidders:
        if bidders[key] > largest_bid:
            largest_bidder = key
            largest_bid = bidders[key]
            largest_bid = 0
            largest_bidder = ""
        if bidders[key] == largest_bid:
            print(f"{largest_bidder} and {key} have to rebid." )
    print(f"The largest bidder is {largest_bidder} bidding at {largest_bid}.")
        

more_users = "Yes"
while more_users == "Yes":
    print(art.logo)
    print("Welcome to the Auction!")
    bidder_key = input("What is your name? ")
    bidder_value = int(input("How much will you be bidding today? "))
    new_bidder(bidder_key,bidder_value)
    more_users = input("Are there anymore bidders? ")

calculation()
