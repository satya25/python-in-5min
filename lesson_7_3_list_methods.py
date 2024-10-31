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
# File Name         :       lesson_7_3_list_methods.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Oct 26, 2024
# version           :       1.0
# Release           :       R1
# Dependencies      :       NONE
# Installation      :       NONE
# Usage             :       python ./src/lesson_7_3_list_methods.py
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
Lesson 7.3 - List Methods
---------------------------
This script demonstrates various methods available for lists in Python.
We will explore methods for adding, removing, and manipulating elements in a list.
"""

# All imports whenever be applicable comes here.

def main():
    # Understanding list methods with fun examples!
    
    # Creating a list of fruits
    fruits = ["apple", "banana", "cherry"]
    print("Original list of fruits:", fruits)

    # Adding elements to the list
    fruits.append("date")
    print("List of fruits after append:", fruits)

    fruits.insert(1, "blueberry")
    print("List of fruits after insert:", fruits)

    # Removing elements from the list
    fruits.remove("banana")
    print("List of fruits after remove:", fruits)

    popped_fruit = fruits.pop()
    print("List of fruits after pop:", fruits)
    print("Popped fruit:", popped_fruit)

    # Finding elements in the list
    index_of_cherry = fruits.index("cherry")
    print("Index of 'cherry':", index_of_cherry)

    count_of_apple = fruits.count("apple")
    print("Count of 'apple':", count_of_apple)

    # Sorting the list
    fruits.sort()
    print("List of fruits after sort:", fruits)

    fruits.reverse()
    print("List of fruits after reverse:", fruits)

    # Copying the list
    fruits_copy = fruits.copy()
    print("Copy of the list of fruits:", fruits_copy)

    # Clearing the list
    fruits.clear()
    print("List of fruits after clear:", fruits)

    """
    Important Points:
    - List methods provide various ways to add, remove, and manipulate elements in a list.
    - Common list methods include append(), insert(), remove(), pop(), index(), count(), sort(), reverse(), copy(), and clear().
    - Understanding list methods helps in effectively managing and manipulating lists in Python.
    """

if __name__ == "__main__":
    main()


