from coffee_menu_and_resource import MENU, resources


def check_resources(items):
    for item in items:
        if items[item] > resources[item]:
            print(f"Sorry there is not enough {item}. "
                  f"Please try another coffee or"
                  "You may turn off the machine by typing 'off'")
    return True


def make_coffee(coffee, items):
    for item in items:
        resources[item] -= items[item]
    print(f"Here's your {coffee}, Enjoy!!", end=' ')


def take_money():
    rupee = int(input("How many Rupees? "))
    paise = int(input("How many Paise? ")) * 0.01
    return rupee + paise


def return_change(money_taken, drink_cost):
    give = money_taken - drink_cost
    print(f"and here's your change ₹{give}")


money = 0
while True:
    action = input("What you like to have (espresso/latte/cappuccino): ")
    action = action.lower()
    if action == 'off':
        break

    elif action == 'report':
        print(f'Water available is {resources["water"]}ml')
        print(f'Milk available is {resources["milk"]}ml')
        print(f'Coffee available is {resources["coffee"]}gms')
        print(f'Money is ₹{money}')

    elif action in MENU:
        drink = MENU[action]
        if check_resources(drink["ingredients"]):
            cash = take_money()
            if cash < drink["cost"]:
                print("Sorry, that's not enough money. Money refunded..")
            else:
                money += cash
                make_coffee(action, drink["ingredients"])
                return_change(cash, drink["cost"])

    else:
        print("Please enter a valid input")
