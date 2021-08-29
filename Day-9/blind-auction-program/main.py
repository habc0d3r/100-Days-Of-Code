from clear_screen import clear
from art import logo

print(logo)
print("Welcome to the secret auction program.")

bidding_record = {}

def auction():
  name = input("What is your name?: ")
  bid = int(input("What's your bids?: $"))
  bidding_record[name] = bid

auction()

isBidding = True
while isBidding:
  more_bidders = input("Are there any other bidders? Type 'y' for yes or 'n' for no.\n")
  if more_bidders == "y":
    clear()
    auction()
  else:
    isBidding = False

highest_bid = 0
for bidder in bidding_record:
  bid_amount = bidding_record[bidder]
  if bid_amount > highest_bid:
    highest_bid = bid_amount
    winner = bidder
print(f"The winner is {winner} with a bid of ${highest_bid}")


