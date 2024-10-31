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
# File Name         :       lesson_3_5_operator_precedence.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Oct 26, 2024
# version           :       1.0
# Release           :       R1
# Dependencies      :       NONE
# Installation      :       NONE
# Usage             :       python ./src/lesson_3_5_operator_precedence.py
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
Lesson 3.5 - Operator Precedence
---------------------------------
This script explains operator precedence in Python.
We will explore how different operators are evaluated in expressions.
"""

# All imports whenever be applicable comes here.

def main():
    # Understanding operator precedence with some whimsical examples!
    
    # Let's meet some characters in the world of operators:
    # Meet Mr. Parentheses, Ms. Exponent, Dr. Multiplication, Professor Division, Teacher Addition, and Sergeant Subtraction
    
    # Mr. Parentheses (())
    expression1 = (2 + 3) * 4
    print("Result with Parentheses:", expression1)  # Parentheses first
    
    # Ms. Exponent (**)
    expression2 = 2 ** 3 + 1
    print("Result with Exponentiation:", expression2)  # Exponentiation second
    
    # Dr. Multiplication (*)
    expression3 = 2 + 3 * 4
    print("Result with Multiplication:", expression3)  # Multiplication third
    
    # Professor Division (/)
    expression4 = 10 / 2 + 5
    print("Result with Division:", expression4)  # Division third
    
    # Teacher Addition (+)
    expression5 = 2 + 3 - 4
    print("Result with Addition and Subtraction:", expression5)  # Addition and Subtraction fourth
    
    # Sergeant Subtraction (-)
    expression6 = 10 - 5 + 2
    print("Another Result with Addition and Subtraction:", expression6)  # Subtraction and Addition fourth
    
    # Combining multiple operators
    complex_expression = (2 + 3) * 4 ** 2 / 8 - 3
    print("Complex Expression Result:", complex_expression)  # Following operator precedence
    
    """
    Important Points:
    - Operator precedence determines the order in which operators are evaluated in an expression.
    - Parentheses have the highest precedence and can be used to change the order of evaluation.
    - Exponentiation (**), Multiplication (*), Division (/), Addition (+), and Subtraction (-) follow in that order.
    - Understanding operator precedence helps in writing correct and predictable expressions.
    """

if __name__ == "__main__":
    main()


