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
# File Name         :       lesson_3_4_logical_operators.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Oct 26, 2024
# version           :       1.0
# Release           :       R1
# Dependencies      :       NONE
# Installation      :       NONE
# Usage             :       python ./src/lesson_3_4_logical_operators.py
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
Lesson 3.4 - Logical Operators
-------------------------------
This script introduces logical operators in Python.
We will learn how to use logical operators to combine conditional statements.
"""

# All imports whenever be applicable comes here.

def main():
    # Let's explore logical operators with some whimsical examples!

    # Meet Mr. AND, Ms. OR, and Dr. NOT
    
    # Mr. AND (and)
    x = True
    y = False
    and_result = x and y
    print("Mr. AND's result:", and_result)  # Both conditions need to be True
    
    # Ms. OR (or)
    a = True
    b = False
    or_result = a or b
    print("Ms. OR's result:", or_result)  # At least one condition needs to be True
    
    # Dr. NOT (not)
    is_sunny = True
    not_result = not is_sunny
    print("Dr. NOT's result:", not_result)  # Inverts the boolean value
    
    # Combining logical operators
    has_umbrella = True
    is_raining = True
    can_go_outside = (is_sunny or has_umbrella) and not is_raining
    print("Can go outside:", can_go_outside)  # Combining multiple conditions
    
    """
    Important Points:
    - Logical operators include and, or, and not.
    - The and operator returns True if both conditions are True.
    - The or operator returns True if at least one condition is True.
    - The not operator inverts the boolean value.
    - Logical operators are useful for combining multiple conditions in decision making.
    """

if __name__ == "__main__":
    main()


