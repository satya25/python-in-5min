#!/usr/bin/en
# -*- coding: utf-8 -*-

# ----------------------------------------------------------------------------
# File Name         :       lesson_2_1_intro_to_variables.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Oct 26, 2024
# version           :       1.0
# Release           :       R1
#
# Dependencies      :       NONE
#
# Installation      :       NONE
#
# Usage             :       python ./src/lesson_2_1_intro_to_variables.py
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
Lesson 2.1 - Introduction to Variables
--------------------------------------
This script introduces the concept of variables in Python. 
We will explore how to declare variables, assign values, and use them.
"""

## All imports whenever be applicable comes here.
 
def main():
    # Declaring and initializing variables
    # Variables are like boxes where we can store different types of information

    # This is an integer variable
    age         = 25 
    your_age    = 34
    his_age     = 40
    her_age     = 50

    # This is a float variable (a number with a decimal point)
    height = 5.6

    # This is a string variable (a sequence of characters)
    name = "Satya" # You can change the name of variable here.

    # This is a boolean variable (True or False value)
    is_student = True

    # Printing the variables to see their values
    print("Age:", age)
    print("Your Age:", your_age)
    print("His Age:", his_age)
    print("Her Age:", her_age)
    
    print("Height:", height)
    print("Name:", name)
    print("Is Student:", is_student)

    """
    Important Points:
    - Variables can store different types of data.
    - No need to specify the data type; Python understands it automatically.
    - Variable names should be descriptive and follow naming conventions.
    - Use underscores (_) to separate words in variable names for readability.
    """
 
if __name__ == "__main__":
    main()
