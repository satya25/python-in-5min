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
# File Name         :       lesson_8_4_iterating_over_dictionaries.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Oct 26, 2024
# version           :       1.0
# Release           :       R1
# Dependencies      :       NONE
# Installation      :       NONE
# Usage             :       python ./src/lesson_8_4_iterating_over_dictionaries.py
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
Lesson 8.4 - Iterating Over Dictionaries
------------------------------------------
This script demonstrates how to iterate over dictionaries in Python.
We will explore different methods for looping through dictionary keys, values, and key-value pairs.
"""

# All imports whenever be applicable comes here.

def main():
    # Understanding how to iterate over dictionaries with fun examples!
    
    # Creating a dictionary of fruits and their prices
    fruit_prices = {
        "apple": 0.5,
        "banana": 0.3,
        "cherry": 1.0
    }
    print("Dictionary of fruit prices:", fruit_prices)

    # Iterating over dictionary keys
    print("Iterating over keys:")
    for key in fruit_prices.keys():
        print("Key:", key)

    # Iterating over dictionary values
    print("Iterating over values:")
    for value in fruit_prices.values():
        print("Value:", value)

    # Iterating over dictionary key-value pairs
    print("Iterating over key-value pairs:")
    for key, value in fruit_prices.items():
        print(f"Key: {key}, Value: {value}")

    # Iterating and modifying values
    print("Iterating and modifying values:")
    for key in fruit_prices.keys():
        fruit_prices[key] *= 1.1  # Increase prices by 10%
    print("Modified dictionary of fruit prices:", fruit_prices)

    """
    Important Points:
    - Iterating over dictionaries allows accessing keys, values, and key-value pairs.
    - The keys() method returns all keys, values() method returns all values, and items() method returns all key-value pairs.
    - Modifying values during iteration is possible using the keys() method.
    - Understanding how to iterate over dictionaries helps in effectively managing and manipulating dictionary data.
    """

if __name__ == "__main__":
    main()


