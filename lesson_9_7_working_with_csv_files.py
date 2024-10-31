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
# File Name         :       lesson_9_7_working_with_csv_files.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Oct 26, 2024
# version           :       1.0
# Release           :       R1
# Dependencies      :       NONE
# Installation      :       NONE
# Usage             :       python ./src/lesson_9_7_working_with_csv_files.py
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
Lesson 9.7 - Working with CSV Files
-------------------------------------
This script demonstrates how to work with CSV files in Python.
We will explore how to read from and write to CSV files using the csv module.
"""

# All imports whenever be applicable comes here.
import csv

def main():
    # Understanding how to work with CSV files with fun examples!
    
    # Writing to a CSV file
    with open("example.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Age", "City"])
        writer.writerow(["Alice", 30, "New York"])
        writer.writerow(["Bob", 25, "San Francisco"])
        writer.writerow(["Charlie", 35, "Chicago"])
        print("Data written to 'example.csv'.")

    # Reading from a CSV file
    with open("example.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print("Row:", row)

    # Writing to a CSV file using DictWriter
    with open("example_dict.csv", "w", newline='') as file:
        fieldnames = ["Name", "Age", "City"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({"Name": "Alice", "Age": 30, "City": "New York"})
        writer.writerow({"Name": "Bob", "Age": 25, "City": "San Francisco"})
        writer.writerow({"Name": "Charlie", "Age": 35, "City": "Chicago"})
        print("Data written to 'example_dict.csv'.")

    # Reading from a CSV file using DictReader
    with open("example_dict.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print("Row:", row)

    """
    Important Points:
    - The csv module provides functions and classes to work with CSV files.
    - The writer and DictWriter classes are used to write data to CSV files.
    - The reader and DictReader classes are used to read data from CSV files.
    - Using newline='' with open() is important for compatibility with different CSV formats.
    - Understanding how to work with CSV files is essential for data storage and exchange in Python.
    """

if __name__ == "__main__":
    main()



