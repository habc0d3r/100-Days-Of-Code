age = input("What is your current age?")

age_as_int = int(age)
# end_age = 90
# days = 365
# weeks = 52
# months = 12
# days_left = end_age*days - age_as_int*days
# weeks_left = end_age*weeks - age_as_int*weeks
# months_left = end_age*months - age_as_int*months
years_left = 90 - age_as_int
days_left = years_left * 365
weeks_left = years_left * 52
months_left = years_left * 12

message = f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left."
print(message)