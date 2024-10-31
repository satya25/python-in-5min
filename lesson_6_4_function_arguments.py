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
# File Name         :       lesson_6_4_function_arguments.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Oct 26, 2024
# version           :       1.0
# Release           :       R1
# Dependencies      :       NONE
# Installation      :       NONE
# Usage             :       python ./src/lesson_6_4_function_arguments.py
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
Lesson 6.4 - Function Arguments
--------------------------------
This script demonstrates different types of function arguments in Python.
We will explore positional arguments, keyword arguments, and default arguments.
"""

# All imports whenever be applicable comes here.

def main():
    # Understanding function arguments with fun examples!
    
    # Defining a function with positional arguments
    def describe_person(name, age):
        """
        This function takes a name and age as positional arguments and prints a description.
        """
        print(f"{name} is {age} years old.")

    # Calling the function with positional arguments
    describe_person("Alice", 30)
    describe_person("Bob", 25)
    
    # Defining a function with keyword arguments
    def describe_city(name, country="USA"):
        """
        This function takes a city name as a positional argument and a country as a keyword argument.
        """
        print(f"{name} is a city in {country}.")

    # Calling the function with keyword arguments
    describe_city("New York")
    describe_city("Tokyo", country="Japan")

    # Defining a function with a mix of arguments
    def book_description(title, author, year=2020):
        """
        This function takes a book title and author as positional arguments and a year as a keyword argument.
        """
        print(f"'{title}' by {author}, published in {year}.")

    # Calling the function with a mix of arguments
    book_description("Python Crash Course", "Eric Matthes")
    book_description("Automate the Boring Stuff with Python", "Al Sweigart", year=2019)

    """
    Important Points:
    - Positional arguments are passed to a function based on their position in the function call.
    - Keyword arguments are passed to a function by explicitly specifying the parameter name.
    - Default arguments are parameters that have a default value if no value is provided in the function call.
    - Understanding function arguments helps in creating flexible and reusable functions.
    """

if __name__ == "__main__":
    main()


