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
# File Name         :       lesson_3_2_arithmetic_operators.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Oct 26, 2024
# version           :       1.0
# Release           :       R1
# Dependencies      :       NONE
# Installation      :       NONE
# Usage             :       python ./src/lesson_3_2_arithmetic_operators.py
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
Lesson 3.2 - Arithmetic Operators
----------------------------------
This script introduces arithmetic operators in Python.
We will explore how to perform basic mathematical operations.
"""

# All imports whenever be applicable comes here.

def main():
    # Let's have some fun with numbers and operators!
    
    # Arithmetic Operators
    # Meet Mr. Addition, Ms. Subtraction, Dr. Multiplication, and Professor Division
    
    # Mr. Addition
    apples = 10
    bananas = 5
    total_fruits = apples + bananas
    print("Total fruits:", total_fruits)
    
    # Ms. Subtraction
    chocolates = 20
    chocolates_eaten = 5
    chocolates_left = chocolates - chocolates_eaten
    print("Chocolates left:", chocolates_left)
    
    # Dr. Multiplication
    cookies_per_box = 4
    boxes = 5
    total_cookies = cookies_per_box * boxes
    print("Total cookies:", total_cookies)
    
    # Professor Division
    total_money = 50
    number_of_friends = 5
    money_per_friend = total_money / number_of_friends
    print("Money per friend:", money_per_friend)
    
    # Modulus (Remainder)
    total_minutes = 130
    minutes_per_hour = 60
    remaining_minutes = total_minutes % minutes_per_hour
    print("Remaining minutes:", remaining_minutes)
    
    # Exponentiation (Power)
    base = 2
    exponent = 3
    power_result = base ** exponent
    print("2 to the power of 3:", power_result)
    
    # Floor Division (Quotient)
    total_pages = 101
    pages_per_chapter = 20
    full_chapters = total_pages // pages_per_chapter
    print("Full chapters:", full_chapters)
    
    """
    Important Points:
    - Arithmetic operators include + (addition), - (subtraction), * (multiplication), / (division), % (modulus), ** (exponentiation), and // (floor division).
    - Arithmetic operators can perform basic mathematical operations and solve real-world problems.
    - Let's make learning Python as delightful as a box of cookies!
    """

if __name__ == "__main__":
    main()
