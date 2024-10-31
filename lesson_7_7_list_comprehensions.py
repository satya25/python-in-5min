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
# File Name         :       lesson_7_7_list_comprehensions.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Oct 26, 2024
# version           :       1.0
# Release           :       R1
# Dependencies      :       NONE
# Installation      :       NONE
# Usage             :       python ./src/lesson_7_7_list_comprehensions.py
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
Lesson 7.7 - List Comprehensions
-----------------------------------
This script introduces the concept of list comprehensions in Python.
We will explore how to create lists in a concise and readable way using list comprehensions.
"""

# All imports whenever be applicable comes here.

def main():
    # Understanding list comprehensions with fun examples!
    
    # Creating a list of squares using a for loop
    squares = []
    for x in range(10):
        squares.append(x**2)
    print("List of squares using for loop:", squares)

    # Creating a list of squares using a list comprehension
    squares_comp = [x**2 for x in range(10)]
    print("List of squares using list comprehension:", squares_comp)

    # Creating a list of even numbers using a for loop
    evens = []
    for x in range(10):
        if x % 2 == 0:
            evens.append(x)
    print("List of even numbers using for loop:", evens)

    # Creating a list of even numbers using a list comprehension
    evens_comp = [x for x in range(10) if x % 2 == 0]
    print("List of even numbers using list comprehension:", evens_comp)

    # Creating a list of tuples using a nested for loop
    tuples = []
    for x in range(3):
        for y in range(3):
            tuples.append((x, y))
    print("List of tuples using nested for loop:", tuples)

    # Creating a list of tuples using a nested list comprehension
    tuples_comp = [(x, y) for x in range(3) for y in range(3)]
    print("List of tuples using nested list comprehension:", tuples_comp)

    """
    Important Points:
    - List comprehensions provide a concise and readable way to create lists.
    - List comprehensions follow the syntax: [expression for item in iterable if condition].
    - Using list comprehensions can simplify code and make it more readable.
    - Understanding list comprehensions helps in efficiently creating and manipulating lists in Python.
    """

if __name__ == "__main__":
    main()


