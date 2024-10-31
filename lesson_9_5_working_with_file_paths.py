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
# File Name         :       lesson_9_5_working_with_file_paths.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Oct 26, 2024
# version           :       1.0
# Release           :       R1
# Dependencies      :       NONE
# Installation      :       NONE
# Usage             :       python ./src/lesson_9_5_working_with_file_paths.py
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
Lesson 9.5 - Working with File Paths
--------------------------------------
This script demonstrates how to work with file paths in Python.
We will explore how to use the os and pathlib modules to handle file paths effectively.
"""

# All imports whenever be applicable comes here.
import os
from pathlib import Path

def main():
    # Understanding how to work with file paths with fun examples!
    
    # Using the os module to work with file paths
    current_directory = os.getcwd()
    print("Current directory using os:", current_directory)

    # Joining paths using os.path.join()
    file_path = os.path.join(current_directory, "example.txt")
    print("File path using os.path.join():", file_path)

    # Checking if a path exists using os.path.exists()
    path_exists = os.path.exists(file_path)
    print("Does the file path exist:", path_exists)

    # Using the pathlib module to work with file paths
    current_directory_pathlib = Path.cwd()
    print("Current directory using pathlib:", current_directory_pathlib)

    # Joining paths using pathlib
    file_path_pathlib = current_directory_pathlib / "example.txt"
    print("File path using pathlib:", file_path_pathlib)

    # Checking if a path exists using pathlib
    path_exists_pathlib = file_path_pathlib.exists()
    print("Does the file path exist using pathlib:", path_exists_pathlib)

    """
    Important Points:
    - The os module provides functions for interacting with the operating system and handling file paths.
    - The os.path.join() function joins one or more path components intelligently.
    - The os.path.exists() function checks if a path exists.
    - The pathlib module provides an object-oriented approach to handling file paths.
    - The Path.cwd() method gets the current working directory, and the / operator is used to join paths.
    - Understanding how to work with file paths is essential for file handling and management in Python.
    """

if __name__ == "__main__":
    main()

