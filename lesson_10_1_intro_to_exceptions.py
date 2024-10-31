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
# File Name         :       lesson_10_1_intro_to_exceptions.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Oct 26, 2024
# version           :       1.0
# Release           :       R1
# Dependencies      :       NONE
# Installation      :       NONE
# Usage             :       python ./src/lesson_10_1_intro_to_exceptions.py
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
Lesson 10.1 - Introduction to Exceptions
------------------------------------------
This script introduces the concept of exceptions in Python.
We will explore what exceptions are, why they occur, and how to handle them.
"""

# All imports whenever be applicable comes here.

def main():
    # Understanding exceptions with fun examples!
    
    # Trying to divide by zero (this will cause an exception)
    try:
        result = 10 / 0
    except ZeroDivisionError as e:
        print(f"Error: {e}")

    # Trying to access an element in a list that doesn't exist (this will cause an exception)
    my_list = [1, 2, 3]
    try:
        element = my_list[5]
    except IndexError as e:
        print(f"Error: {e}")

    # Trying to convert a string to an integer (this will cause an exception)
    try:
        number = int("hello")
    except ValueError as e:
        print(f"Error: {e}")

    """
    Important Points:
    - Exceptions are errors that occur during the execution of a program.
    - Common exceptions include ZeroDivisionError, IndexError, and ValueError.
    - The try-except block is used to handle exceptions and manage errors gracefully.
    - The except block catches the exception and allows the program to continue running.
    - Understanding exceptions is essential for writing robust and error-resistant code in Python.
    """

if __name__ == "__main__":
    main()


