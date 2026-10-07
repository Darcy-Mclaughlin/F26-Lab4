# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Darcy McLaughlin
# Date: 07/10/2026
# Purpose: Create Some Complex Functions.
# Usage: ./lab4b.py

# TO DO 1: Add the docstring
# @Function definition: add definition here
# @param: write parameters here
# @return: write return value here
# TO DO 2: Create the function.
# TO DO 3: Call the function.

def even_numbers(num_list):
    """
    Returns a list of even numbers from the given list.
    @param: num_list (list): A list of integers to check.
    @return: list: A new list containing only the even numbers from the input list.
    """
    evenList = []
    for num in num_list:
        if num % 2 == 0:
            evenList.append(num)
    return evenList

list = [3, 7, 2, 8, 5, 10, 1, 4]
result = even_numbers(list)
print(result)

# Fill in the required fields in the comment section.
# write a function called even_numbers that takes a list as argument and returns a new list of all the even numbers from the list.
#If the passed list does not contain any even numbers, return an empty list.
#Call the function with a list of 8 integer values.
#Receive the result in a list variable and print the list variable.
#Run your script to test it.
