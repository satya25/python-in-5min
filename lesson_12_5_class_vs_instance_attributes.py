#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This file is part of aialchemyhub_in (https://github.com/satya25/aialchemyhub_in).
aialchemyhub_in is free software repository: You can redistribute it and/or modify it 
under the terms of the MIT License. aialchemyhub_in is distributed in the hope that 
it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of 
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. 
See the MIT License for more details. You should have received a copy of the MIT 
License along with aialchemyhub_in. If not, see <https://opensource.org/licenses/MIT>.
"""
# ----------------------------------------------------------------------------
# File Name         :       lesson_12_5_class_vs_instance_attributes.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Oct 30, 2024
# version           :       1.0
# Release           :       R1
# Dependencies      :       None
# Installation      :       NONE
# Usage             :       python ./src/lesson_12_5_class_vs_instance_attributes.py
# ----------------------------------------------------------------------------
# Credits and Acknowledgements
# - Special thanks to the Python community for their excellent work:
#   https://www.python.org/community/
# - The APIs used in this script are documented here:
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
Lesson 12.5 - Class vs. Instance Attributes
-------------------------------------------
This script explains the differences between class attributes and instance attributes in Python.
We will provide practical examples and best practices.
"""

# Defining a class
class Dog:
    # Class attribute
    species = 'Canis familiaris'

    # Constructor
    def __init__(self, name, age):
        self.name = name  # instance attribute
        self.age = age    # instance attribute

    # Method
    def description(self):
        return f"{self.name} is {self.age} years old."

    # Method
    def speak(self, sound):
        return f"{self.name} says {sound}."

def main():
    # Creating instances (objects) of the Dog class
    dog1 = Dog("Buddy", 5)
    dog2 = Dog("Max", 3)
    
    # Accessing class attributes and instance attributes
    print(f"Dog 1 is a {dog1.species}.")            # Output: Dog 1 is a Canis familiaris.
    print(f"Dog 2 is a {dog2.species}.")            # Output: Dog 2 is a Canis familiaris.

    print(dog1.description())                       # Output: Buddy is 5 years old.
    print(dog2.description())                       # Output: Max is 3 years old.

    # Modifying instance attributes
    dog1.age = 6
    print(dog1.description())                       # Output: Buddy is 6 years old.

    # Best practices
    # - Use class attributes for attributes that are shared across all instances of a class.
    # - Use instance attributes for attributes that are unique to each instance.

if __name__ == "__main__":
    main()
