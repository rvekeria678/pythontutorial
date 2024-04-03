from art import logo


# Add
def add(a, b):
    return a + b

# Subtract
def subtract(a, b):
    return a - b

# Multiply
def multiply(a, b):
    return a * b

# Divide
def divide(a, b):
    return a / b

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

print(logo)

def calculator():
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick and operation: ")
        num2 = float(input("What's the next number?: "))
        while operation_symbol == '/' and num2 == 0:
            print("Divide by Zero Err. Please pick a different Number!")
            num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input("Type 'y' to continue calculating with {answer}, type 'c' to clear, or type 'n' to quit:")
        if choice == 'y':
            num1 = answer
        elif choice == 'c':
            calculator()
        else:
            should_continue = False

calculator()