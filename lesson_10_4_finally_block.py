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
# File Name         :       lesson_10_4_finally_block.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Oct 26, 2024
# version           :       1.0
# Release           :       R1
# Dependencies      :       NONE
# Installation      :       NONE
# Usage             :       python ./src/lesson_10_4_finally_block.py
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
Lesson 10.4 - Finally Block
-----------------------------
This script demonstrates how to use the finally block in Python to ensure code execution.
We will explore how to use the finally block to clean up resources and handle exceptions.
"""

# All imports whenever be applicable comes here.

def main():
    # Understanding the finally block with fun examples!
    
    # Example 1: Using the finally block to clean up resources
    try:
        file = open("example_finally.txt", "w")
        file.write("This file is managed using the finally block.\n")
        file.write("Ensuring resources are released properly.\n")
        print("Data written to 'example_finally.txt'.")
    except IOError as e:
        print(f"Error: {e}")
    finally:
        file.close()
        print("File closed using the finally block.")

    # Example 2: Using the finally block to clean up resources after an exception
    try:
        file = open("example_finally_exception.txt", "w")
        file.write("This file will trigger an exception.\n")
        file.write("Attempting to divide by zero.\n")
        result = 10 / 0
    except ZeroDivisionError as e:
        print(f"Error: {e}")
    finally:
        file.close()
        print("File closed using the finally block after an exception.")

    """
    Important Points:
    - The finally block is used to ensure that code is executed, regardless of whether an exception occurs or not.
    - The finally block is commonly used for cleaning up resources, such as closing files or releasing network connections.
    - The finally block is always executed after the try and except blocks, even if an exception occurs.
    - Using the finally block helps in writing robust and error-resistant code by ensuring proper resource management.
    """

if __name__ == "__main__":
    main()


