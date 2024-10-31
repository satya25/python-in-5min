#!/usr/bin/en
# -*- coding: utf-8 -*-

# ----------------------------------------------------------------------------
# File Name         :       lesson_2_4_intro_to_strings.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Oct 26, 2024
# version           :       1.0
# Release           :       R1
#
# Dependencies      :       NONE
#
# Installation      :       NONE
#
# Usage             :       python ./src/lesson_2_4_intro_to_strings.py
#
# ---------------------------------------------------------------------------
#
# Credits and Acknowledgements
#
# - Special thanks to the Python community for their excellent work:
#   https://www.python.org/community/
#
# - The APIs used in this script is documented here:
#   https://numpy.org/doc/stable/reference/index.html
#
# - Code Snippet(s) adapted from    :   -- NOT Applicable --
#
# - Dataset(s) sourced  from        :   -- NOT Applicable --
#
#
# - Inspiration drawn from          :   -- NOT Applicable --
#    
#
# Thank you to the creators and maintainers of these resources!
#
# ---------------------------------------------------------------------------
#
# - Content Removal Requests
#
#   If you are the owner or creator of any content used in this script and
#   would like it to be removed, please contact me at:  spnigam25@yahoo.com
#   I will promptly remove the content upon request.
#
# ---------------------------------------------------------------------------
  

"""
Lesson 2.4 - Introduction to Strings
-------------------------------------
This script introduces strings in Python. 
We will learn how to declare string variables, concatenate strings, and perform basic string operations.
"""

## All imports whenever be applicable comes here.

def main():

    # Declaring string variables
    # Strings are sequences of characters enclosed in quotes

    # This is a string variable representing a name
    name = "Satya"

    # This is a string variable representing a sentence
    greeting = "Hello, world!"

    # Concatenating (combining) strings
    # We can use the + operator to join strings together
    full_greeting = greeting + " My name is " + name + "."
    print(full_greeting)

    # Accessing individual characters in a string
    # We can use indexing to get specific characters from a string
    first_letter = name[0]  # Gets the first character in the string "Alice"
    print("First letter of name:", first_letter)

    # Slicing strings
    # We can get a substring by specifying a range of indices
    name_slice = name[1:4]  # Gets characters from index 1 to 3 (not including 4)
    print("Sliced name:", name_slice)

    # Changing the case of a string
    # We can use methods like .upper() and .lower() to change the case of a string
    uppercase_greeting = greeting.upper()
    print("Uppercase Greeting:", uppercase_greeting)

    lowercase_greeting = greeting.lower()
    print("Lowercase Greeting:", lowercase_greeting)

    """
    Important Points:
    - Strings are sequences of characters, such as words or sentences.
    - Strings are enclosed in single ('') or double ("") quotes.
    - We can concatenate strings using the + operator.
    - Individual characters in a string can be accessed using indexing.
    - We can get substrings by slicing strings with a range of indices.
    - There are several methods available to manipulate strings, such as changing their case.
    """

if __name__ == "__main__":
    main()
 