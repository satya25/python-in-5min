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
# File Name         :       lesson_6_5_function_return_values.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Oct 26, 2024
# version           :       1.0
# Release           :       R1
# Dependencies      :       NONE
# Installation      :       NONE
# Usage             :       python ./src/lesson_6_5_function_return_values.py
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
Lesson 6.5 - Function Return Values
------------------------------------
This script demonstrates how to use return values in Python functions.
We will explore how functions can return values and how to handle them.
"""

# All imports whenever be applicable comes here.

def main():
    # Understanding function return values with fun examples!
    
    # Defining a function that returns a value
    def add_numbers(num1, num2):
        """
        This function takes two numbers as arguments and returns their sum.
        """
        return num1 + num2

    # Calling the function and storing the result
    result = add_numbers(5, 10)
    print("Sum of 5 and 10 is:", result)
    
    # Defining a function that returns multiple values
    def get_person_info():
        """
        This function returns a person's name and age.
        """
        name = "Alice"
        age = 30
        return name, age

    # Calling the function and handling multiple return values
    person_name, person_age = get_person_info()
    print("Person's name is:", person_name)
    print("Person's age is:", person_age)
    
    # Defining a function with conditional return values
    def check_even_or_odd(number):
        """
        This function checks if a number is even or odd and returns the result.
        """
        if number % 2 == 0:
            return "Even"
        else:
            return "Odd"

    # Calling the function and printing the result
    result = check_even_or_odd(42)
    print("The number 42 is:", result)

    """
    Important Points:
    - Functions can return values using the 'return' statement.
    - Return values can be captured and used in the calling code.
    - Functions can return multiple values as a tuple, which can be unpacked.
    - Conditional return values allow functions to return different results based on conditions.
    - Understanding function return values helps in writing flexible and reusable functions.
    """

if __name__ == "__main__":
    main()


