from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# function to check user's guess is right or wrong
def check_answer(guess, random_num, turns):
  """Checks answer against guess. Returns the number of turns remaining."""
  if guess > random_num:
    print("Too high.")
    return turns - 1
  elif guess < random_num:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {random_num}.")
# Make function to set difficulty
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS
def game():
  print(logo)
  # Choosing a random number between 1 and 100
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  random_num = randint(1, 100)

  turns = set_difficulty()
  # repeat the guessing functionality if they get it wrong
  guess = 0
  while guess != random_num:
    print(f"You have {turns} attempts remaining to guess the number.")
    # let the user guess the number
    guess = int(input("Make a guess: "))
    turns = check_answer(guess, random_num, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return #empty return exit the function
    elif guess != random_num:
      print("Guess again.")
# track the number of turns and reduce by 1 if they gett it wrong

game()