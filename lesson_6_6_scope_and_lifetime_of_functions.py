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
# File Name         :       lesson_6_6_scope_and_lifetime_of_functions.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Oct 26, 2024
# version           :       1.0
# Release           :       R1
# Dependencies      :       NONE
# Installation      :       NONE
# Usage             :       python ./src/lesson_6_6_scope_and_lifetime_of_functions.py
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
Lesson 6.6 - Scope and Lifetime of Functions
---------------------------------------------
This script explains the concept of scope and lifetime of variables within functions in Python.
We will explore local and global scope, and how the lifetime of variables is managed.
"""

# All imports whenever be applicable comes here.

def main():
    # Understanding scope and lifetime of variables with fun examples!
    
    # Global variable
    global_var = "I am a global variable"

    def print_global_var():
        """
        This function prints the value of a global variable.
        """
        print(global_var)  # Accessing the global variable

    def modify_global_var():
        """
        This function modifies the value of a global variable.
        """
        global global_var  # Declaring the intention to use the global variable
        global_var = "I have been modified"
    
    def demonstrate_local_scope():
        """
        This function demonstrates the concept of local scope.
        """
        local_var = "I am a local variable"
        print(local_var)  # Accessing the local variable

    def demonstrate_variable_lifetime():
        """
        This function demonstrates the lifetime of local variables.
        """
        if True:
            temp_var = "I exist only within this block"
        # Trying to access temp_var outside its block will cause an error
        # Uncommenting the following line will cause an error
        # print(temp_var)

    # Calling functions to demonstrate scope and lifetime
    print_global_var()
    modify_global_var()
    print_global_var()
    demonstrate_local_scope()
    demonstrate_variable_lifetime()

    """
    Important Points:
    - Variables declared inside a function are local variables and have local scope.
    - Variables declared outside any function are global variables and have global scope.
    - Global variables can be accessed inside functions, but to modify them, the 'global' keyword must be used.
    - Local variables exist only within the block of code where they are defined and are destroyed after the function completes.
    - Understanding scope and lifetime of variables helps in managing data and avoiding errors in code.
    """

if __name__ == "__main__":
    main()


