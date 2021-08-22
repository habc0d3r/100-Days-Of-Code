import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

# get the total number of items in the list
no_of_people = len(names)
# generating a random int between 0 and (no_of_people - 1)
random_choice = random.randint(0, no_of_people -1)
# accessing the bill payer by its index on the list
bill_payer = names[random_choice]
# bill_payer = random.choice(names)
print(f"{bill_payer} is going to buy the meal today!") 



