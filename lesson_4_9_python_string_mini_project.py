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
# File Name         :       lesson_4_9_python_string_mini_project.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Oct 26, 2024
# version           :       1.0
# Release           :       R1
# Dependencies      :       NONE
# Installation      :       NONE
# Usage             :       python ./src/lesson_4_9_python_string_mini_project.py
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
Lesson 4.9 - Python String Mini Project
----------------------------------------
This mini project demonstrates various string manipulations in Python.
We will create a fun and interactive Mad Libs game using string formatting and methods.
"""

# All imports whenever be applicable comes here.

def main():
    # Welcome to the Mad Libs game!
    print("Welcome to the Python Mad Libs game!")
    print("Fill in the blanks to create a funny story.\n")
    
    # Collecting user input for the Mad Libs
    adjective = input("Enter an adjective: ")
    noun1 = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    noun2 = input("Enter another noun: ")
    adverb = input("Enter an adverb: ")
    adjective2 = input("Enter another adjective: ")
    
    # Creating the Mad Libs story using f-strings
    story = f"Today, I went to the park and saw a {adjective} {noun1}. \nIt was so {adjective2} that I decided to {verb} it. \
    \nSuddenly, a {noun2} appeared and {verb}ed {adverb} at me. It was the most {adjective2} experience ever!"
    
    # Displaying the generated story
    print("\nHere is your Mad Libs story:")
    print(story)

    """
    Important Points:
    - This mini project demonstrates the use of string formatting, methods, and user input.
    - Interactive projects like Mad Libs make learning Python fun and engaging.
    - Combining different string techniques can create complex and entertaining programs.
    """

if __name__ == "__main__":
    main()


