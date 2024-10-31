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
# File Name         :       lesson_4_5_string_immutability.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Oct 26, 2024
# version           :       1.0
# Release           :       R1
# Dependencies      :       NONE
# Installation      :       NONE
# Usage             :       python ./src/lesson_4_5_string_immutability.py
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
Lesson 4.5 - String Immutability
----------------------------------
This script explains the concept of string immutability in Python.
We will explore what it means for a string to be immutable and how to work with strings effectively.
"""

# All imports whenever be applicable comes here.

def main():
    # Understanding string immutability with some fun examples!
    
    # Declaring a string variable
    original_string = "Hello, world!"
    print("Original string:", original_string)
    
    # Attempting to modify an individual character in the string (will cause an error)
    try:
        original_string[0] = 'h'
    except TypeError as e:
        print("Error:", e)
    
    # Creating a new string by modifying the original string
    # Since strings are immutable, we create a new string instead of changing the original
    new_string = 'h' + original_string[1:]
    print("New string:", new_string)
    
    # Using string methods to create new strings
    uppercase_string = original_string.upper()
    print("Uppercase string:", uppercase_string)
    
    replaced_string = original_string.replace("world", "Python")
    print("Replaced string:", replaced_string)
    
    """
    Important Points:
    - Strings in Python are immutable, meaning their values cannot be changed after they are created.
    - Any modification to a string results in the creation of a new string.
    - Understanding immutability helps in working with strings more effectively and efficiently.
    """

if __name__ == "__main__":
    main()


