############### Blackjack Project #####################
from art import logo
from clear_screen import clear
import random

def deal_card():
  """Returns a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(card_list):
  """It takes list of cards as an argument and return the score calculated from the cards"""
  score = sum(card_list)

  if score == 21 and len(card_list) == 2:
      return 0

  if 11 in card_list and score > 21:
    card_list.remove(11)
    card_list.append(1)

  return score

def compare(user_score, computer_score):
    if user_score == computer_score:
      return "Draw 🙃"
    elif computer_score == 0:
      return "Lose, opponent has Blackjack 🤦"
    elif user_score == 0:
      return "Win with a Black Jack 😁"
    elif user_score > 21:
      return "You went over. You lose 😅"
    elif computer_score > 21:
      return "Opponent went over. You win 😂"
    elif user_score > computer_score:
      return "You win 😄"
    else:
      return "You lose 😵"

def play_game():
  print(logo)

  user_cards = []
  computer_cards = []
  isGame_over = False

  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  while not isGame_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      isGame_over = True
    else:
      user_should_deal = input("Type 'y' to get another card or 'n' to pass: ")
      if user_should_deal == "y":
        user_cards.append(deal_card())
      else:
        isGame_over = True

  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"Your final hand: {user_cards}, final score: {user_score}")
  print(f"Computer's final hand: {computer_cards}, final scoreL: {computer_score}")
  print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play_game()