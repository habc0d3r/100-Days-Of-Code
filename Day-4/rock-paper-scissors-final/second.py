# Another way for rock paper scissors:
# -----------------------
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
game_images = [rock, paper, scissors]
lose = "You lose!"
won = "You won!"

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if player_choice == 0:
  print(game_images[0])
elif player_choice == 1:
  print(game_images[1])
else:
  print(game_images[2])


computer_choice = random.randint(0, 2)
print('Computer chose:')
if computer_choice == 0:
  print(game_images[0])
elif computer_choice == 1:
  print(game_images[1])
else:
  print(game_images[2])

if player_choice >= 3 or player_choice < 0:
  print("You typed an Invalid number. You lose!")
elif player_choice == 2 and computer_choice == 0:
  print(lose)
elif player_choice == 0 and computer_choice == 2:
  print(won)
elif player_choice == 0 and computer_choice == 1:
  print(lose)
elif player_choice == 1 and computer_choice == 2:
  print(lose)
elif player_choice == 1 and computer_choice == 0:
  print(won)
elif player_choice == 2 and computer_choice == 1:
  print(won)
elif computer_choice == player_choice:
  print("It's a draw!")
