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
# File Name         :       lesson_7_2_accessing_list_elements.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Oct 26, 2024
# version           :       1.0
# Release           :       R1
# Dependencies      :       NONE
# Installation      :       NONE
# Usage             :       python ./src/lesson_7_2_accessing_list_elements.py
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
Lesson 7.2 - Accessing List Elements
-------------------------------------
This script demonstrates how to access elements in a list in Python.
We will explore different methods for accessing individual elements and slices of a list.
"""

# All imports whenever be applicable comes here.

def main():
    # Understanding how to access list elements with fun examples!
    
    # Creating a list of animals
    animals = ["dog", "cat", "elephant", "giraffe", "lion"]
    print("List of animals:", animals)

    # Accessing elements by index
    first_animal = animals[0]
    print("First animal:", first_animal)

    third_animal = animals[2]
    print("Third animal:", third_animal)

    # Accessing elements using negative indexing
    last_animal = animals[-1]
    print("Last animal:", last_animal)

    second_last_animal = animals[-2]
    print("Second last animal:", second_last_animal)

    # Slicing a list to get a sublist
    first_two_animals = animals[0:2]
    print("First two animals:", first_two_animals)

    middle_animals = animals[1:4]
    print("Middle animals:", middle_animals)

    # Accessing elements in a loop
    print("All animals in the list:")
    for animal in animals:
        print(animal)

    """
    Important Points:
    - Lists are ordered collections, and elements can be accessed by their index.
    - Indexing starts from 0 for the first element and -1 for the last element.
    - Negative indexing allows accessing elements from the end of the list.
    - Slicing allows creating sublists by specifying a range of indices.
    - Understanding how to access list elements helps in effectively managing and manipulating data.
    """

if __name__ == "__main__":
    main()



