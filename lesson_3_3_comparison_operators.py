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
# File Name         :       lesson_3_3_comparison_operators.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Oct 26, 2024
# version           :       1.0
# Release           :       R1
# Dependencies      :       NONE
# Installation      :       NONE
# Usage             :       python ./src/lesson_3_3_comparison_operators.py
# ----------------------------------------------------------------------------
# Credits and Acknowledgements
#
# - Special thanks to the Python community for their excellent work:
#   https://www.python.org/community/
#
# - The APIs used in this script is documented here:
#   https://docs.python.org/3/
#
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
Lesson 3.3 - Comparison Operators
----------------------------------
This script introduces comparison operators in Python.
We will explore how to compare values and use the results.
"""

# All imports whenever be applicable comes here.

def main():
    # Let's dive into the world of comparison with some quirky examples!

    # Meet Mr. Equal, Ms. Not Equal, Dr. Greater, and Professor Less
    
    # Mr. Equal (==)
    a = 5
    b = 5
    are_equal = (a == b)
    print("Are a and b equal:", are_equal)
    
    # Ms. Not Equal (!=)
    c = 7
    d = 10
    are_not_equal = (c != d)
    print("Are c and d not equal:", are_not_equal)
    
    # Dr. Greater Than (>)
    apples = 8
    bananas = 5
    more_apples = (apples > bananas)
    print("Are there more apples than bananas:", more_apples)
    
    # Professor Less Than (<)
    cats = 3
    dogs = 4
    fewer_cats = (cats < dogs)
    print("Are there fewer cats than dogs:", fewer_cats)
    
    # Greater Than or Equal To (>=)
    height_Alice = 5.5
    height_Bob = 5.5
    is_Alice_taller_or_equal = (height_Alice >= height_Bob)
    print("Is Alice as tall as or taller than Bob:", is_Alice_taller_or_equal)
    
    # Less Than or Equal To (<=)
    candies_John = 10
    candies_Jane = 12
    has_John_fewer_or_equal_candies = (candies_John <= candies_Jane)
    print("Does John have fewer or equal candies as Jane:", has_John_fewer_or_equal_candies)
    
    """
    Important Points:
    - Comparison operators include == (equal to), != (not equal to), > (greater than), < (less than), >= (greater than or equal to), and <= (less than or equal to).
    - Comparison operators are used to compare two values and return a boolean result (True or False).
    - Let's have fun comparing things in Python!
    """

if __name__ == "__main__":
    main()


