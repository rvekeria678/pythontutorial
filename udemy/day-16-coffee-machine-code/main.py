from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine



def driver():
    machine_status = 'on'
    coffee_machine_menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()

    while machine_status == 'on':
        user_input = input(f"What would you like? ({coffee_machine_menu.get_items()}): ")

        if user_input == 'off':
            machine_status = 'off'
        elif user_input == 'report':
            coffee_maker.report()
            money_machine.report()
        else:
            drink = coffee_machine_menu.find_drink(user_input)
            if drink != None:
                if coffee_maker.is_resource_sufficient(drink):
                    if money_machine.make_payment(drink.cost):
                        coffee_maker.make_coffee(drink)

driver()