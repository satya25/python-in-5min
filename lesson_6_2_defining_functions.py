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
# File Name         :       lesson_6_2_defining_functions.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Oct 26, 2024
# version           :       1.0
# Release           :       R1
# Dependencies      :       NONE
# Installation      :       NONE
# Usage             :       python ./src/lesson_6_2_defining_functions.py
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
Lesson 6.2 - Defining Functions
--------------------------------
This script demonstrates how to define functions in Python.
We will explore function definitions, arguments, return values, and documentation.
"""

# All imports whenever be applicable comes here.

def main():
    # Understanding function definitions with fun examples!
    
    # Defining a function with a single argument
    def greet(name):
        """
        This function takes a name as an argument and prints a greeting.
        """
        print(f"Hello, {name}! Nice to meet you.")

    # Calling the function
    greet("Alice")
    greet("Bob")
    
    # Defining a function with multiple arguments
    def add_numbers(num1, num2):
        """
        This function takes two numbers as arguments and returns their sum.
        """
        return num1 + num2

    # Calling the function and storing the result
    result = add_numbers(5, 10)
    print("Sum of 5 and 10 is:", result)
    
    # Defining a function with default arguments
    def introduce(name, age=30):
        """
        This function takes a name and an optional age as arguments and prints an introduction.
        """
        print(f"My name is {name} and I am {age} years old.")

    # Calling the function with and without the default argument
    introduce("Charlie")
    introduce("Dana", 25)
    
    """
    Important Points:
    - Functions are defined using the 'def' keyword, followed by the function name and parentheses.
    - Functions can have parameters (arguments) that serve as inputs.
    - Functions can return a value using the 'return' statement.
    - Functions can have default arguments, which are used if no value is provided.
    - Functions help in organizing code, making it reusable and easier to understand.
    """

if __name__ == "__main__":
    main()


