#!/usr/bin/en
# -*- coding: utf-8 -*-

# ----------------------------------------------------------------------------
# File Name         :       lesson_2_6_intro_to_type_conversions.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Oct 26, 2024
# version           :       1.0
# Release           :       R1
#
# Dependencies      :       NONE
#
# Installation      :       NONE
#
# Usage             :       python ./src/lesson_2_6_intro_to_type_conversions.py
#
# ---------------------------------------------------------------------------
#
# Credits and Acknowledgements
#
# - Special thanks to the Python community for their excellent work:
#   https://www.python.org/community/
#
# - The APIs used in this script is documented here:
#   https://numpy.org/doc/stable/reference/index.html
#
# - Code Snippet(s) adapted from    :   -- NOT Applicable --
#
# - Dataset(s) sourced  from        :   -- NOT Applicable --
#
#
# - Inspiration drawn from          :   -- NOT Applicable --
#    
#
# Thank you to the creators and maintainers of these resources!
#
# ---------------------------------------------------------------------------
#
# - Content Removal Requests
#
#   If you are the owner or creator of any content used in this script and
#   would like it to be removed, please contact me at:  spnigam25@yahoo.com
#   I will promptly remove the content upon request.
#
# ---------------------------------------------------------------------------
  

"""
Lesson 2.6 - Introduction to Type Conversions
---------------------------------------------
This script introduces type conversions in Python. 
We will learn how to convert one data type to another.
"""

## All imports whenever be applicable comes here.

def main():

    # Declaring variables of different types
    age = 25             # Integer
    height = 5.6         # Float
    name = "Prakash"       # String
    is_student = True    # Boolean

    # Converting integer to float
    # Using the float() function
    age_as_float = float(age)
    print("Age as float:", age_as_float)

    # Converting float to integer
    # Using the int() function
    height_as_int = int(height)
    print("Height as integer:", height_as_int)

    # Converting integer to string
    # Using the str() function
    age_as_string = str(age)
    print("Age as string:", age_as_string)

    # Converting string to integer
    # Using the int() function
    age_string = "30"
    age_from_string = int(age_string)
    print("Age from string:", age_from_string)

    # Converting boolean to integer
    # Using the int() function
    is_student_as_int = int(is_student)
    print("Is student as integer:", is_student_as_int)

    # Converting string to float
    # Using the float() function
    height_string = "5.9"
    height_from_string = float(height_string)
    print("Height from string:", height_from_string)

    """
    Important Points:
    - Type conversion allows us to change the data type of a variable.
    - Common type conversion functions include int(), float(), and str().
    - Ensure the value being converted is compatible with the target data type to avoid errors.
    - Type conversion is useful when performing operations that require a specific data type.
    """

if __name__ == "__main__":
    main()
 
 