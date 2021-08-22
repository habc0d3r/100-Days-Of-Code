#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

# print("Welcome to the tip calculator!")
# bill = input("What is the total bill? $")
# bill_as_float = float(bill)
# tip_percent = input("What percentage tip would you like to give? 10, 12, or 15? ")
# people = input("How many people to split the bill? ")
# tip = float(tip_percent)/100 * bill_as_float
# final_bill = bill_as_float + tip
# per_person_bill = round(final_bill/int(people), 2)
# result = f"Each person should pay: ${per_person_bill}"
# print(result)

#Another way

print("Welcome to the tip calculator!")
bill = float(input("What is the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

tip_as_percent = tip/100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill/people
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)
result = f"Each person should pay: ${final_amount}"
print(result)