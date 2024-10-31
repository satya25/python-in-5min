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
# File Name         :       lesson_12_1_introduction_to_oop.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Oct 26, 2024
# version           :       1.0
# Release           :       R1
# Dependencies      :       None
# Installation      :       NONE
# Usage             :       python ./src/lesson_12_1_introduction_to_oop.py
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
Lesson 12.1 - Introduction to OOP
---------------------------------
This script introduces the basics of Object-Oriented Programming in Python.
We will cover what OOP is, its key principles, and an overview of classes and objects.
""" 

# Importing the module 

# Object-Oriented Programming (OOP) is a programming paradigm based on the concept of "objects", which are instances of classes. It allows for organizing software design around data, or objects, rather than functions and logic.

# Key principles of OOP:
# - Encapsulation: Bundling of data and methods that operate on the data within one unit, e.g., a class in Python.
# - Inheritance: A mechanism where a new class inherits attributes and methods from an existing class.
# - Polymorphism: The ability to present the same interface for different underlying forms (data types).
# - Abstraction: Hiding the complex reality while exposing only the necessary parts.

# Overview of classes and objects
# A class is a blueprint for creating objects. An object is an instance of a class. Classes encapsulate data for the object and methods to manipulate that data.

# Example:
class Dog:
    # Constructor
    def __init__(self, name, age):
        self.name = name  # instance variable
        self.age = age    # instance variable
    
    # Method
    def bark(self):
        return f"{self.name} says Woof!"

def main():
    # Creating an object of the Dog class
    my_dog = Dog("Buddy", 5)

    # Calling the bark method
    print(my_dog.bark())  # Output: Buddy says Woof!
 
if __name__ == "__main__":
    main()