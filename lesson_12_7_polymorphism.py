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
# File Name         :       lesson_12_7_polymorphism.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Nov 01, 2024
# version           :       1.0
# Release           :       R1
# Dependencies      :       None
# Installation      :       NONE
# Usage             :       python ./src/lesson_12_7_polymorphism.py
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
Lesson 12.7 - Polymorphism
--------------------------
This script introduces the concept of polymorphism in Object-Oriented Programming.
We will explain polymorphism, demonstrate method overriding and method overloading, and provide practical examples of polymorphism.
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
    # Overriding the speak method
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    # Overriding the speak method
    def speak(self):
        return f"{self.name} says Meow!"

def main():
    # Creating instances (objects) of the Dog and Cat classes
    dog = Dog("Buddy")
    cat = Cat("Whiskers")

    # Accessing overridden methods
    print(dog.speak())  # Output: Buddy says Woof!
    print(cat.speak())  # Output: Whiskers says Meow!

    # Demonstrating polymorphism
    animals = [dog, cat]
    for animal in animals:
        print(animal.speak())

if __name__ == "__main__":
    main()
