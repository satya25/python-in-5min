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
# File Name         :       lesson_11_4_create_your_own_module.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Oct 26, 2024
# version           :       1.0
# Release           :       R1
# Dependencies      :       mymathmodule.py
# Installation      :       NONE
# Usage             :       python ./src/lesson_11_4_create_your_own_module.py
# ----------------------------------------------------------------------------
# Credits and Acknowledgements
# - Special thanks to the Python community for their excellent work:
#   https://www.python.org/community/
# - The APIs used in this script is documented here:
#   https://docs.python.org/3/
# - Code Snippet(s) adapted from    :   -- NOT Applicable --
# - Dataset(s) sourced from         :   -- NOT Applicable --
# - Inspiration drawn from          :   -- NOT Applicable --

# Thank you to the creators and maintainers of these resources!
# ----------------------------------------------------------------------------
# - Content Removal Requests
#   If you are the owner or creator of any content used in this script and
#   would like it to be removed, please contact me at: spnigam25@yahoo.com
#   I will promptly remove the content upon request.
# ----------------------------------------------------------------------------

"""
Lesson 11.4 - Create Your Own Module
--------------------------------------
This script demonstrates how to create and use a custom module in Python.
We will create a module with custom functions for mathematical operations and use it in this script.
"""

# Importing the custom module
import mymathmodule

def main():
    # Using the factorial function from the custom module
    print("Factorial of 5:", mymathmodule.factorial(5))
    
    # Using the arithmetic progression sum function from the custom module
    print("Sum of first 5 terms of AP with first term 2 and common difference 3:", mymathmodule.arithmetic_progression_sum(2, 3, 5))
    
    # Using the simple interest function from the custom module
    print("Simple interest for principal 1000, rate 5%, and time 2 years:", mymathmodule.simple_interest(1000, 5, 2))

    """
    Important Points:
    - Creating a custom module involves saving the code in a separate file with a .py extension.
    - Importing the custom module allows using its functions and classes in other programs.
    - Using custom modules helps in organizing code, making it reusable and easier to maintain.
    - Understanding how to create and use custom modules is essential for writing modular and scalable code in Python.
    """

if __name__ == "__main__":
    main()

