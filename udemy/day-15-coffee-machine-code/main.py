# Coffee Machine Program

from menu import MENU, resources

def enough_resources(menu_item, resources):
    for resource in resources:
        if resource in menu_item['ingredients']:
            if menu_item['ingredients'][resource] > resources[resource]:
                print(f"Sorry there is not enough {resource}.")
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
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${money}")
        elif user_input in MENU:
            if enough_resources(MENU[user_input], resources):
                # Process Payment
                quarters = int(input("How many quarters?: "))
                dimes = int(input("How many dimes?: "))
                nickles = int(input("How many nickles?: "))
                pennies = int(input("How many pennies?: "))

                total_payment = (quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01)

                if total_payment < MENU[user_input]['cost']:
                    print("Sorry that's not enough money. Money refunded")
                else:
                    for resource in resources:
                        if resource in MENU[user_input]['ingredients']:
                            resources[resource] -= MENU[user_input]['ingredients'][resource]
                    # Calculate Change
                    change = total_payment - MENU[user_input]['cost']
                    money += total_payment - change
                    if change > 0:
                        print(f"Here is ${change:.2f} dollars in change.")
                    # Finished Message
                    print(f"Here is your {user_input}. Enjoy!")
        else:
            print("Invalid Command. Please Try Again.")



driver()