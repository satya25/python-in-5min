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
# File Name         :       lesson_10_7_handling_multiple_exceptions.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Oct 26, 2024
# version           :       1.0
# Release           :       R1
# Dependencies      :       NONE
# Installation      :       NONE
# Usage             :       python ./src/lesson_10_7_handling_multiple_exceptions.py
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
Lesson 10.7 - Handling Multiple Exceptions
--------------------------------------------
This script demonstrates how to handle multiple exceptions in Python.
We will explore different scenarios where multiple exceptions may occur and how to manage them effectively.
"""

# All imports whenever be applicable comes here.

def main():
    # Understanding how to handle multiple exceptions with fun examples!
    
    # Example 1: Handling multiple exceptions using multiple except blocks
    try:
        result = 10 / 0
    except ZeroDivisionError as e:
        print(f"ZeroDivisionError: {e}")
    except ValueError as e:
        print(f"ValueError: {e}")

    # Example 2: Handling multiple exceptions using a single except block with a tuple
    try:
        num = int("hello")
        result = 10 / 0
    except (ValueError, ZeroDivisionError) as e:
        print(f"Error: {e}")

    # Example 3: Handling multiple exceptions with specific error messages
    try:
        num = int("hello")
    except ValueError:
        print("Error: Could not convert string to integer.")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

    # Example 4: Handling multiple exceptions with a single except block
    try:
        with open("non_existent_file.txt", "r") as file:
            content = file.read()
    except (FileNotFoundError, IOError) as e:
        print(f"Error: {e}")

    """
    Important Points:
    - Multiple exceptions can be handled using multiple except blocks or a single except block with a tuple.
    - Handling multiple exceptions helps in managing different types of errors effectively.
    - The except block can catch specific exceptions and provide appropriate error messages.
    - Using a single except block with a tuple allows handling multiple exceptions in a concise manner.
    - Understanding how to handle multiple exceptions is essential for writing robust and error-resistant code in Python.
    """

if __name__ == "__main__":
    main()


