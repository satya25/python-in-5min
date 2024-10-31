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
# File Name         :       lesson_5_6_loop_control_statements.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Oct 26, 2024
# version           :       1.0
# Release           :       R1
# Dependencies      :       NONE
# Installation      :       NONE
# Usage             :       python ./src/lesson_5_6_loop_control_statements.py
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
Lesson 5.6 - Loop Control Statements
-------------------------------------
This script demonstrates the use of loop control statements in Python.
We will explore how to use break, continue, and pass statements to control the flow of loops.
"""

# All imports whenever be applicable comes here.

def main():
    # Understanding loop control statements with fun examples!
    
    # Using the break statement
    print("Break statement example:")
    for number in range(1, 10):
        if number == 5:
            print("Breaking the loop at number:", number)
            break
        print("Number:", number)

    # Using the continue statement
    print("\nContinue statement example:")
    for number in range(1, 10):
        if number == 5:
            print("Skipping number:", number)
            continue
        print("Number:", number)

    # Using the pass statement
    print("\nPass statement example:")
    for number in range(1, 10):
        if number == 5:
            pass  # Pass is a null operation; nothing happens here
        print("Number:", number)

    """
    Important Points:
    - The break statement exits the loop prematurely when a specified condition is met.
    - The continue statement skips the rest of the current loop iteration and moves to the next iteration.
    - The pass statement is a null operation; it does nothing and is used as a placeholder.
    - Loop control statements provide additional ways to control the flow of loops and handle specific situations.
    """

if __name__ == "__main__":
    main()
