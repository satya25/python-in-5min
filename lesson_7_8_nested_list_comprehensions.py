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
# File Name         :       lesson_7_8_nested_list_comprehensions.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Oct 26, 2024
# version           :       1.0
# Release           :       R1
# Dependencies      :       NONE
# Installation      :       NONE
# Usage             :       python ./src/lesson_7_8_nested_list_comprehensions.py
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
Lesson 7.8 - Nested List Comprehensions
-----------------------------------------
This script introduces the concept of nested list comprehensions in Python.
We will explore how to create lists using nested list comprehensions for more complex scenarios.
"""

# All imports whenever be applicable comes here.

def main():
    # Understanding nested list comprehensions with fun examples!
    
    # Creating a matrix using nested loops
    matrix = []
    for i in range(3):
        row = []
        for j in range(3):
            row.append(i * j)
        matrix.append(row)
    print("Matrix using nested loops:")
    for row in matrix:
        print(row)

    # Creating a matrix using nested list comprehensions
    matrix_comp = [[i * j for j in range(3)] for i in range(3)]
    print("Matrix using nested list comprehensions:")
    for row in matrix_comp:
        print(row)

    # Flattening a nested list using nested loops
    nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flat_list = []
    for sublist in nested_list:
        for item in sublist:
            flat_list.append(item)
    print("Flattened list using nested loops:", flat_list)

    # Flattening a nested list using a nested list comprehension
    flat_list_comp = [item for sublist in nested_list for item in sublist]
    print("Flattened list using nested list comprehension:", flat_list_comp)

    """
    Important Points:
    - Nested list comprehensions provide a concise way to create and manipulate nested lists.
    - Nested list comprehensions follow the syntax: [expression for item in iterable for subitem in subiterable].
    - Using nested list comprehensions can simplify code and make it more readable.
    - Understanding nested list comprehensions helps in efficiently creating and manipulating complex lists in Python.
    """

if __name__ == "__main__":
    main()


