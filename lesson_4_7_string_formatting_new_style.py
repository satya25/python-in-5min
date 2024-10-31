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
# File Name         :       lesson_4_7_string_formatting_new_style.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Oct 26, 2024
# version           :       1.0
# Release           :       R1
# Dependencies      :       NONE
# Installation      :       NONE
# Usage             :       python ./src/lesson_4_7_string_formatting_new_style.py
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
Lesson 4.7 - String Formatting (New Style)
--------------------------------------------
This script demonstrates string formatting using the new-style 'str.format()' method in Python.
We will explore how to format strings with different data types.
"""

# All imports whenever be applicable comes here.

def main():
    # Let's dive into new-style string formatting with quirky examples!
    
    # Declaring variables
    name = "Alice"
    age = 25
    height = 5.6
    score = 95.5

    # Formatting strings using the 'str.format()' method
    formatted_string1 = "Name: {}".format(name)
    print(formatted_string1)

    formatted_string2 = "Age: {}".format(age)
    print(formatted_string2)

    formatted_string3 = "Height: {:.1f}".format(height)
    print(formatted_string3)

    formatted_string4 = "Score: {:.2f}".format(score)
    print(formatted_string4)

    # Formatting multiple values
    formatted_string5 = "Name: {}, Age: {}, Height: {:.1f}, Score: {:.2f}".format(name, age, height, score)
    print(formatted_string5)

    # Using named placeholders
    formatted_string6 = "Name: {n}, Age: {a}, Height: {h:.1f}, Score: {s:.2f}".format(n=name, a=age, h=height, s=score)
    print(formatted_string6)

    """
    Important Points:
    - New-style string formatting uses the 'str.format()' method with curly braces {} as placeholders.
    - Placeholders can be indexed or named, allowing for flexible and readable formatting.
    - Common format specifiers include {:.1f} for one decimal float, {:.2f} for two decimal float, etc.
    - New-style formatting is preferred over old-style '%' formatting for its readability and versatility.
    """

if __name__ == "__main__":
    main()
