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
# File Name         :       lesson_8_5_intro_to_sets.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Oct 26, 2024
# version           :       1.0
# Release           :       R1
# Dependencies      :       NONE
# Installation      :       NONE
# Usage             :       python ./src/lesson_8_5_intro_to_sets.py
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
Lesson 8.5 - Introduction to Sets
-----------------------------------
This script introduces the concept of sets in Python.
We will explore how to create, access, and use sets in Python.
"""

# All imports whenever be applicable comes here.

def main():
    # Understanding sets with fun examples!
    
    # Creating a set of fruits
    fruits = {"apple", "banana", "cherry"}
    print("Set of fruits:", fruits)

    # Adding elements to a set
    fruits.add("date")
    print("Set of fruits after adding 'date':", fruits)

    # Removing elements from a set
    fruits.remove("banana")
    print("Set of fruits after removing 'banana':", fruits)

    # Checking membership in a set
    has_apple = "apple" in fruits
    print("Is 'apple' in the set of fruits:", has_apple)

    # Sets automatically remove duplicates
    fruits.add("apple")
    fruits.add("apple")
    print("Set of fruits after adding duplicate 'apple':", fruits)

    """
    Important Points:
    - Sets are unordered collections of unique elements.
    - Sets are created using curly braces {} or the set() function.
    - Elements in a set can be added using the add() method.
    - Elements in a set can be removed using the remove() method.
    - Sets do not allow duplicate elements, and duplicates are automatically removed.
    - Understanding sets is essential for managing collections of unique data in Python.
    """

if __name__ == "__main__":
    main()


