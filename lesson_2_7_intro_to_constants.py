#!/usr/bin/en
# -*- coding: utf-8 -*-

# ----------------------------------------------------------------------------
# File Name         :       lesson_2_7_intro_to_constants.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Oct 26, 2024
# version           :       1.0
# Release           :       R1
#
# Dependencies      :       NONE
#
# Installation      :       NONE
#
# Usage             :       python ./src/lesson_2_7_intro_to_constants.py
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
Lesson 2.7 - Introduction to Constants
--------------------------------------
This script introduces constants in Python. 
We will learn how to declare and use constants.
"""

## All imports whenever be applicable comes here.

def main():
 
    # Declaring constants
    # Constants are variables whose values are not meant to change.
    # In Python, we use all uppercase letters to indicate a constant.

    # This is a constant representing the value of pi
    PI = 3.14159

    # This is a constant representing the maximum speed limit in km/h
    MAX_SPEED = 120

    # Using constants in calculations

    # Calculating the circumference of a circle
    radius = 5
    circumference = 2 * PI * radius
    print("Circumference of the circle:", circumference)

    # Checking speed against the maximum speed limit
    current_speed = 100
    is_speeding = current_speed > MAX_SPEED
    print("Is the vehicle speeding:", is_speeding)

    """
    Important Points:
    - Constants are variables whose values should not change during the execution of a program.
    - Use uppercase letters to declare constants for better readability and convention.
    - Constants help make code more readable and maintainable by providing clear, descriptive names for fixed values.
    - Although Python doesn't have built-in support for constants, using conventions can help indicate their purpose.
    """


if __name__ == "__main__":
    main()
 
 
