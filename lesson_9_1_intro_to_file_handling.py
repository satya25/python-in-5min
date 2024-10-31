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
# File Name         :       lesson_9_1_intro_to_file_handling.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Oct 26, 2024
# version           :       1.0
# Release           :       R1
# Dependencies      :       NONE
# Installation      :       NONE
# Usage             :       python ./src/lesson_9_1_intro_to_file_handling.py
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
Lesson 9.1 - Introduction to File Handling
--------------------------------------------
This script introduces the concept of file handling in Python.
We will explore how to open, read, write, and close files.
"""

# All imports whenever be applicable comes here.

def main():
    # Understanding file handling with fun examples!
    
    # Opening a file
    file = open("example.txt", "w")
    print("File opened successfully for writing.")

    # Writing to the file
    file.write("Hello, world!\n")
    file.write("Welcome to file handling in Python.\n")
    print("Data written to the file.")

    # Closing the file
    file.close()
    print("File closed successfully.")

    # Reopening the file for reading
    file = open("example.txt", "r")
    print("File opened successfully for reading.")

    # Reading the file content
    content = file.read()
    print("File content:\n", content)

    # Closing the file
    file.close()
    print("File closed successfully.")

    """
    Important Points:
    - File handling allows you to work with files to store and retrieve data.
    - The open() function is used to open a file, with the mode ('w' for write, 'r' for read, etc.) specified.
    - The write() method is used to write data to a file.
    - The read() method is used to read the entire content of a file.
    - The close() method is used to close the file, ensuring all resources are released.
    - Understanding file handling is essential for managing data storage and retrieval in Python.
    """

if __name__ == "__main__":
    main()


