# Add comments before you do anything else.
#!/usr/bin/env python3
# Author: Darcy McLaughlin
# Date: 07/10/2026
# Purpose: use the main Function as entry point.
# Usage: ./lab4c.py

# Follow the instructions from readme.md.

# Fill in the required fields in the comment section.
# Write a function sum that takes two numbers as parameters and returns their sum.
# Write the main functions.
# In the main function get two numbers from user. Convert the user input to int.
# Call the sum function and pass the two numbers as argument.
# In the main() function, receive the sum in a variable, and print the sum for the user.
# Call the main function inside the condition:

def sum(num1, num2):
    """
    Returns the sum of two numbers.
    @param: num1 (int): The first number.
    @param: num2 (int): The second number.
    @return: int: The sum of num1 and num2.
    """
    return num1 + num2

def main():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = sum(num1, num2)
    print("The sum of", num1, "and", num2, "is:", result)

if __name__ == "__main__":
    main()
