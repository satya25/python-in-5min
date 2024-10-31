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
# File Name         :       lesson_10_5_else_clause.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Oct 26, 2024
# version           :       1.0
# Release           :       R1
# Dependencies      :       NONE
# Installation      :       NONE
# Usage             :       python ./src/lesson_10_5_else_clause.py
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
Lesson 10.5 - Else Clause in Try-Except Blocks
------------------------------------------------
This script demonstrates how to use the else clause in try-except blocks in Python.
We will explore how to execute code when no exceptions occur.
"""

# All imports whenever be applicable comes here.

def main():
    # Understanding the else clause in try-except blocks with fun examples!
    
    # Example 1: Using the else clause when no exceptions occur
    try:
        result = 10 / 2
    except ZeroDivisionError as e:
        print(f"Error: {e}")
    else:
        print(f"Result: {result}")

    # Example 2: Using the else clause with file operations
    try:
        with open("example_else.txt", "w") as file:
            file.write("This file is managed using the else clause.\n")
            file.write("Ensuring code runs when no exceptions occur.\n")
            print("Data written to 'example_else.txt'.")
    except IOError as e:
        print(f"Error: {e}")
    else:
        print("File written successfully without any errors.")

    """
    Important Points:
    - The else clause in a try-except block is executed if no exceptions occur in the try block.
    - The else clause allows for cleaner and more readable code by separating the exception handling from the normal execution flow.
    - The else clause is optional and can be used for code that should only run when no exceptions occur.
    - Understanding the else clause helps in writing robust and error-resistant code in Python.
    """

if __name__ == "__main__":
    main()


