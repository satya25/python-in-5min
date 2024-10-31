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
# File Name         :       lesson_5_3_comparison_and_logical_operators.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Oct 26, 2024
# version           :       1.0
# Release           :       R1
# Dependencies      :       NONE
# Installation      :       NONE
# Usage             :       python ./src/lesson_5_3_comparison_and_logical_operators.py
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
Lesson 5.3 - Comparison and Logical Operators
----------------------------------------------
This script demonstrates the use of comparison and logical operators in Python.
We will explore how to compare values and combine conditions in our code.
"""

# All imports whenever be applicable comes here.

def main():
    # Understanding comparison and logical operators with fun examples!
    
    # Comparison Operators
    a = 10
    b = 20

    # Equal to (==)
    is_equal = (a == b)
    print("Is 10 equal to 20:", is_equal)

    # Not equal to (!=)
    is_not_equal = (a != b)
    print("Is 10 not equal to 20:", is_not_equal)

    # Greater than (>)
    is_greater = (a > b)
    print("Is 10 greater than 20:", is_greater)

    # Less than (<)
    is_less = (a < b)
    print("Is 10 less than 20:", is_less)

    # Greater than or equal to (>=)
    is_greater_equal = (a >= b)
    print("Is 10 greater than or equal to 20:", is_greater_equal)

    # Less than or equal to (<=)
    is_less_equal = (a <= b)
    print("Is 10 less than or equal to 20:", is_less_equal)

    # Logical Operators
    x = True
    y = False

    # AND operator
    and_result = x and y
    print("True AND False:", and_result)

    # OR operator
    or_result = x or y
    print("True OR False:", or_result)

    # NOT operator
    not_result = not x
    print("NOT True:", not_result)

    """
    Important Points:
    - Comparison operators include == (equal to), != (not equal to), > (greater than), < (less than), >= (greater than or equal to), and <= (less than or equal to).
    - Logical operators include and, or, and not.
    - Comparison operators are used to compare values and return a boolean result (True or False).
    - Logical operators are used to combine multiple conditions and return a boolean result.
    - Understanding these operators helps in making complex decisions and controlling the flow of a program.
    """

if __name__ == "__main__":
    main()


