#!/usr/bin/en
# -*- coding: utf-8 -*-

# ----------------------------------------------------------------------------
# File Name         :       lesson_2_3_intro_to_floats.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Oct 26, 2024
# version           :       1.0
# Release           :       R1
#
# Dependencies      :       NONE
#
# Installation      :       NONE
#
# Usage             :       python ./src/lesson_2_3_intro_to_floats.py
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
Lesson 2.3 - Introduction to Floats
-----------------------------------
This script introduces floats in Python. 
We will learn how to declare float variables and perform basic operations.
"""

## All imports whenever be applicable comes here.

def main():

    # Declaring float variables
    # Floats are numbers with a decimal point

    # This is a float variable representing height in meters
    height = 5.6

    # This is a float variable representing price in dollars
    price = 12.99

    # Performing basic arithmetic operations with floats

    # Adding two floats
    total_height = height + 0.4  # Adding 0.4 meters to the height
    print("Total Height:", total_height)

    # Subtracting two floats
    discounted_price = price - 2.99  # Subtracting a discount of $2.99
    print("Discounted Price:", discounted_price)

    # Multiplying two floats
    double_height = height * 2  # Doubling the height
    print("Double Height:", double_height)

    # Dividing two floats
    half_price = price / 2  # Dividing the price by 2
    print("Half Price:", half_price)

    # Raising a float to a power
    square_height = height ** 2  # Squaring the height
    print("Square Height:", square_height)

    """
    Important Points:
    - Floats are numbers with decimal points, allowing for greater precision.
    - Basic arithmetic operations include addition (+), subtraction (-), 
      multiplication (*), division (/), and exponentiation (**).
    - Use floats for measurements, prices, and any value requiring precision.
    """

if __name__ == "__main__":
    main()

 
