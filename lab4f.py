# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Darcy McLaughlin
# Date: 11/10/2026
# Purpose: Practice variable number of arguments with *args
# Usage: ./lab4f.py

# Fill in the required fields in the comment section.
# Write a function called get_initials that returns the first letter from each provided name. It can handle a variable number of name inputs.
# The function uses *args to accept a variable number of name inputs.
# The function iterates through each name and extract the first letter.
# The function collects these first letters into a list.
# Finally, the function returns the list of initials.
# Given the names "Alice", "Bob", "Charlie", and "David", the function will return the list ['A', 'B', 'C', 'D'].
# Call the get_initials function from main function and receive the result in a list variable.
# Print the result in main.
# Run your script to test it.

def get_initials(*names):
    initials = []
    for name in names:
        initials.append(name[0])
    return initials

def main():
    result = get_initials("Alice", "Bob", "Charlie", "David")
    print(result)

if __name__ == "__main__":
    main()
