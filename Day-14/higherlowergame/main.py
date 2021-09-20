from art import logo, vs
from game_data import data
from clear_screen import clear
import random
def format_data(account):
    """format the account data into printable format"""
    account_name = account['name']
    account_description = account['description']
    account_country = account['country']
    return f"{account_name} , a {account_description} from {account_country}"

def check_answer(guess, a_followers, b_followers):
    """Take the user guess and follower counts and returns if they got it right."""
    if a_followers > b_followers:
        return guess == "a"
    return guess == "b"

# Display art
print(logo)
score = 0
# make the game repeatable 
continue_game = True
account_b = random.choice(data)
while continue_game:
    # generate random account from the list
    # make previous B account become account A next time 
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    # Ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # check if user is correct
    ## get followers count of each account
    a_follower_count = account_a['follower_count']
    b_follower_count = account_b['follower_count']

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # clear the screen
    clear()
    print(logo)
    # give user feedback on their guess
    # keep score
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        continue_game = False
        print(f"Sorry, that's wrong! Final Score: {score}")
