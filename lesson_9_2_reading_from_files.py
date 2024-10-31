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
# File Name         :       lesson_9_2_reading_from_files.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Oct 26, 2024
# version           :       1.0
# Release           :       R1
# Dependencies      :       NONE
# Installation      :       NONE
# Usage             :       python ./src/lesson_9_2_reading_from_files.py
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
Lesson 9.2 - Reading from Files
---------------------------------
This script demonstrates how to read data from files in Python.
We will explore different methods for reading files, including reading the entire file, reading line by line, and reading into a list.
"""

# All imports whenever be applicable comes here.

def main():
    # Understanding how to read data from files with fun examples!
    
    # Creating a sample file for reading
    with open("example.txt", "w") as file:
        file.write("Hello, world!\n")
        file.write("Welcome to file handling in Python.\n")
        file.write("Let's read from this file.\n")
    print("Sample file 'example.txt' created for reading.")

    # Reading the entire file
    with open("example.txt", "r") as file:
        content = file.read()
    print("Reading entire file content:\n", content)

    # Reading the file line by line
    print("Reading file line by line:")
    with open("example.txt", "r") as file:
        for line in file:
            print(line, end='')

    # Reading file lines into a list
    with open("example.txt", "r") as file:
        lines = file.readlines()
    print("\nReading file lines into a list:", lines)

    """
    Important Points:
    - The read() method reads the entire content of a file as a single string.
    - The readline() method reads one line from the file at a time.
    - The readlines() method reads all lines of a file and returns them as a list of strings.
    - Using with open() ensures that the file is properly closed after its suite finishes.
    - Understanding how to read from files is essential for data processing and analysis in Python.
    """

if __name__ == "__main__":
    main()


