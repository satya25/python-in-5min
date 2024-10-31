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
# File Name         :       lesson_8_7_set_operations.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Oct 26, 2024
# version           :       1.0
# Release           :       R1
# Dependencies      :       NONE
# Installation      :       NONE
# Usage             :       python ./src/lesson_8_7_set_operations.py
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
Lesson 8.7 - Set Operations
-----------------------------
This script demonstrates various operations that can be performed on sets in Python.
We will explore union, intersection, difference, and symmetric difference operations.
"""

# All imports whenever be applicable comes here.

def main():
    # Understanding set operations with fun examples!
    
    # Creating two sets of fruits
    set_a = {"apple", "banana", "cherry"}
    set_b = {"banana", "cherry", "date"}

    print("Set A:", set_a)
    print("Set B:", set_b)

    # Union of two sets
    union_set = set_a.union(set_b)
    print("Union of Set A and Set B:", union_set)

    # Intersection of two sets
    intersection_set = set_a.intersection(set_b)
    print("Intersection of Set A and Set B:", intersection_set)

    # Difference of two sets (elements in set_a but not in set_b)
    difference_set = set_a.difference(set_b)
    print("Difference of Set A and Set B:", difference_set)

    # Symmetric difference of two sets (elements in either set_a or set_b but not in both)
    sym_diff_set = set_a.symmetric_difference(set_b)
    print("Symmetric Difference of Set A and Set B:", sym_diff_set)

    """
    Important Points:
    - Set operations allow combining and comparing sets in various ways.
    - The union() method returns a set containing all unique elements from both sets.
    - The intersection() method returns a set containing only elements common to both sets.
    - The difference() method returns a set containing elements in the first set but not in the second set.
    - The symmetric_difference() method returns a set containing elements in either set but not in both.
    - Understanding set operations helps in effectively managing and manipulating sets in Python.
    """

if __name__ == "__main__":
    main()



