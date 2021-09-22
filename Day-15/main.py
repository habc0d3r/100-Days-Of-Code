# from menu import MENU, resources

# Todo: Ask what would user like
user_choice = input("What would you like? (espresso/latte/cappuccino):")
# Todo: Ask how many coins in: quarters, dimes, nickels, pennies
print("Please insert coins.")
quarters = int(input("How many quarters?: "))
dimes = int(input("How many dimes?: "))
nickles = int(input("How many nickles?: "))
pennies = int(input("How many pennies?: "))


# Todo: Convert quarters, dimes, nickels, pennies to dollar
def convert_currency(q, d, n, p):
    cents = q*25 + d*10 + n*5 + p*1
    dollar = cents/100
    return dollar


print(convert_currency(q=quarters, d=dimes, n=nickles, p=pennies))


# todo: based on user's choice of coffee subtract quantity of resources
def resource_calc(coffee):
    # todo: based on users choice access the items used for make the coffee
    if user_choice == coffee:
        # subtract from resources
        pass


# Todo: Check resources sufficient?
# Todo: Process coins
# todo: based on coffee choice calculate changes and return
def change():
    pass


# Todo: Check transaction successful
# Todo: Make Coffee
# Todo: Ask What would user want?
# Todo: If user enter 'off' turn off the coffee machine
# Todo: Print report
# water = resources['water']
# milk = resources['milk']
# coffee = resources['coffee']
# if user_choice == 'report':
#     print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g")
