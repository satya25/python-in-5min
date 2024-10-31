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
# File Name         :       lesson_10_6_raising_exceptions.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Oct 26, 2024
# version           :       1.0
# Release           :       R1
# Dependencies      :       NONE
# Installation      :       NONE
# Usage             :       python ./src/lesson_10_6_raising_exceptions.py
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
Lesson 10.6 - Raising Exceptions
-----------------------------------
This script demonstrates how to raise exceptions in Python.
We will explore how to use the raise statement to trigger exceptions intentionally.
"""

# All imports whenever be applicable comes here.

def main():
    # Understanding how to raise exceptions with fun examples!
    
    # Example 1: Raising a ValueError
    def check_positive(number):
        if number <= 0:
            raise ValueError("Number must be positive")
        return number

    try:
        result = check_positive(-10)
    except ValueError as e:
        print(f"Error: {e}")

    # Example 2: Raising a TypeError
    def check_string(value):
        if not isinstance(value, str):
            raise TypeError("Value must be a string")
        return value

    try:
        result = check_string(123)
    except TypeError as e:
        print(f"Error: {e}")

    # Example 3: Raising a custom exception
    class CustomException(Exception):
        pass

    def raise_custom_exception():
        raise CustomException("This is a custom exception")

    try:
        raise_custom_exception()
    except CustomException as e:
        print(f"Error: {e}")

    """
    Important Points:
    - The raise statement is used to trigger exceptions intentionally in Python.
    - Common exceptions like ValueError and TypeError can be raised to indicate specific errors.
    - Custom exceptions can be defined by creating new exception classes that inherit from the base Exception class.
    - Raising exceptions helps in enforcing constraints and managing errors in a controlled manner.
    - Understanding how to raise exceptions is essential for writing robust and error-resistant code in Python.
    """

if __name__ == "__main__":
    main()


