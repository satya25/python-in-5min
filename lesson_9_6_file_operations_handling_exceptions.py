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
# File Name         :       lesson_9_6_file_operations_handling_exceptions.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Oct 26, 2024
# version           :       1.0
# Release           :       R1
# Dependencies      :       NONE
# Installation      :       NONE
# Usage             :       python ./src/lesson_9_6_file_operations_handling_exceptions.py
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
Lesson 9.6 - File Operations and Handling Exceptions
------------------------------------------------------
This script demonstrates how to handle exceptions during file operations in Python.
We will explore how to use try-except blocks to manage errors when working with files.
"""

# All imports whenever be applicable comes here.

def main():
    # Understanding file operations and handling exceptions with fun examples!
    
    # Handling exceptions during file reading
    try:
        with open("non_existent_file.txt", "r") as file:
            content = file.read()
        print("File content:\n", content)
    except FileNotFoundError:
        print("Error: File not found.")

    # Handling exceptions during file writing
    try:
        with open("output.txt", "w") as file:
            file.write("Hello, world!\n")
        print("Data written to 'output.txt'.")
    except IOError:
        print("Error: An IOError occurred while writing to the file.")

    # Handling multiple exceptions
    try:
        with open("another_non_existent_file.txt", "r") as file:
            content = file.read()
        print("File content:\n", content)
    except FileNotFoundError:
        print("Error: File not found.")
    except IOError:
        print("Error: An IOError occurred while reading the file.")

    """
    Important Points:
    - Exceptions can occur during file operations, such as reading from or writing to a file.
    - The try-except block is used to handle exceptions and manage errors gracefully.
    - The FileNotFoundError is raised when a file is not found.
    - The IOError is raised for input/output operations, such as file reading or writing errors.
    - Understanding how to handle exceptions is essential for robust and error-resistant file handling in Python.
    """

if __name__ == "__main__":
    main()


