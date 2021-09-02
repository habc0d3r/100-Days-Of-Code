# generate a random number between 1 and 100
import random 
random_num = random.randint(1, 100)
print(random_num)

#take input for difficulty hard or easy
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

#if hard: attempts = 5 , if easy attempts = 10
if difficulty == "hard":
  attempts = 5
  #print how many guesses they have
  print(f"You have {attempts} attempts remaining to guess the number.")
elif difficulty == "easy":
  attempts = 10
  #print how many guesses they have
  print(f"You have {attempts} attempts remaining to guess the number.")

# take a number input 
guess = int(input("Make a guess: "))

# make a while loop to check if the guessed number and random number is same 
while attempts > 0:
  # check:
  # if guessed number is greater than the random number print "too high"
  if guess > random_num:
      print("Too high.\nGuess again.")
      # if guessed number is not equal to random number reduce attempts by 1
      attempts -= 1
  # if guessed number is lesser than the random number print "too low"
  elif guess < random_num:
      print("Too low.\nGuess again.")
      # if guessed number is not equal to random number reduce attempts by 1
      attempts -= 1
  #  if the guessed number is same as the random number
  elif guess == random_num:
    print(f"You got it! The answer was {random_num}.")
    attempts = 0
# if guessed number is not equal to random number reduce attempts by 1 and print how many guess attempts has left
