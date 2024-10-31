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
# File Name         :       lesson_11_2_importing_modules.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Oct 26, 2024
# version           :       1.0
# Release           :       R1
# Dependencies      :       mymodule.py
# Installation      :       NONE
# Usage             :       python ./src/lesson_11_2_importing_modules.py
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
Lesson 11.2 - Importing Modules
---------------------------------
This script demonstrates how to import modules in Python.
We will explore different ways to import and use modules in Python programs.
"""

# Importing the module
import mymodule

def main():
    # Using the function from the module
    mymodule.greet("Alice")
    mymodule.greet("Bob")

    # Importing specific functions from the module
    from mymodule import greet
    greet("Charlie")
    greet("Dana")

    # Importing the module with an alias
    import mymodule as mm
    mm.greet("Eve")
    mm.greet("Frank")

    """
    Important Points:
    - Modules can be imported using the import statement followed by the module name.
    - Specific functions or classes can be imported from a module using the from module import function syntax.
    - Modules can be imported with an alias using the import module as alias syntax.
    - Using modules helps in organizing code, making it reusable and easier to maintain.
    - Understanding different ways to import modules is essential for writing modular and scalable code in Python.
    """

if __name__ == "__main__":
    main()

