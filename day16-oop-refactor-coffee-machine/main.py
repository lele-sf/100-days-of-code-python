from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


def coffee_machine():
    while True:
        options = menu.get_items()
        choice = input(f"What would you like? ({options}): ").lower()
        if choice == "off":
            break
        elif choice == "report":
            coffee_maker.report()
            money_machine.report()
        else:
            drink = menu.find_drink(choice)
            if coffee_maker.is_resource_sufficient(
                drink
            ) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)


def main():
    coffee_machine()


if __name__ == "__main__":
    main()
