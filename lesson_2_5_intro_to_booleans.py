#!/usr/bin/en
# -*- coding: utf-8 -*-

# ----------------------------------------------------------------------------
# File Name         :       lesson_2_5_intro_to_booleans.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Oct 26, 2024
# version           :       1.0
# Release           :       R1
#
# Dependencies      :       NONE
#
# Installation      :       NONE
#
# Usage             :       python ./src/lesson_2_5_intro_to_booleans.py
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
Lesson 2.5 - Introduction to Booleans
--------------------------------------
This script introduces booleans in Python. 
We will learn how to declare boolean variables and perform basic logical operations.
"""

## All imports whenever be applicable comes here.

def main():

    # Declaring boolean variables
    # Booleans can only have two values: True or False

    # This is a boolean variable indicating if a person is a student
    is_student = True

    # This is a boolean variable indicating if it is raining
    is_raining = False

    # Performing basic logical operations with booleans

    # Using the "and" operator
    # The result is True only if both conditions are True
    can_go_outside = is_student and not is_raining
    print("Can go outside:", can_go_outside)

    # Using the "or" operator
    # The result is True if at least one of the conditions is True
    has_umbrella = False
    can_go_outside_with_umbrella = is_raining or has_umbrella
    print("Can go outside with umbrella:", can_go_outside_with_umbrella)

    # Using the "not" operator
    # The result is the opposite boolean value
    is_not_raining = not is_raining
    print("Is it not raining:", is_not_raining)

    """
    Important Points:
    - Booleans represent truth values and can only be True or False.
    - Basic logical operations include "and", "or", and "not".
    - The "and" operator returns True only if both conditions are True.
    - The "or" operator returns True if at least one condition is True.
    - The "not" operator inverts the boolean value.
    """
 
if __name__ == "__main__":
    main()
 
