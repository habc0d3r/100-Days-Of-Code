from clear_screen import clear
from art import logo

print(logo)
print("Welcome to the secret auction program.")

bidding_record = {}

def max_bid(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

bidding_stopped = False
while not bidding_stopped:
  name = input("What is your name?: ")
  bid = int(input("What's your bids?: $"))
  bidding_record[name] = bid
  more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  if more_bidders == "yes":
    clear()
  else:
    bidding_stopped = True
    max_bid(bidding_record)



