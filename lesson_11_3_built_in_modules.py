#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" 
This file is part of aialchemyhub_in
(https://github.com/satya25/aialchemyhub_in).
aialchemyhub_in is free software repository:
You can redistribute it and/or modify it under the terms of the MIT License.
aialchemyhub_in is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the MIT License for more details.
You should have received a copy of the MIT License along with aialchemyhub_in.
If not, see <https://opensource.org/licenses/MIT>.
"""

# ----------------------------------------------------------------------------
# File Name         :       lesson_11_3_built_in_modules.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Oct 26, 2024
# version           :       1.0
# Release           :       R1
# Dependencies      :       NONE
# Installation      :       NONE
# Usage             :       python ./src/lesson_11_3_built_in_modules.py
# ----------------------------------------------------------------------------
# Credits and Acknowledgements
# - Special thanks to the Python community for their excellent work:
#   https://www.python.org/community/
# - The APIs used in this script are documented here:
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
Lesson 11.3 - Built-in Modules
---------------------------------
This script demonstrates how to use some of the most commonly used built-in modules in Python.
We will explore modules like math, datetime, os, sys, and random.
"""

# Importing commonly used built-in modules
import math
import datetime
import os
import sys
import random

def main():
    # Using the math module for mathematical operations
    print("Math module:")
    print(f"Square root of 16: {math.sqrt(16)}")
    print(f"Factorial of 5: {math.factorial(5)}")
    print(f"Value of pi: {math.pi}")

    # Using the datetime module for date and time operations
    print("\nDatetime module:")
    now = datetime.datetime.now()
    print(f"Current date and time: {now}")
    today = datetime.date.today()
    print(f"Today's date: {today}")
    print(f"Current year: {now.year}")
    print(f"Current month: {now.month}")
    print(f"Current day: {now.day}")

    # Using the os module for operating system-related operations
    print("\nOS module:")
    current_directory = os.getcwd()
    print(f"Current directory: {current_directory}")
    files_in_directory = os.listdir()
    print(f"Files in current directory: {files_in_directory}")

    # Using the sys module for system-related operations
    print("\nSys module:")
    print(f"Python version: {sys.version}")
    print(f"Command-line arguments: {sys.argv}")
    print(f"Platform: {sys.platform}")
    
    # Using the random module
    print("\nRandom module:")
    random_number = random.randint(1, 10)
    print(f"Random number between 1 and 10: {random_number}")
    
    print(f"Random choice from a list: {random.choice(['apple', 'banana', 'cherry'])}")
 
    """
    Important Points:
    - The math module provides mathematical functions like sqrt() and factorial().
    - The datetime module provides functions to work with dates and times.
    - The os module provides functions to interact with the operating system.
    - The sys module provides functions and variables to manipulate the Python runtime environment.
    - The random module provides functions to generate random numbers and make random choices.
    - Understanding built-in modules is essential for leveraging Python's standard library
   """

if __name__ == "__main__":
    main()