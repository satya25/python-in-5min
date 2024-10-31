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
# File Name         :       lesson_9_9_context_managers.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Oct 26, 2024
# version           :       1.0
# Release           :       R1
# Dependencies      :       NONE
# Installation      :       NONE
# Usage             :       python ./src/lesson_9_9_context_managers.py
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
Lesson 9.9 - Context Managers and try...finally
-------------------------------------------------
This script introduces the concept of context managers in Python and demonstrates how to use the with statement and the try...finally approach to manage resources such as files.
"""

# All imports whenever be applicable comes here.

def main():
    # Understanding context managers with fun examples!
    
    # Using the with statement to open a file
    with open("example.txt", "w") as file:
        file.write("Hello, world!\n")
        file.write("Welcome to the context managers in Python.\n")
        print("Data written to 'example.txt' using context manager.")

    # Reading from the file using the with statement
    with open("example.txt", "r") as file:
        content = file.read()
        print("Data read from 'example.txt' using context manager:\n", content)

    # Using try...finally to manage file resources
    file = open("example_finally.txt", "w")
    try:
        file.write("This file is managed using try...finally.\n")
        file.write("Ensuring resources are released properly.\n")
        print("Data written to 'example_finally.txt' using try...finally.")
    finally:
        file.close()
        print("File closed using try...finally.")

    """
    Important Points:
    - Context managers are used to manage resources, ensuring they are properly acquired and released.
    - The with statement is used to create a context manager, which automatically handles resource management.
    - The try...finally approach ensures that resources are properly closed or released after their use, even if an error occurs.
    - Common use cases for context managers and try...finally include file handling, network connections, and database connections.
    - Understanding context managers and try...finally is essential for efficient and error-resistant resource management in Python.
    """

if __name__ == "__main__":
    main()


