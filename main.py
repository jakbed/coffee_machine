from menu import menu, resources


def check_resources(drink):
    if menu[drink]['ingredients']['water'] > resources['water']:
        print("Sorry, there is not enough water")
        return False

    if resources['coffee'] < menu[drink]['ingredients']['coffee']:
        print("Sorry, there is not enough coffee")
        return False

    if 'milk' in menu[drink]['ingredients']:
        if menu[drink]['ingredients']['milk'] > resources['milk']:
            print("Sorry, there is not enough milk")
            return False

    return True


def insert_coins(drink):
    print("Please insert coins")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    result = 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies
    if result > menu[drink]['cost']:
        change = result - menu[drink]['cost']
        print(f"Here's ${change} in change")
    elif result == menu[drink]['cost']:
        print("No change.")
    else:
        print("not enough money ")
        return False


def update_resources(drink):
    resources['water'] -= menu[drink]['ingredients']['water']
    resources['coffee'] -= menu[drink]['ingredients']['coffee']
    if 'milk' in menu[drink]['ingredients']:
        resources['milk'] -= menu[drink]['ingredients']['milk']


def add_money(drink):
    resources['money'] += menu[drink]['cost']


def make_drink(coffee):
    if check_resources(coffee) == True:
        if insert_coins(coffee) is not False:
            update_resources(coffee)
            add_money(coffee)
            print(f"Enjoy your {coffee}!\n")

stop = False

while not stop:
    choose = input("What would you like to drink? (espresso, cappuccino, latte): ")

    if choose == "report":
        for i, x in resources.items():
            print(f"{i} -> {x}")

    elif choose == 'off':
        stop = True
    else:
        make_drink(choose)


