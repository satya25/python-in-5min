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
# File Name         :       lesson_7_4_iterating_over_lists.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Oct 26, 2024
# version           :       1.0
# Release           :       R1
# Dependencies      :       NONE
# Installation      :       NONE
# Usage             :       python ./src/lesson_7_4_iterating_over_lists.py
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
Lesson 7.4 - Iterating Over Lists
-----------------------------------
This script demonstrates how to iterate over lists in Python.
We will explore different methods for looping through list elements.
"""

# All imports whenever be applicable comes here.

def main():
    # Understanding how to iterate over lists with fun examples!
    
    # Creating a list of numbers
    numbers = [1, 2, 3, 4, 5]
    print("List of numbers:", numbers)

    # Iterating over the list using a for loop
    print("Iterating using a for loop:")
    for number in numbers:
        print(number)

    # Iterating over the list using a while loop
    print("Iterating using a while loop:")
    index = 0
    while index < len(numbers):
        print(numbers[index])
        index += 1

    # Iterating over the list with index using enumerate()
    print("Iterating using enumerate() to get index and value:")
    for index, value in enumerate(numbers):
        print(f"Index: {index}, Value: {value}")

    """
    Important Points:
    - Iterating over lists is common and essential for performing operations on each element.
    - The for loop is the most straightforward way to iterate over a list.
    - The while loop can also be used for iteration, especially when working with conditions.
    - The enumerate() function provides both the index and the value during iteration.
    - Understanding different ways to iterate over lists helps in effectively managing and manipulating list data.
    """

if __name__ == "__main__":
    main()


