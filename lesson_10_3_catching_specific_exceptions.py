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
# File Name         :       lesson_10_3_catching_specific_exceptions.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Oct 26, 2024
# version           :       1.0
# Release           :       R1
# Dependencies      :       NONE
# Installation      :       NONE
# Usage             :       python ./src/lesson_10_3_catching_specific_exceptions.py
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
Lesson 10.3 - Catching Specific Exceptions
--------------------------------------------
This script demonstrates how to catch specific exceptions in Python using multiple except blocks.
We will explore different scenarios where specific exceptions need to be handled.
"""

# All imports whenever be applicable comes here.

def main():
    # Understanding how to catch specific exceptions with fun examples!
    
    # Example 1: Catching ZeroDivisionError
    try:
        result = 10 / 0
    except ZeroDivisionError as e:
        print(f"Error: {e}")

    # Example 2: Catching IndexError
    my_list = [1, 2, 3]
    try:
        element = my_list[5]
    except IndexError as e:
        print(f"Error: {e}")

    # Example 3: Catching ValueError
    try:
        number = int("hello")
    except ValueError as e:
        print(f"Error: {e}")

    # Example 4: Catching FileNotFoundError
    try:
        with open("non_existent_file.txt", "r") as file:
            content = file.read()
    except FileNotFoundError as e:
        print(f"Error: {e}")

    # Example 5: Catching multiple exceptions
    try:
        num = int("hello")
        result = 10 / 0
    except (ValueError, ZeroDivisionError) as e:
        print(f"Error: {e}")

    """
    Important Points:
    - Multiple except blocks can be used to catch specific exceptions.
    - The except block is used to handle specific exceptions and manage errors gracefully.
    - Catching specific exceptions helps in writing robust and error-resistant code in Python.
    - The try-except block can handle multiple exceptions by specifying a tuple of exception types.
    - Understanding how to catch specific exceptions is essential for effective error handling in Python.
    """

if __name__ == "__main__":
    main()


