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
# File Name         :       lesson_4_8_string_formatting_f_strings.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Oct 26, 2024
# version           :       1.0
# Release           :       R1
# Dependencies      :       NONE
# Installation      :       NONE
# Usage             :       python ./src/lesson_4_8_string_formatting_f_strings.py
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
Lesson 4.8 - String Formatting (f-Strings)
--------------------------------------------
This script demonstrates string formatting using f-strings (formatted string literals) in Python.
We will explore how to format strings with different data types.
"""

# All imports whenever be applicable comes here.

def main():
    # Let's dive into f-strings with quirky examples!
    
    # Declaring variables
    name = "Alice"
    age = 25
    height = 5.6
    score = 95.5

    # Formatting strings using f-strings
    formatted_string1 = f"Name: {name}"
    print(formatted_string1)

    formatted_string2 = f"Age: {age}"
    print(formatted_string2)

    formatted_string3 = f"Height: {height:.1f}"
    print(formatted_string3)

    formatted_string4 = f"Score: {score:.2f}"
    print(formatted_string4)

    # Formatting multiple values
    formatted_string5 = f"Name: {name}, Age: {age}, Height: {height:.1f}, Score: {score:.2f}"
    print(formatted_string5)

    """
    Important Points:
    - f-Strings (formatted string literals) are a concise and readable way to embed expressions inside string literals using curly braces {}.
    - f-Strings are prefixed with 'f' or 'F' before the opening quotation mark.
    - Expressions inside curly braces are evaluated at runtime and formatted using format specifiers.
    - f-Strings are a preferred method for string formatting in Python for their readability and ease of use.
    """

if __name__ == "__main__":
    main()


