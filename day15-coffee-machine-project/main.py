MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# Todo: print report
def print_report(res, money):
    return print(
        f'Water: {res["water"]}ml\nMilk: {res["milk"]}ml\nCoffee: {res["coffee"]}g'
        f"\nMoney: ${money:.2f}\n"
    )


# Todo: check if resources are sufficient
def check_resources(res, coffee_choice):
    for ingredient in MENU[coffee_choice]["ingredients"]:
        if res[ingredient] < MENU[coffee_choice]["ingredients"][ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
        return True


# Todo: process coins
def process_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.1
    nickels = int(input("How many nickels?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01

    total = quarters + dimes + nickels + pennies
    return total


# Todo: check if transaction was successful
def check_transaction(total_money, coffee_cost):
    if total_money < coffee_cost:
        print("Sorry, that's not enough money. Money refunded.")
        return False, 0
    change = round(total_money - coffee_cost, 2)
    if change > 0:
        print(f"Here is ${change} in change.")
    return True, coffee_cost


# Todo: make coffee
def make_coffee(res, drink):
    for ingredient, amount in MENU[drink]["ingredients"].items():
        res[ingredient] -= amount
    print(f"Enjoy your {drink}!")


def coffee_machine():
    money = 0
    while True:
        # Todo: prompt user by asking “What would you like? (espresso/latte/cappuccino):”
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        # Todo: Turn off the Coffee Machine by entering “off” to the prompt.
        if choice == "off":
            break
        elif choice == "report":
            print_report(resources, money)
        elif choice in MENU:
            if check_resources(resources, choice):
                total_inserted = process_coins()
                success, earned = check_transaction(
                    total_inserted, MENU[choice]["cost"]
                )
                if success:
                    money += earned
                    make_coffee(resources, choice)
        else:
            print("Invalid choice. Please select a valid option.")


def main():
    coffee_machine()


if __name__ == "__main__":
    main()
