#!/usr/bin/en
# -*- coding: utf-8 -*-

# ----------------------------------------------------------------------------
# File Name         :       lesson_2_2_intro_to_integers.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Oct 26, 2024
# version           :       1.0
# Release           :       R1
#
# Dependencies      :       NONE
#
# Installation      :       NONE
#
# Usage             :       python ./src/lesson_2_2_intro_to_integers.py
#
# ---------------------------------------------------------------------------
#
# Credits and Acknowledgements
#
# - Special thanks to the Python community for their excellent work:
#   https://www.python.org/community/
#
# - The APIs used in this script is documented here:
#   https://docs.python.org/3/
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
Lesson 2.2 - Introduction to Integers
-------------------------------------
This script introduces integers in Python. 
We will learn how to declare integer variables and perform basic operations.
"""

## All imports whenever be applicable comes here.

def main():
    # Declaring integer variables
    # Integers are whole numbers, without a decimal point

    # This is an integer variable representing age
    age = 25

    # This is an integer variable representing number of apples
    number_of_apples = 10

    # Performing basic arithmetic operations with integers

    # Adding two integers
    total_age = age + 5  # Adding 5 years to the age
    print("Total Age:", total_age)

    # Subtracting two integers
    remaining_apples = number_of_apples - 3  # Subtracting 3 apples
    print("Remaining Apples:", remaining_apples)

    # Multiplying two integers
    double_age = age * 2  # Doubling the age
    print("Double Age:", double_age)

    # Dividing two integers
    half_apples = number_of_apples // 2  # Integer division
    print("Half Apples:", half_apples)

    # Finding the remainder of a division (modulus)
    remainder_apples = number_of_apples % 3  # Remainder when dividing by 3
    print("Remainder Apples:", remainder_apples)

    """
    Important Points:
    - Integers are whole numbers (positive or negative) without decimal points.
    - Basic arithmetic operations include addition (+), subtraction (-), multiplication (*), and integer division (//).
    - The modulus operator (%) gives the remainder of a division.
    """

if __name__ == "__main__":
    main()

 