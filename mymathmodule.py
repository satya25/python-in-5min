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
# File Name         :       mymathmodule.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Oct 26, 2024
# version           :       1.0
# Release           :       R1
# Dependencies      :       NONE
# Installation      :       NONE
# Usage             :       import mymathmodule
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
This module contains custom functions for mathematical operations including
factorials, arithmetic progressions sum, and computing simple interest.
"""

def factorial(n):
    """
    This function calculates the factorial of a number.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def arithmetic_progression_sum(a, d, n):
    """
    This function calculates the sum of the first n terms of an arithmetic progression.
    a: First term
    d: Common difference
    n: Number of terms
    """
    return n / 2 * (2 * a + (n - 1) * d)

def simple_interest(principal, rate, time):
    """
    This function calculates the simple interest.
    principal: Principal amount
    rate: Rate of interest (as a percentage)
    time: Time period (in years)
    """
    return (principal * rate * time) / 100


