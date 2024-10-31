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
# File Name         :       lesson_12_10_practical_applications.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Nov 04, 2024
# version           :       1.0
# Release           :       R1
# Dependencies      :       None
# Installation      :       NONE
# Usage             :       python ./src/lesson_12_10_practical_applications.py
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
Lesson 12.10 - Practical Applications and Exercises
---------------------------------------------------
This script combines OOP concepts in real-world scenarios.
We will create a simple banking system using OOP principles to reinforce the concepts learned.
"""

class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Added {amount} to the balance")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount} from the balance")
        else:
            print("Invalid withdrawal amount or insufficient funds")

    def display_balance(self):
        return f"Account owner: {self.owner}, Balance: {self.balance}"

def main():
    # Creating an Account object
    account1 = Account("Alice", 1000)

    # Displaying the initial balance
    print(account1.display_balance())  # Output: Account owner: Alice, Balance: 1000

    # Making a deposit
    account1.deposit(500)
    print(account1.display_balance())  # Output: Account owner: Alice, Balance: 1500

    # Making a withdrawal
    account1.withdraw(200)
    print(account1.display_balance())  # Output: Account owner: Alice, Balance: 1300

    # Trying an invalid deposit
    account1.deposit(-100)  # Output: Invalid deposit amount

    # Trying an invalid withdrawal
    account1.withdraw(2000)  # Output: Invalid withdrawal amount or insufficient funds

if __name__ == "__main__":
    main()
