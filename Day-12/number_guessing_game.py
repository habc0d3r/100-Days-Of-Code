#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random 
random_number = random.randint(1, 100)

print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
print(random_number)

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == "hard":
  attempts = 5
elif difficulty == "easy":
  attempts = 10
guess = int(input("Make a guess: "))

def check_number():
  if guess > random_number:
    print("Too high.\nGuess again.")
  elif guess < random_number:
    print("Too low.\nGuess again.")
#   elif guess == random_number:
#     print(f"You got it! The answer was {random_number}.")

should_continue = True
while should_continue:
    if guess != random_number:
        attempts -= 1
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
    elif guess == random_number:
        print(f"You got it! The answer was {random_number}.")
        should_continue = False

if attempts == 0:
    print("You've run out of guesses, you lose.")
    should_continue = False

