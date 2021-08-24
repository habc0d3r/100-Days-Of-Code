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

bidding_condition = True
while bidding_condition:
  more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  if more_bidders == "yes":
    clear()
    auction()
  else:
    bidding_condition = False

highest_bid = 0
for bidder in bidding_record:
  bid_amount = bidding_record[bidder]
  if bid_amount > highest_bid:
    highest_bid = bid_amount
    winner = bidder
print(f"The winner is {winner} with a bid of ${highest_bid}")

