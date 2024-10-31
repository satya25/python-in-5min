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
# File Name         :       lesson_8_6_set_methods.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Oct 26, 2024
# version           :       1.0
# Release           :       R1
# Dependencies      :       NONE
# Installation      :       NONE
# Usage             :       python ./src/lesson_8_6_set_methods.py
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
Lesson 8.6 - Set Methods
--------------------------
This script demonstrates various methods available for sets in Python.
We will explore methods for adding, removing, and manipulating set elements.
"""

# All imports whenever be applicable comes here.

def main():
    # Understanding set methods with fun examples!
    
    # Creating a set of fruits
    fruits = {"apple", "banana", "cherry"}
    print("Original set of fruits:", fruits)

    # Adding elements to the set
    fruits.add("date")
    print("Set of fruits after add:", fruits)

    # Removing elements from the set
    fruits.remove("banana")
    print("Set of fruits after remove:", fruits)

    # Removing elements using discard()
    fruits.discard("cherry")
    print("Set of fruits after discard:", fruits)

    # Removing and returning a random element using pop()
    popped_fruit = fruits.pop()
    print("Set of fruits after pop:", fruits)
    print("Popped fruit:", popped_fruit)

    # Clearing the set
    fruits.clear()
    print("Set of fruits after clear:", fruits)

    # Creating another set of vegetables
    vegetables = {"carrot", "broccoli", "spinach"}
    print("Set of vegetables:", vegetables)

    # Union of two sets
    food = fruits.union(vegetables)
    print("Union of fruits and vegetables:", food)

    # Intersection of two sets
    common_food = fruits.intersection(vegetables)
    print("Intersection of fruits and vegetables:", common_food)

    # Difference of two sets
    diff_food = vegetables.difference(fruits)
    print("Difference of vegetables and fruits:", diff_food)

    # Symmetric difference of two sets
    sym_diff_food = vegetables.symmetric_difference(fruits)
    print("Symmetric difference of vegetables and fruits:", sym_diff_food)

    """
    Important Points:
    - Set methods provide various ways to add, remove, and manipulate elements in a set.
    - Common set methods include add(), remove(), discard(), pop(), clear(), union(), intersection(), difference(), and symmetric_difference().
    - Understanding set methods helps in effectively managing and manipulating sets in Python.
    """

if __name__ == "__main__":
    main()


