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
# File Name         :       lesson_9_4_file_modes.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Oct 26, 2024
# version           :       1.0
# Release           :       R1
# Dependencies      :       NONE
# Installation      :       NONE
# Usage             :       python ./src/lesson_9_4_file_modes.py
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
Lesson 9.4 - File Modes
-------------------------
This script demonstrates the different file modes available in Python for reading and writing files.
We will explore modes like read ('r'), write ('w'), append ('a'), and binary ('b') modes.
"""

# All imports whenever be applicable comes here.

def main():
    # Understanding file modes with fun examples!
    
    # Writing to a file in write mode ('w')
    with open("example_write.txt", "w") as file:
        file.write("This file is created in write mode.\n")
        print("Data written to 'example_write.txt' in write mode.")

    # Appending to a file in append mode ('a')
    with open("example_append.txt", "a") as file:
        file.write("This line is appended to the file.\n")
        print("Data appended to 'example_append.txt' in append mode.")

    # Reading from a file in read mode ('r')
    with open("example_write.txt", "r") as file:
        content = file.read()
        print("Data read from 'example_write.txt' in read mode:\n", content)

    # Writing to a file in binary write mode ('wb')
    with open("example_binary_write.bin", "wb") as file:
        file.write(b"This is binary data.\n")
        print("Binary data written to 'example_binary_write.bin' in binary write mode.")

    # Reading from a file in binary read mode ('rb')
    with open("example_binary_write.bin", "rb") as file:
        binary_content = file.read()
        print("Binary data read from 'example_binary_write.bin' in binary read mode:\n", binary_content)

    """
    Important Points:
    - File modes determine how a file is opened and how data can be read from or written to the file.
    - Common file modes include read ('r'), write ('w'), append ('a'), binary read ('rb'), and binary write ('wb').
    - Write mode ('w') creates a new file or overwrites an existing file.
    - Append mode ('a') adds data to the end of the file without overwriting it.
    - Binary modes ('rb' and 'wb') are used for reading and writing binary data.
    - Understanding file modes is essential for proper file handling in Python.
    """

if __name__ == "__main__":
    main()


