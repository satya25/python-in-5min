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
# File Name         :       lesson_12_4_constructors.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Oct 29, 2024
# version           :       1.0
# Release           :       R1
# Dependencies      :       None
# Installation      :       NONE
# Usage             :       python ./src/lesson_12_4_constructors.py
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
Lesson 12.4 - Constructors
---------------------------
This script explains the concept of constructors in Object-Oriented Programming.
We will introduce the __init__ method, show how to initialize object attributes, and provide practical examples and use cases.
"""

# Defining a class
class Dog:
    # Class attributes
    species = 'Canis familiaris'

    # Constructor (__init__ method)
    def __init__(self, name, age):
        self.name = name  # instance variable
        self.age = age    # instance variable

    # Method
    def description(self):
        return f"{self.name} is {self.age} years old."

    # Method
    def speak(self, sound):
        return f"{self.name} says {sound}."

def main():
    # Creating instances (objects) of the Dog class
    my_dog = Dog("Buddy", 5)
    another_dog = Dog("Max", 3)
    
    # Accessing class attributes and methods
    print(f"My dog is a {my_dog.species}.")            # Output: My dog is a Canis familiaris.
    print(my_dog.description())                        # Output: Buddy is 5 years old.
    print(my_dog.speak("Woof Woof!"))                  # Output: Buddy says Woof Woof!

    print(f"Another dog is a {another_dog.species}.")  # Output: Another dog is a Canis familiaris.
    print(another_dog.description())                   # Output: Max is 3 years old.
    print(another_dog.speak("Bark!"))                  # Output: Max says Bark!

if __name__ == "__main__":
    main()

