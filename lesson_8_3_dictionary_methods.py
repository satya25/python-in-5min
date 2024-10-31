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
# File Name         :       lesson_8_3_dictionary_methods.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Oct 26, 2024
# version           :       1.0
# Release           :       R1
# Dependencies      :       NONE
# Installation      :       NONE
# Usage             :       python ./src/lesson_8_3_dictionary_methods.py
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
Lesson 8.3 - Dictionary Methods
---------------------------------
This script demonstrates various methods available for dictionaries in Python.
We will explore methods for adding, removing, and manipulating dictionary elements.
"""

# All imports whenever be applicable comes here.

def main():
    # Understanding dictionary methods with fun examples!
    
    # Creating a dictionary of fruits and their prices
    fruit_prices = {
        "apple": 0.5,
        "banana": 0.3,
        "cherry": 1.0
    }
    print("Original dictionary of fruit prices:", fruit_prices)

    # Adding elements to the dictionary using update()
    fruit_prices.update({"date": 1.5, "elderberry": 2.0})
    print("Dictionary after update:", fruit_prices)

    # Removing elements from the dictionary using pop()
    banana_price = fruit_prices.pop("banana")
    print("Dictionary after popping 'banana':", fruit_prices)
    print("Popped banana price:", banana_price)

    # Removing the last inserted key-value pair using popitem()
    last_item = fruit_prices.popitem()
    print("Dictionary after popitem:", fruit_prices)
    print("Popped item:", last_item)

    # Getting all keys using keys()
    keys = fruit_prices.keys()
    print("Keys in the dictionary:", list(keys))

    # Getting all values using values()
    values = fruit_prices.values()
    print("Values in the dictionary:", list(values))

    # Getting all key-value pairs using items()
    items = fruit_prices.items()
    print("Items in the dictionary:", list(items))

    # Copying the dictionary using copy()
    fruit_prices_copy = fruit_prices.copy()
    print("Copy of the dictionary:", fruit_prices_copy)

    # Clearing all elements using clear()
    fruit_prices.clear()
    print("Dictionary after clear:", fruit_prices)

    """
    Important Points:
    - Dictionary methods provide various ways to add, remove, and manipulate key-value pairs.
    - Common dictionary methods include update(), pop(), popitem(), keys(), values(), items(), copy(), and clear().
    - Understanding dictionary methods helps in effectively managing and manipulating dictionaries in Python.
    """

if __name__ == "__main__":
    main()

 