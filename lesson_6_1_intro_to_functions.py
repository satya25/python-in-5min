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
# File Name         :       lesson_6_1_intro_to_functions.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Oct 26, 2024
# version           :       1.0
# Release           :       R1
# Dependencies      :       NONE
# Installation      :       NONE
# Usage             :       python ./src/lesson_6_1_intro_to_functions.py
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
Lesson 6.1 - Introduction to Functions
---------------------------------------
This script introduces the concept of functions in Python.
We will explore how to define and call functions to organize and reuse code.
"""

# All imports whenever be applicable comes here.

def main():
    # Understanding functions with fun examples!
    
    # Defining a function
    def greet(name):
        """
        This function takes a name as an argument and prints a greeting.
        """
        print(f"Hello, {name}! Welcome to the world of Python functions.")

    # Calling the function
    greet("Alice")
    greet("Bob")

    """
    Important Points:
    - Functions are blocks of reusable code that perform a specific task.
    - Use the 'def' keyword to define a function, followed by the function name and parentheses.
    - Functions can take arguments (inputs) and return values (outputs).
    - Calling a function executes its code and can pass in arguments.
    - Functions help in organizing code, making it reusable and easier to understand.
    """

if __name__ == "__main__":
    main()


