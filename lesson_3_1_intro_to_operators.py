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
# File Name         :       lesson_3_1_intro_to_operators.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Oct 26, 2024
# version           :       1.0
# Release           :       R1
# Dependencies      :       NONE
# Installation      :       NONE
# Usage             :       python ./src/lesson_3_1_intro_to_operators.py
# ----------------------------------------------------------------------------
# Credits and Acknowledgements
#
# - Special thanks to the Python community for their excellent work:
#   https://www.python.org/community/
#
# - The APIs used in this script is documented here:
#   https://docs.python.org/3/
#
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
Lesson 3.1 - Introduction to Operators
--------------------------------------
This script introduces operators in Python.
We will explore arithmetic, comparison, logical, and assignment operators.
"""

# All imports whenever be applicable comes here.

def main():
    # Arithmetic Operators
    # Used to perform mathematical operations

    a = 10
    b = 3

    # Addition
    addition = a + b
    print("Addition:", addition)

    # Subtraction
    subtraction = a - b
    print("Subtraction:", subtraction)

    # Multiplication
    multiplication = a * b
    print("Multiplication:", multiplication)

    # Division
    division = a / b
    print("Division:", division)

    # Modulus
    modulus = a % b
    print("Modulus:", modulus)

    # Exponentiation
    exponentiation = a ** b
    print("Exponentiation:", exponentiation)

    # Floor Division
    floor_division = a // b
    print("Floor Division:", floor_division)

    # Comparison Operators
    # Used to compare two values

    # Equal to
    is_equal = (a == b)
    print("Is Equal:", is_equal)

    # Not equal to
    is_not_equal = (a != b)
    print("Is Not Equal:", is_not_equal)

    # Greater than
    is_greater = (a > b)
    print("Is Greater:", is_greater)

    # Less than
    is_less = (a < b)
    print("Is Less:", is_less)

    # Greater than or equal to
    is_greater_equal = (a >= b)
    print("Is Greater or Equal:", is_greater_equal)

    # Less than or equal to
    is_less_equal = (a <= b)
    print("Is Less or Equal:", is_less_equal)

    # Logical Operators
    # Used to combine conditional statements

    x = True
    y = False

    # AND operator
    and_operator = x and y
    print("AND Operator:", and_operator)

    # OR operator
    or_operator = x or y
    print("OR Operator:", or_operator)

    # NOT operator
    not_operator = not x
    print("NOT Operator:", not_operator)

    # Assignment Operators
    # Used to assign values to variables

    c = 5
    print("Initial Value of c:", c)

    # Add and assign
    c += 2
    print("c after += 2:", c)

    # Subtract and assign
    c -= 1
    print("c after -= 1:", c)

    # Multiply and assign
    c *= 3
    print("c after *= 3:", c)

    # Divide and assign
    c /= 4
    print("c after /= 4:", c)

    # Modulus and assign
    c %= 2
    print("c after %= 2:", c)

    """
    Important Points:
    - Arithmetic operators include +, -, *, /, %, **, and //.
    - Comparison operators include ==, !=, >, <, >=, and <=.
    - Logical operators include and, or, and not.
    - Assignment operators include =, +=, -=, *=, /=, and %=.
    """

if __name__ == "__main__":
    main()


