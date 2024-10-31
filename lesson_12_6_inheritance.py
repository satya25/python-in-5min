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
# File Name         :       lesson_12_6_inheritance.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Oct 31, 2024
# version           :       1.0
# Release           :       R1
# Dependencies      :       None
# Installation      :       NONE
# Usage             :       python ./src/lesson_12_6_inheritance.py
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
Lesson 12.6 - Inheritance
--------------------------
This script introduces the concept of inheritance in Object-Oriented Programming.
We will explain inheritance, create a subclass, override methods, and provide practical examples of inheritance.
"""

# Defining a base class
class Animal:
    # Constructor
    def __init__(self, name):
        self.name = name

    # Method
    def speak(self):
        raise NotImplementedError("Subclasses must implement this method")

# Defining a subclass
class Dog(Animal):
    # Overriding the constructor
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    # Overriding the speak method
    def speak(self):
        return f"{self.name} says Woof!"

def main():
    # Creating an instance (object) of the Dog class
    my_dog = Dog("Buddy", 5)
    
    # Accessing class attributes and methods
    print(f"{my_dog.name} is {my_dog.age} years old.") # Output: Buddy is 5 years old.
    print(my_dog.speak())                             # Output: Buddy says Woof!

if __name__ == "__main__":
    main()

