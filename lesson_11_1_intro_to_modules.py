#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" 
This file is part of aialchemyhub_in
(https://github.com/satya25/aialchemyhub_in).
aialchemyhub_in is free software repository: 
You can redistribute it and/or modify it under the terms of the MIT License.
aialchemyhub_in is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the MIT License for more details.
You should have received a copy of the MIT License along with aialchemyhub_in.
If not, see <https://opensource.org/licenses/MIT>.
"""

# ----------------------------------------------------------------------------
# File Name         :       lesson_11_1_intro_to_modules.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Oct 26, 2024
# version           :       1.0
# Release           :       R1
# Dependencies      :       NONE
# Installation      :       NONE
# Usage             :       python ./src/lesson_11_1_intro_to_modules.py
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
Lesson 11.1 - Introduction to Modules
---------------------------------------
This script introduces the concept of modules in Python.
We will explore how to create, import, and use modules to organize and reuse code.
"""

# Importing the module
import mymodule

def main():
    # Using the function from the module
    mymodule.greet("Alice")
    mymodule.greet("Bob")

    """
    Important Points:
    - Modules are files containing Python code, typically functions, classes, or variables, that can be reused in other programs.
    - Creating a module involves saving the code in a separate file with a .py extension.
    - Importing a module involves using the import statement followed by the module name.
    - Using modules helps in organizing code, making it reusable and easier to maintain.
    - Understanding modules is essential for writing modular and scalable code in Python.
    """

if __name__ == "__main__":
    main()
