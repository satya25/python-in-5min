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
# File Name         :       lesson_4_4_string_methods.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Oct 26, 2024
# version           :       1.0
# Release           :       R1
# Dependencies      :       NONE
# Installation      :       NONE
# Usage             :       python ./src/lesson_4_4_string_methods.py
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
Lesson 4.4 - String Methods
----------------------------
This script demonstrates various string methods in Python.
We will explore common methods to manipulate and format strings.
"""

# All imports whenever be applicable comes here.

def main():
    # Let's explore some common string methods with quirky examples!
    
    # Declaring a string variable
    text = "  Python is awesome!  "

    # .strip() - Removes leading and trailing whitespace
    stripped_text = text.strip()
    print("Stripped text:", stripped_text)

    # .lower() - Converts all characters to lowercase
    lowercase_text = text.lower()
    print("Lowercase text:", lowercase_text)

    # .upper() - Converts all characters to uppercase
    uppercase_text = text.upper()
    print("Uppercase text:", uppercase_text)

    # .replace() - Replaces a substring with another substring
    replaced_text = text.replace("awesome", "fantastic")
    print("Replaced text:", replaced_text)

    # .split() - Splits the string into a list of substrings
    words_list = text.split()
    print("List of words:", words_list)

    # .join() - Joins a list of strings into a single string
    joined_text = " ".join(words_list)
    print("Joined text:", joined_text)

    # .find() - Finds the index of the first occurrence of a substring
    index_of_is = text.find("is")
    print("Index of 'is':", index_of_is)

    # .count() - Counts the number of occurrences of a substring
    count_of_is = text.count("is")
    print("Count of 'is':", count_of_is)

    """
    Important Points:
    - String methods are built-in functions that can be used to manipulate and format strings.
    - Common string methods include strip(), lower(), upper(), replace(), split(), join(), find(), and count().
    - Understanding and using string methods can make string manipulation easier and more efficient.
    """

if __name__ == "__main__":
    main()
