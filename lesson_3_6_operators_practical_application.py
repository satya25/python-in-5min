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
# File Name         :       lesson_3_6_operators_practical_application.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Oct 26, 2024
# version           :       1.0
# Release           :       R1
# Dependencies      :       NONE
# Installation      :       NONE
# Usage             :       python ./src/lesson_3_6_operators_practical_application.py
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
Lesson 3.6 - Practical Application of Operators
------------------------------------------------
This script demonstrates the practical application of operators in Python.
We will explore how to use different operators in real-world scenarios.
"""

# All imports whenever be applicable comes here.

def main():
    # Let's dive into some practical examples with a touch of humor!

    # Example 1: Calculating the total cost of a shopping cart
    apple_price = 0.5  # price per apple in dollars
    banana_price = 0.3  # price per banana in dollars
    apple_count = 10  # number of apples
    banana_count = 6  # number of bananas

    total_cost = (apple_price * apple_count) + (banana_price * banana_count)
    print("Total cost of the shopping cart:", total_cost)

    # Example 2: Checking if we have enough budget to buy items
    budget = 10  # total budget in dollars
    can_afford = total_cost <= budget
    print("Can we afford the items in the shopping cart:", can_afford)

    # Example 3: Calculating the area of a circle
    radius = 5  # radius of the circle in meters
    pi = 3.14159
    area = pi * (radius ** 2)
    print("Area of the circle:", area)

    # Example 4: Determining if a number is even or odd
    number = 17  # any integer number
    is_even = (number % 2) == 0
    print("Is the number even:", is_even)

    # Example 5: Logical operations to check conditions
    is_sunny = True
    has_sunglasses = False
    go_for_walk = is_sunny and has_sunglasses
    print("Can we go for a walk:", go_for_walk)

    """
    Important Points:
    - Operators can be used in practical applications like calculating costs, areas, and checking conditions.
    - Arithmetic operators help in performing mathematical calculations.
    - Comparison operators help in making decisions based on numerical comparisons.
    - Logical operators help in combining multiple conditions for decision making.
    - Let's make learning Python practical and enjoyable!
    """

if __name__ == "__main__":
    main()


