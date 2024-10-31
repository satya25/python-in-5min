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
# File Name         :       lesson_10_9_mini_project_file_parser.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Oct 26, 2024
# version           :       1.0
# Release           :       R1
# Dependencies      :       NONE
# Installation      :       NONE
# Usage             :       python ./src/lesson_10_9_mini_project_file_parser.py
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
Lesson 10.9 - Mini Project: File Parser
-----------------------------------------
This mini project demonstrates the use of exception handling in Python by creating a simple file parser.
We will implement functions to read, analyze, and summarize text files, handling any exceptions that occur.
"""

# All imports whenever be applicable comes here.

def main():
    # Welcome to the File Parser Tool!
    print("Welcome to the File Parser Tool!")

    # Creating a sample text file for parsing
    with open("sample_text.txt", "w") as file:
        file.write("Hello, world!\n")
        file.write("This is a sample text file for parsing.\n")
        file.write("Let's analyze and summarize the content.\n")
        print("Sample text file 'sample_text.txt' created for parsing.")

    # Function to read and parse the text file
    def parse_text_file(file_path):
        try:
            with open(file_path, "r") as file:
                content = file.read()
                return content
        except FileNotFoundError:
            print(f"Error: The file '{file_path}' was not found.")
        except IOError:
            print(f"Error: An IOError occurred while reading the file '{file_path}'.")
        finally:
            print("Finished attempting to read the file.")

    # Function to analyze the content of the text file
    def analyze_content(content):
        lines = content.split("\n")
        word_count = sum(len(line.split()) for line in lines)
        return len(lines), word_count

    # Function to summarize the text file
    def summarize_text_file(file_path):
        content = parse_text_file(file_path)
        if content:
            num_lines, num_words = analyze_content(content)
            print(f"Summary of '{file_path}':")
            print(f"Number of lines: {num_lines}")
            print(f"Number of words: {num_words}")

    # Summarizing the sample text file
    summarize_text_file("sample_text.txt")

    """
    Important Points:
    - This mini project demonstrates the use of exception handling to manage errors while parsing text files.
    - Functions for reading, analyzing, and summarizing text files are implemented.
    - The file parser tool provides a summary of the text file, including the number of lines and words.
    - Interactive projects like this file parser make learning Python fun and engaging.
    """

if __name__ == "__main__":
    main()


