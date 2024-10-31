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
# File Name         :       lesson_4_6_string_formatting_old_style.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Oct 26, 2024
# version           :       1.0
# Release           :       R1
# Dependencies      :       NONE
# Installation      :       NONE
# Usage             :       python ./src/lesson_4_6_string_formatting_old_style.py
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
Lesson 4.6 - String Formatting (Old Style)
--------------------------------------------
This script demonstrates string formatting using the old-style '%' operator in Python.
We will explore how to format strings with different data types.
"""

# All imports whenever be applicable comes here.

def main():
    # Let's dive into old-style string formatting with quirky examples!
    
    # Declaring variables
    name = "Alice"
    age = 25
    height = 5.6
    score = 95.5

    # Formatting strings using the '%' operator
    formatted_string1 = "Name: %s" % name
    print(formatted_string1)

    formatted_string2 = "Age: %d" % age
    print(formatted_string2)

    formatted_string3 = "Height: %.1f" % height
    print(formatted_string3)

    formatted_string4 = "Score: %.2f" % score
    print(formatted_string4)

    # Formatting multiple values
    formatted_string5 = "Name: %s, Age: %d, Height: %.1f, Score: %.2f" % (name, age, height, score)
    print(formatted_string5)

    """
    Important Points:
    - Old-style string formatting uses the '%' operator followed by format specifiers.
    - Common format specifiers include %s for strings, %d for integers, and %f for floating-point numbers.
    - Old-style formatting is still supported in Python but newer methods like str.format() and f-strings are preferred.
    """

if __name__ == "__main__":
    main()


