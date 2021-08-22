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

# code for player
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if player_choice >= 3 or player_choice < 0:
  print("You typed an Invalid number. You lose!")
else:
  print(game_images[player_choice])

  # code for computer
  computer_choice = random.randint(0, 2)
  print('Computer chose:')
  print(game_images[computer_choice])

  # game logic/rules
  if player_choice == 2 and computer_choice == 0:
    print(lose)
  elif player_choice == 0 and computer_choice == 2:
    print(won)
  elif player_choice > computer_choice:
    print(won)
  elif player_choice < computer_choice:
    print(lose)
  elif computer_choice == player_choice:
    print("It's a draw!")
