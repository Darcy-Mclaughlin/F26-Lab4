# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Darcy McLaughlin
# Date: 07/10/2026
# Purpose: Create the complete calculator function using default parameters and positional parameters
# Usage: ./lab4d.py

# Follow the instructions from readme.md.

from py_compile import main


def compute (num1, num2, operation):
    """
    Performs a calculation based on the specified operation.
    @param: num1 (int): The first number.
    @param: num2 (int): The second number.
    @param: operation (str): The operation to perform ("+", "-", "*", "/").
    @return: float: The result of the calculation.
    """
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 != 0 and num1 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero."
    else:
        return num1 + num2

def main():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ")
    result = compute(num1, num2, operation)
    print("The result of", num1, operation, num2, "is:", result)

if __name__ == "__main__":
    main()
