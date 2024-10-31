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
# File Name         :       lesson_9_8_working_with_json_files.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Oct 26, 2024
# version           :       1.0
# Release           :       R1
# Dependencies      :       NONE
# Installation      :       NONE
# Usage             :       python ./src/lesson_9_8_working_with_json_files.py
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
Lesson 9.8 - Working with JSON Files
--------------------------------------
This script demonstrates how to work with JSON files in Python.
We will explore how to read from and write to JSON files using the json module.
"""

# All imports whenever be applicable comes here.
import json

def main():
    # Understanding how to work with JSON files with fun examples!
    
    # Creating a dictionary to be converted to JSON
    data = {
        "name": "Alice",
        "age": 30,
        "city": "New York",
        "is_student": False,
        "courses": ["Math", "Science", "History"]
    }
    print("Original data dictionary:", data)

    # Writing the dictionary to a JSON file
    with open("example.json", "w") as file:
        json.dump(data, file, indent=4)
        print("Data written to 'example.json'.")

    # Reading from the JSON file
    with open("example.json", "r") as file:
        loaded_data = json.load(file)
        print("Data read from 'example.json':", loaded_data)

    # Converting a dictionary to a JSON string
    json_string = json.dumps(data, indent=4)
    print("Data converted to JSON string:\n", json_string)

    # Converting a JSON string back to a dictionary
    converted_data = json.loads(json_string)
    print("JSON string converted back to dictionary:", converted_data)

    """
    Important Points:
    - The json module provides functions to work with JSON data.
    - The dump() and dumps() methods are used to write data to a JSON file and convert data to a JSON string, respectively.
    - The load() and loads() methods are used to read data from a JSON file and convert a JSON string to a dictionary, respectively.
    - JSON (JavaScript Object Notation) is a popular data interchange format used for storing and exchanging data.
    - Understanding how to work with JSON files is essential for data storage and communication in Python.
    """

if __name__ == "__main__":
    main()


