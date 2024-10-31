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
# File Name         :       lesson_6_8_higher_order_functions.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Oct 26, 2024
# version           :       1.0
# Release           :       R1
# Dependencies      :       NONE
# Installation      :       NONE
# Usage             :       python ./src/lesson_6_8_higher_order_functions.py
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
Lesson 6.8 - Higher-Order Functions
-------------------------------------
This script introduces the concept of higher-order functions in Python.
We will explore how to define and use functions that accept other functions as arguments or return functions.
"""

# All imports whenever be applicable comes here.

def main():
    # Understanding higher-order functions with fun examples!
    
    # Defining a higher-order function that takes a function as an argument
    def apply_operation(x, y, operation):
        """
        This function takes two numbers and a function (operation) as arguments and returns the result of applying the operation.
        """
        return operation(x, y)

    # Defining some basic operations as lambda functions
    add = lambda x, y: x + y
    multiply = lambda x, y: x * y

    # Calling the higher-order function with different operations
    result_add = apply_operation(5, 10, add)
    print("Result of addition:", result_add)

    result_multiply = apply_operation(5, 10, multiply)
    print("Result of multiplication:", result_multiply)
    
    # Defining a higher-order function that returns a function
    def create_multiplier(factor):
        """
        This function takes a factor and returns a lambda function that multiplies its argument by the factor.
        """
        return lambda x: x * factor

    # Creating multiplier functions using the higher-order function
    doubler = create_multiplier(2)
    tripler = create_multiplier(3)

    # Using the multiplier functions
    print("Double of 5:", doubler(5))
    print("Triple of 5:", tripler(5))

    """
    Important Points:
    - Higher-order functions are functions that can accept other functions as arguments or return functions.
    - Using higher-order functions allows for more abstract and flexible code.
    - Lambda functions are often used with higher-order functions for concise and functional code.
    - Understanding higher-order functions helps in writing more powerful and reusable code.
    """

if __name__ == "__main__":
    main()


