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
# File Name         :       lesson_5_1_intro_to_control_flow.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Oct 26, 2024
# version           :       1.0
# Release           :       R1
# Dependencies      :       NONE
# Installation      :       NONE
# Usage             :       python ./src/lesson_5_1_intro_to_control_flow.py
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
Lesson 5.1 - Introduction to Control Flow
------------------------------------------
This script introduces the concept of control flow in Python.
We will explore how to use conditional statements and loops to control the flow of a program.
"""

# All imports whenever be applicable comes here.

def main():
    # Understanding control flow with some fun examples!
    
    # Declaring variables
    age = 20
    height = 5.8

    # Conditional statements (if, elif, else)
    # Making decisions based on conditions
    if age >= 18:
        print("You are an adult.")
    elif age >= 13:
        print("You are a teenager.")
    else:
        print("You are a child.")

    # Looping with while loop
    # Repeating a block of code as long as a condition is true
    counter = 0
    while counter < 5:
        print("Counter is:", counter)
        counter += 1  # Incrementing the counter

    # Looping with for loop
    # Iterating over a sequence (such as a list or string)
    fruits = ["apple", "banana", "cherry"]
    for fruit in fruits:
        print("I like", fruit)

    """
    Important Points:
    - Control flow allows us to make decisions and repeat actions in a program.
    - Conditional statements (if, elif, else) execute different code blocks based on conditions.
    - Loops (while, for) allow us to repeat actions multiple times.
    - Understanding control flow is essential for writing efficient and effective programs.
    """

if __name__ == "__main__":
    main()

