# Coffee Machine Program

from menu import MENU, resources

def enough_resources(menu_item, resources):
    for resource in resources:
        if menu_item['ingredients'][resources] > resources[resource]:
            return False
    return True

def driver():
    coffee_machine_status = 'on'
    money = 0
    while coffee_machine_status == 'on':
        user_input = input("What would you like? (espresso/latte/cappuccino): ")

        if user_input == 'off':
            coffee_machine_status = 'off'
        elif user_input == 'report':
            print(f'Water: {resources['water']}ml')
            print(f'Milk: {resources['milk']}ml')
            print(f'Coffee: {resources['coffee']}g')
            print(f'Money: ${money}')
        elif user_input in MENU:
            if enough_resources(MENU[user_input], resources):
                # Process Payment
                quarters = input("How many quarters?: ")
                dimes = input("How many dimes?: ")
                nickles = input("How many nickles?: ")
                pennies = input("How many pennies?: ")

                total_payment = (quarters * 25 + dimes * 10 + nickles * 5 + pennies) / 100

                for resource in resources:
                    resources[resources] -= MENU[user_input]['ingredients'][resource]
        else:
            print("Invalid Command. Please Try Again.")



driver()