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
# File Name         :       lesson_5_4_for_loops.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Oct 26, 2024
# version           :       1.0
# Release           :       R1
# Dependencies      :       NONE
# Installation      :       NONE
# Usage             :       python ./src/lesson_5_4_for_loops.py
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
Lesson 5.4 - For Loops
-----------------------
This script demonstrates the use of for loops in Python.
We will explore how to iterate over sequences and perform repetitive tasks.
"""

# All imports whenever be applicable comes here.

def main():
    # Understanding for loops with fun examples!
    
    # Iterating over a list of fruits
    fruits = ["apple", "banana", "cherry"]
    for fruit in fruits:
        print("I like", fruit)

    # Iterating over a string
    word = "Python"
    for letter in word:
        print("Letter:", letter)

    # Using range() function in a for loop
    for number in range(5):
        print("Number:", number)

    # Iterating over a list with index
    for index, fruit in enumerate(fruits):
        print("Fruit at index", index, "is", fruit)

    """
    Important Points:
    - For loops are used to iterate over sequences (like lists, strings, and ranges).
    - The range() function generates a sequence of numbers.
    - The enumerate() function provides both index and value while iterating over a sequence.
    - For loops help in performing repetitive tasks efficiently.
    """

if __name__ == "__main__":
    main()

