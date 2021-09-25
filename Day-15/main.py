from menu import MENU, resources, profit


def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are not enough"""
    for i in order_ingredients:
        if order_ingredients[i] >= resources[i]:
            print(f"Sorry there is not enough {i}.")
            return False
    return True


def process_money():
    """Returns the total money calculated from coins inserted """
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = quarters*25 + dimes*10 + nickles*5 + pennies*1
    total = total/100
    return total


def is_transaction_successful(money_received, coffee_cost):
    """Return True when the payment is accepted, or False if money
    is insufficient """
    if money_received >= coffee_cost:
        change = round(money_received - coffee_cost, 2)
        print(f"Here is {round(change, 2)} in change.")
        global profit
        profit += coffee_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(coffee_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {coffee_name} ☕️. Enjoy!")


is_machine_on = True

while is_machine_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino):")
    if user_choice == "off":
        is_machine_on = False
    elif user_choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        coffee_choice = MENU[user_choice]
        if is_resource_sufficient(coffee_choice['ingredients']):
            payment = process_money()
            if is_transaction_successful(payment, coffee_choice['cost']):
                make_coffee(user_choice, coffee_choice['ingredients'])
