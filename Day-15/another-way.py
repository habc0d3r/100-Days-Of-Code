from menu import MENU, resources


# Todo: Convert quarters, dimes, nickels, pennies to dollar
def convert_currency(q, d, n, p):
    cents = q*25 + d*10 + n*5 + p*1
    dollar = cents/100
    return dollar


# todo: based on user's choice of coffee subtract quantity of resources
def subtract_resource(x_coffee, items):
    remaining_resources = []
    for i in resources:
        resource = resources[i] - MENU[x_coffee][items][i]
        remaining_resources.append(resource)
    return remaining_resources


# Todo: Process coins
# Todo: Check transaction successful
def is_enough_money(x_coffee, items, price):
    if convert_currency(quarters, dimes, nickles, pennies) < MENU[x_coffee][price]:
        # todo: if total money is less than coffee cost :
        return "Sorry that's not enough money. Money refunded."
    else:
        # Todo: Check resources sufficient
        for i in items:
            if items[i] >= resources[i]:
                return f"Sorry! There is not enough {i}."
        # todo: based on coffee choice calculate changes and make coffee
        change = convert_currency(quarters, dimes, nickles, pennies) - MENU[x_coffee][price]
        return f"Here is {round(change, 2)} in change.\nHere is your {x_coffee} ☕️. Enjoy!"


# Repeatable code part:
is_machine_off = False
while not is_machine_off:
    # Todo: Ask What would user want?
    user_choice = input("What would you like? (espresso/latte/cappuccino):")

    if user_choice == "off":
        is_machine_ff = True
    # Todo: Ask how many coins in: quarters, dimes, nickels, pennies
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))


    convert_currency(quarters, dimes, nickles, pennies)
    print(is_enough_money(user_choice, 'ingredients', 'cost'))
    remaining = subtract_resource(user_choice, 'ingredients')


    # Todo: If user enter 'off' turn off the coffee machine
    # Todo: Print report

# money = 0
# if user_choice == 'report' and money != 0:
#     print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}")
# elif user_choice == 'report' and money == 0:
#     print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g")
