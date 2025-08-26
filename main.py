from shape import logo
import os

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

calculate_dict = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}

def calculator():
    print(logo)
    first_number = int(input("What's the first number?: "))
    calculate_status = True

    while calculate_status:
        for key in calculate_dict:
            print(key)
        operation = input("Pick an operation: ")
        next_number = int(input("What's the next number?: "))
        calculation_function = calculate_dict.get(operation)
        result = calculation_function(first_number, next_number)
        print(f"{first_number} {operation} {next_number} = {result}")
        next_step = input(f"Type 'y' to continue calculating with {result},"
                          f" or type 'n' to start a new calculation: ").lower()
        if next_step == "y":
            first_number = result
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            calculator()
            return

calculator()
