#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This file is part of aialchemyhub_in (https://github.com/satya25/aialchemyhub_in).
aialchemyhub_in is free software repository: You can redistribute it and/or modify it 
under the terms of the MIT License. aialchemyhub_in is distributed in the hope that 
it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of 
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. 
See the MIT License for more details. You should have received a copy of the MIT 
License along with aialchemyhub_in. If not, see <https://opensource.org/licenses/MIT>.
"""
# ----------------------------------------------------------------------------
# File Name         :       lesson_12_9_special_methods_operator_overloading.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Nov 03, 2024
# version           :       1.0
# Release           :       R1
# Dependencies      :       None
# Installation      :       NONE
# Usage             :       python ./src/lesson_12_9_special_methods_operator_overloading.py
# ----------------------------------------------------------------------------
# Credits and Acknowledgements
# - Special thanks to the Python community for their excellent work:
#   https://www.python.org/community/
# - The APIs used in this script are documented here:
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
Lesson 12.9 - Special Methods and Operator Overloading
------------------------------------------------------
This script introduces special methods in Python (e.g., __str__, __repr__, __add__).
We will implement operator overloading and provide practical examples and use cases.
"""

# Defining a class
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Special method __str__ for string representation
    def __str__(self):
        return f"Point({self.x}, {self.y})"

    # Special method __repr__ for detailed representation
    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    # Special method __add__ for adding two Point objects
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

def main():
    # Creating instances (objects) of the Point class
    point1 = Point(2, 3)
    point2 = Point(5, 7)

    # Using special methods
    print(point1)                # Output: Point(2, 3) - calls __str__
    print(repr(point2))          # Output: Point(5, 7) - calls __repr__

    # Operator overloading using __add__
    point3 = point1 + point2
    print(point3)                # Output: Point(7, 10)

if __name__ == "__main__":
    main()

