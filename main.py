from replit import clear
from logo import logo

print(logo)

auction = {"start":0}
auction_end = False

while not auction_end:
    name = str(input(">>What is your name ? : "))
    bid = int(input(">>What's your bid? :$ "))
    check_price = list(auction.values())[-1]

    while True:
        if check_price < bid:
            auction[name] = bid
            break
        print("Bid price is less than last value.")
        offerNewPrice = str(input("Offer a new price Type 'yes' or 'no'\n"))

        if offerNewPrice == 'yes':
            bid = int(input(">>What's your bid? :$ "))
        else:
            print(f"Sir {name} cancel bid")
            break

    other_bid = str(input(">>Are there any other bidders? Type 'yes' or 'no'\n"))
    auction_end = True if other_bid == 'no' else False
    clear()

clear()
winner_name = list(auction.keys())[-1]
top_bid = list(auction.values())[-1]
print(f"The winner is {winner_name} with a bid of ${top_bid}")