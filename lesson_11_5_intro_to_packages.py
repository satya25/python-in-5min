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
# File Name         :       lesson_11_5_intro_to_packages.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Oct 26, 2024
# version           :       1.0
# Release           :       R1
# Dependencies      :       mypackage
# Installation      :       NONE
# Usage             :       python ./src/lesson_11_5_intro_to_packages.py
# ----------------------------------------------------------------------------
# Credits and Acknowledgements
# - Special thanks to the Python community for their excellent work:
#   https://www.python.org/community/
# - The APIs used in this script are documented here:
#   https://docs.python.org/3/
# - Code Snippet(s) adapted from    :   -- NOT Applicable --
# - Dataset(s) sourced from         :   -- NOT Applicable --
# - Inspiration drawn from          :   -- NOT Applicable --

# Thank you to the creators and maintainers of these resources!
# ----------------------------------------------------------------------------
# - Content Removal Requests
#   If you are the owner or creator of any content used in this script and
#   would like it to be removed, please contact me at: spnigam25@yahoo.com
#   I will promptly remove the content upon request.
# ----------------------------------------------------------------------------

"""
Lesson 11.5 - Introduction to Packages
----------------------------------------
This script demonstrates how to create and use packages in Python.
We will create a package with multiple modules and use it in this script.
"""

# Importing the custom package modules
from mypackage import module1
from mypackage import module2

def main():
    # Using functions from module1
    print("Addition (2 + 3):", module1.add(2, 3))
    #print("Subtraction
    

if __name__ == "__main__":
    main()







"""
Create a Package Directory: 
    
    1.  Create a directory named mypackage.

    2.  Inside mypackage, create an __init__.py file to make it a package.

    3.  Create two module files: module1.py and module2.py.

    4.  Module files in mypackage:
"""