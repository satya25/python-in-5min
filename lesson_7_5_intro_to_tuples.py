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
# File Name         :       lesson_7_5_intro_to_tuples.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Oct 26, 2024
# version           :       1.0
# Release           :       R1
# Dependencies      :       NONE
# Installation      :       NONE
# Usage             :       python ./src/lesson_7_5_intro_to_tuples.py
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
Lesson 7.5 - Introduction to Tuples
-------------------------------------
This script introduces the concept of tuples in Python.
We will explore how to create, access, and use tuples in Python.
"""

# All imports whenever be applicable comes here.

def main():
    # Understanding tuples with fun examples!
    
    # Creating a tuple of fruits
    fruits = ("apple", "banana", "cherry")
    print("Tuple of fruits:", fruits)

    # Accessing elements in a tuple
    first_fruit = fruits[0]
    print("First fruit:", first_fruit)

    third_fruit = fruits[2]
    print("Third fruit:", third_fruit)

    # Tuples are immutable (cannot be changed)
    # Uncommenting the following line will cause an error
    # fruits[1] = "blueberry"

    # Tuples can contain different data types
    person = ("Alice", 30, 5.6, True)
    print("Tuple of person information:", person)

    # Nesting tuples
    nested_tuple = (fruits, person)
    print("Nested tuple:", nested_tuple)

    # Accessing elements in nested tuples
    nested_first_fruit = nested_tuple[0][0]
    nested_person_name = nested_tuple[1][0]
    print("First fruit in nested tuple:", nested_first_fruit)
    print("Person's name in nested tuple:", nested_person_name)

    """
    Important Points:
    - Tuples are ordered collections of items that are immutable (cannot be changed).
    - Tuples are created using parentheses (), with items separated by commas.
    - Elements in a tuple can be accessed by their index, starting from 0.
    - Tuples can contain elements of different data types and can be nested.
    - Understanding tuples is essential for managing immutable collections of data in Python.
    """

if __name__ == "__main__":
    main()

