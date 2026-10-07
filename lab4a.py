# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Darcy McLaughlin 
# Date: 07/10/2026
# Purpose: Create Simple Functions.
# Usage: ./lab4a.py

# TO DO 1: Add the docstring
# @Function definition: add definition here
# @param: write parameters here
# @return: write return value here 

# TO DO 2: define the function with name `is_even`.

# TO DO 3: Call the function `is_even`.

def is_even(num):
    """
    Check if a number is even.
    @param: num (int): The number to check.
    @return: bool: True if the number is even, False otherwise.
    """
    answer = []
    for i in range(len(num)):
        if num[i] % 2 == 0:
            answer.append(True)
        else:
            answer.append(False)

    return answer

num = [4, 1, 6, 5, 10]
print(is_even(num))