#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" 
This file is part of aialchemyhub_in 
(https://github.com/satya25/aialchemyhub_in). 
aialchemyhub_in is free software repository: 
You can redistribute it and/or modify it under 
the terms of the MIT License. 
aialchemyhub_in is distributed in the hope that it will be useful, 
but WITHOUT ANY WARRANTY; without even the implied warranty of 
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the 
MIT License for more details. 
You should have received a copy of the MIT License along with 
aialchemyhub_in.  If not, see <https://opensource.org/licenses/MIT>.
"""

# ----------------------------------------------------------------------------
# File Name         :       lesson_6_9_mini_project_simple_calculator.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Oct 26, 2024
# version           :       1.0
# Release           :       R1
# Dependencies      :       NONE
# Installation      :       NONE
# Usage             :       python ./src/lesson_6_9_mini_project_simple_calculator.py
# ----------------------------------------------------------------------------
# Credits and Acknowledgements
# - Special thanks to the Python community for their excellent work:
#   https://www.python.org/community/
# - The APIs used in this script is documented here:
#   https://docs.python.org/3/
# - Code Snippet(s) adapted from    :   -- NOT Applicable --
# - Dataset(s) sourced  from        :   -- NOT Applicable --
# - Inspiration drawn from          :   -- NOT Applicable --
# 
# Thank you to the creators and maintainers of these resources!
# ----------------------------------------------------------------------------
# - Content Removal Requests
#   If you are the owner or creator of any content used in this script and
#   would like it to be removed, please contact me at:  spnigam25@yahoo.com
#   I will promptly remove the content upon request.
# ----------------------------------------------------------------------------

"""
Lesson 6.9 - Mini Project: Simple Calculator
---------------------------------------------
This mini project demonstrates the use of functions in Python by creating a simple calculator.
We will implement functions for addition, subtraction, multiplication, and division.
"""

# All imports whenever be applicable comes here.

def main():
    # Welcome to the Simple Calculator!
    print("Welcome to the Simple Calculator!")

    # Defining calculator functions
    def add(x, y):
        """
        This function takes two numbers and returns their sum.
        """
        return x + y

    def subtract(x, y):
        """
        This function takes two numbers and returns their difference.
        """
        return x - y

    def multiply(x, y):
        """
        This function takes two numbers and returns their product.
        """
        return x * y

    def divide(x, y):
        """
        This function takes two numbers and returns their division result.
        """
        if y != 0:
            return x / y
        else:
            return "Error! Division by zero."

    # Displaying the calculator menu
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    # Taking user input for operation
    choice = input("Enter choice (1/2/3/4): ")

    # Taking user input for numbers
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return

    # Performing the selected operation
    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", subtract(num1, num2))
    elif choice == '3':
        print("Result:", multiply(num1, num2))
    elif choice == '4':
        print("Result:", divide(num1, num2))
    else:
        print("Invalid choice.")

    """
    Important Points:
    - This mini project demonstrates the use of functions to implement a simple calculator.
    - Functions for addition, subtraction, multiplication, and division are defined and called based on user input.
    - The calculator handles basic arithmetic operations and provides error handling for division by zero.
    - Interactive projects like this simple calculator make learning Python fun and engaging.
    """

if __name__ == "__main__":
    main()

