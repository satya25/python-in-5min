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
# File Name         :       lesson_10_8_exception_handling_best_practices.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Oct 26, 2024
# version           :       1.0
# Release           :       R1
# Dependencies      :       NONE
# Installation      :       NONE
# Usage             :       python ./src/lesson_10_8_exception_handling_best_practices.py
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
Lesson 10.8 - Exception Handling Best Practices
-------------------------------------------------
This script demonstrates best practices for exception handling in Python.
We will explore techniques for writing robust and maintainable exception handling code.
"""

# All imports whenever be applicable comes here.

def main():
    # Understanding exception handling best practices with fun examples!
    
    # Example 1: Use specific exceptions
    try:
        result = 10 / 0
    except ZeroDivisionError as e:
        print(f"ZeroDivisionError: {e}")
    except Exception as e:
        print(f"General Exception: {e}")

    # Example 2: Avoid using bare except
    try:
        result = 10 / 0
    except ZeroDivisionError as e:
        print(f"ZeroDivisionError: {e}")
    except Exception as e:
        print(f"General Exception: {e}")

    # Example 3: Provide meaningful error messages
    try:
        num = int("hello")
    except ValueError as e:
        print(f"Error: Could not convert string to integer. Details: {e}")

    # Example 4: Use the finally block for cleanup
    try:
        file = open("example_best_practices.txt", "w")
        file.write("Writing to a file using best practices.\n")
    except IOError as e:
        print(f"IOError: {e}")
    finally:
        file.close()
        print("File closed using the finally block.")

    # Example 5: Use the else clause for code that should run when no exceptions occur
    try:
        result = 10 / 2
    except ZeroDivisionError as e:
        print(f"ZeroDivisionError: {e}")
    else:
        print(f"Result: {result}")

    # Example 6: Raise exceptions when needed
    def check_positive(number):
        if number <= 0:
            raise ValueError("Number must be positive")
        return number

    try:
        result = check_positive(-10)
    except ValueError as e:
        print(f"Error: {e}")

    """
    Important Points:
    - Use specific exceptions to handle known error conditions explicitly.
    - Avoid using bare except blocks; always specify the exception type.
    - Provide meaningful error messages to help with debugging and understanding the error.
    - Use the finally block to ensure that cleanup code is always executed.
    - Use the else clause for code that should run when no exceptions occur.
    - Raise exceptions intentionally to enforce constraints and handle errors.
    - Following these best practices helps in writing robust and maintainable exception handling code in Python.
    """

if __name__ == "__main__":
    main()



