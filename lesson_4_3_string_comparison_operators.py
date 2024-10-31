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
# File Name         :       lesson_4_3_string_comparison_operators.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Oct 26, 2024
# version           :       1.0
# Release           :       R1
# Dependencies      :       NONE
# Installation      :       NONE
# Usage             :       python ./src/lesson_4_3_string_comparison_operators.py
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
Lesson 4.3 - String Comparison Operators
-----------------------------------------
This script demonstrates how to compare strings in Python using comparison operators.
We will explore equality, inequality, and other comparison operations with strings.
"""

# All imports whenever be applicable comes here.

def main():
    # Let's compare strings with some fun examples!
    
    # Declaring string variables
    string1 = "apple"
    string2 = "banana"
    string3 = "apple"
    string4 = "Apple"

    # Equality (==)
    are_equal = (string1 == string3)
    print("Are 'apple' and 'apple' equal:", are_equal)
    
    # Inequality (!=)
    are_not_equal = (string1 != string2)
    print("Are 'apple' and 'banana' not equal:", are_not_equal)
    
    # Greater than (>)
    is_greater = (string2 > string1)
    print("Is 'banana' greater than 'apple':", is_greater)
    
    # Less than (<)
    is_less = (string1 < string2)
    print("Is 'apple' less than 'banana':", is_less)
    
    # Greater than or equal to (>=)
    is_greater_equal = (string1 >= string4)
    print("Is 'apple' greater than or equal to 'Apple':", is_greater_equal)
    
    # Less than or equal to (<=)
    is_less_equal = (string1 <= string3)
    print("Is 'apple' less than or equal to 'apple':", is_less_equal)
    
    # Case sensitivity
    case_sensitive_compare = (string1 == string4)
    print("Is 'apple' equal to 'Apple' (case-sensitive):", case_sensitive_compare)
    
    """
    Important Points:
    - Comparison operators can be used with strings to check for equality, inequality, and order.
    - Strings are compared based on their Unicode values.
    - Comparisons are case-sensitive; 'apple' is different from 'Apple'.
    - Understanding string comparisons is useful for sorting, searching, and conditional logic.
    """

if __name__ == "__main__":
    main()


