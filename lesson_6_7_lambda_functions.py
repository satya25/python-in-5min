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
# File Name         :       lesson_6_7_lambda_functions.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Oct 26, 2024
# version           :       1.0
# Release           :       R1
# Dependencies      :       NONE
# Installation      :       NONE
# Usage             :       python ./src/lesson_6_7_lambda_functions.py
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
Lesson 6.7 - Lambda Functions
------------------------------
This script introduces the concept of lambda functions in Python.
We will explore how to define and use anonymous functions using the lambda keyword.
"""

# All imports whenever be applicable comes here.

def main():
    # Understanding lambda functions with fun examples!
    
    # Defining a simple lambda function for addition
    add = lambda x, y: x + y

    # Calling the lambda function and printing the result
    result = add(5, 10)
    print("Sum of 5 and 10 using lambda function is:", result)
    
    # Using a lambda function inside a higher-order function (e.g., map)
    numbers = [1, 2, 3, 4, 5]
    squared_numbers = list(map(lambda x: x**2, numbers))
    print("Squared numbers:", squared_numbers)
    
    # Using a lambda function for sorting a list of tuples
    people = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
    sorted_people = sorted(people, key=lambda person: person[1])
    print("People sorted by age:", sorted_people)
    
    """
    Important Points:
    - Lambda functions are anonymous functions defined using the lambda keyword.
    - Lambda functions can take any number of arguments but can only have one expression.
    - Lambda functions are useful for short, simple functions that are used temporarily.
    - Lambda functions are often used in higher-order functions like map(), filter(), and sorted().
    - Understanding lambda functions helps in writing concise and functional code.
    """

if __name__ == "__main__":
    main()


