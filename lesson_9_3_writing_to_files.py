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
# File Name         :       lesson_9_3_writing_to_files.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Oct 26, 2024
# version           :       1.0
# Release           :       R1
# Dependencies      :       NONE
# Installation      :       NONE
# Usage             :       python ./src/lesson_9_3_writing_to_files.py
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
Lesson 9.3 - Writing to Files
-------------------------------
This script demonstrates how to write data to files in Python.
We will explore different methods for writing data to files, including writing text and appending to files.
"""

# All imports whenever be applicable comes here.

def main():
    # Understanding how to write data to files with fun examples!
    
    # Writing text to a file
    with open("output.txt", "w") as file:
        file.write("Hello, world!\n")
        file.write("Welcome to file handling in Python.\n")
        print("Data written to 'output.txt'.")

    # Appending text to a file
    with open("output.txt", "a") as file:
        file.write("This line is appended to the file.\n")
        print("Data appended to 'output.txt'.")

    # Writing a list of lines to a file
    lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
    with open("lines.txt", "w") as file:
        file.writelines(lines)
        print("List of lines written to 'lines.txt'.")

    """
    Important Points:
    - The write() method writes a string to a file.
    - The writelines() method writes a list of strings to a file.
    - Opening a file in 'a' (append) mode allows adding data to the end of the file without overwriting it.
    - Using with open() ensures that the file is properly closed after its suite finishes.
    - Understanding how to write to files is essential for data storage and logging in Python.
    """

if __name__ == "__main__":
    main()



