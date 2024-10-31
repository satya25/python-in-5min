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
# File Name         :       lesson_5_5_while_loops.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Oct 26, 2024
# version           :       1.0
# Release           :       R1
# Dependencies      :       NONE
# Installation      :       NONE
# Usage             :       python ./src/lesson_5_5_while_loops.py
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
Lesson 5.5 - While Loops
--------------------------
This script demonstrates the use of while loops in Python.
We will explore how to repeat a block of code as long as a condition is true.
"""

# All imports whenever be applicable comes here.

def main():
    # Understanding while loops with fun examples!
    
    # While loop to print numbers from 1 to 5
    count = 1
    while count <= 5:
        print("Count is:", count)
        count += 1  # Incrementing the counter

    # Using a while loop to sum numbers from 1 to 10
    total = 0
    number = 1
    while number <= 10:
        total += number
        number += 1
    print("Sum of numbers from 1 to 10 is:", total)

    # Using a while loop with a condition
    temperature = 25
    while temperature > 20:
        print("Temperature is:", temperature)
        temperature -= 1  # Decreasing the temperature

    """
    Important Points:
    - While loops repeat a block of code as long as a condition is true.
    - The condition is checked before each iteration, and the loop terminates when the condition becomes false.
    - Ensure that the loop condition will eventually become false to avoid infinite loops.
    - While loops are useful for repeating tasks with unknown or variable repetition counts.
    """

if __name__ == "__main__":
    main()

