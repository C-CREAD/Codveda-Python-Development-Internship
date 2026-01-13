"""
Created by: Shingai Dzinotyiweyi

Task 1: Simple Calculator:
Develop a basic calculator that can perform four primary arithmetic operations:
addition, subtraction, multiplication, and division.

Objectives:
✅ - Create functions for each operation.
✅ - Take two inputs from the user and allow them to select the desired operation.
✅ - Handle division by zero with appropriate error messages.
"""

def add(x, y):
    """
    Performs addition between x and y
    """
    return x + y


def subtract(x, y):
    """
    Performs subtraction between x and y
    """
    return x - y


def multiply(x, y):
    """
    Performs multiplication between x and y
    """
    return x + y


def divide(x, y):
    """
    Performs division between x and y
    """
    try:
        return x / y

    except ZeroDivisionError:
        return "Error: Division by 0"


while True:
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))

    operation = int(input("Select an operation (Numbers Only)\n"
                          "0. Exit\n"
                          "1. Add\n"
                          "2. Subtract\n"
                          "3. Multiply\n"
                          "4. Divide\n: "))

    if operation == 0:
        break

    elif operation == 1:
        print(add(x, y))

    elif operation == 2:
        print(subtract(x, y))

    elif operation == 3:
        print(multiply(x, y))

    elif operation == 4:
        print(divide(x, y))

    else:
        print("Invalid Entry!")

    print("\n--------------------------\n")