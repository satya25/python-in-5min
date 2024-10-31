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
# File Name         :       lesson_9_10_mini_project_log_file_analysis_tool.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Oct 26, 2024
# version           :       1.0
# Release           :       R1
# Dependencies      :       NONE
# Installation      :       NONE
# Usage             :       python ./src/lesson_9_10_mini_project_log_file_analysis_tool.py
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
Lesson 9.10 - Mini Project: Log File Analysis Tool
---------------------------------------------------
This mini project demonstrates the use of file handling in Python by creating a simple log file analysis tool.
We will implement functions to read, analyze, and summarize log files.
"""

# All imports whenever be applicable comes here.

def main():
    # Welcome to the Log File Analysis Tool!
    print("Welcome to the Log File Analysis Tool!")

    # Creating a sample log file for analysis
    with open("logfile.log", "w") as file:
        file.write("INFO: User logged in\n")
        file.write("ERROR: File not found\n")
        file.write("WARNING: Low disk space\n")
        file.write("INFO: User performed action\n")
        file.write("ERROR: Network timeout\n")
        print("Sample log file 'logfile.log' created for analysis.")

    # Function to read and analyze the log file
    def analyze_log_file(log_file_path):
        """
        This function reads a log file and analyzes its contents.
        """
        log_data = {
            "INFO": 0,
            "ERROR": 0,
            "WARNING": 0
        }
        
        with open(log_file_path, "r") as file:
            for line in file:
                if "INFO" in line:
                    log_data["INFO"] += 1
                elif "ERROR" in line:
                    log_data["ERROR"] += 1
                elif "WARNING" in line:
                    log_data["WARNING"] += 1
        
        return log_data

    # Analyzing the sample log file
    log_analysis = analyze_log_file("logfile.log")
    print("Log file analysis summary:", log_analysis)

    """
    Important Points:
    - This mini project demonstrates the use of file handling to analyze log files.
    - Functions for reading and analyzing log files are implemented.
    - The log file analysis tool provides a summary of log entries, categorized by type (INFO, ERROR, WARNING).
    - Interactive projects like this log file analysis tool make learning Python fun and engaging.
    """

if __name__ == "__main__":
    main()


