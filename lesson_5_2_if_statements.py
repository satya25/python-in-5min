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
# File Name         :       lesson_5_2_if_statements.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Oct 26, 2024
# version           :       1.0
# Release           :       R1
# Dependencies      :       NONE
# Installation      :       NONE
# Usage             :       python ./src/lesson_5_2_if_statements.py
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
Lesson 5.2 - If Statements
----------------------------
This script demonstrates the use of if statements in Python.
We will explore how to make decisions in our code based on conditions.
"""

# All imports whenever be applicable comes here.

def main():
    # Understanding if statements with fun examples!
    
    # Declaring a variable
    temperature = 25  # in degrees Celsius

    # Using an if statement to make decisions
    if temperature > 30:
        print("It's a hot day! Stay hydrated.")
    elif temperature > 20:
        print("It's a warm day! Enjoy the sunshine.")
    elif temperature > 10:
        print("It's a cool day! A light jacket would be nice.")
    else:
        print("It's a cold day! Stay warm.")

    # Checking if a number is even or odd
    number = 42
    if number % 2 == 0:
        print(number, "is an even number.")
    else:
        print(number, "is an odd number.")

    """
    Important Points:
    - If statements allow us to execute code based on conditions.
    - The 'if' keyword is used to check a condition.
    - The 'elif' keyword (short for else if) checks another condition if the previous ones are false.
    - The 'else' keyword runs code when all previous conditions are false.
    - Understanding if statements helps in making decisions and controlling the flow of a program.
    """

if __name__ == "__main__":
    main()


