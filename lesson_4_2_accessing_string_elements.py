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
# File Name         :       lesson_4_2_accessing_string_elements.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Oct 26, 2024
# version           :       1.0
# Release           :       R1
# Dependencies      :       NONE
# Installation      :       NONE
# Usage             :       python ./src/lesson_4_2_accessing_string_elements.py
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
Lesson 4.2 - Accessing String Elements
---------------------------------------
This script demonstrates how to access and manipulate individual characters
and substrings within a string in Python.
"""

# All imports whenever be applicable comes here.

def main():
    # Declaring a string variable
    sentence = "Python is fun!"

    # Accessing individual characters in a string
    # We can use indexing to get specific characters from a string
    first_letter = sentence[0]  # Gets the first character
    print("First letter of sentence:", first_letter)
    
    # Last character using negative indexing
    last_letter = sentence[-1]  # Gets the last character
    print("Last letter of sentence:", last_letter)
    
    # Slicing strings
    # We can get a substring by specifying a range of indices
    first_three = sentence[0:3]  # Gets characters from index 0 to 2 (not including 3)
    print("First three characters:", first_three)
    
    # Slice from the start to a specific position
    up_to_five = sentence[:5]  # Gets characters from the start up to (but not including) index 5
    print("Up to five characters:", up_to_five)
    
    # Slice from a specific position to the end
    from_seven = sentence[7:]  # Gets characters from index 7 to the end
    print("From seventh character onwards:", from_seven)
    
    # Accessing characters in a loop
    for char in sentence:
        print(char, end=' ')
    print()  # New line after loop
    
    """
    Important Points:
    - Strings are sequences of characters, and each character has an index.
    - Indexing starts from 0 for the first character and -1 for the last character.
    - Slicing allows extracting substrings using a range of indices.
    - Indexing and slicing are powerful tools for accessing and manipulating strings.
    """

if __name__ == "__main__":
    main()

