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
# File Name         :       lesson_8_8_mini_project_inventory_management_system.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Oct 26, 2024
# version           :       1.0
# Release           :       R1
# Dependencies      :       NONE
# Installation      :       NONE
# Usage             :       python ./src/lesson_8_8_mini_project_inventory_management_system.py
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
Lesson 8.8 - Mini Project: Inventory Management System
--------------------------------------------------------
This mini project demonstrates the use of dictionaries and sets in Python by creating a simple inventory management system.
We will implement functions to add, remove, update, and view inventory items.
"""

# All imports whenever be applicable comes here.

def main():
    # Welcome to the Inventory Management System!
    print("Welcome to the Inventory Management System!")

    # Creating an empty inventory dictionary
    inventory = {}

    # Defining functions for the inventory management system
    def add_item(item_name, quantity):
        """
        This function adds a new item to the inventory or updates the quantity if the item already exists.
        """
        if item_name in inventory:
            inventory[item_name] += quantity
        else:
            inventory[item_name] = quantity
        print(f"Added/Updated item: {item_name} - Quantity: {quantity}")

    def remove_item(item_name):
        """
        This function removes an item from the inventory.
        """
        if item_name in inventory:
            del inventory[item_name]
            print(f"Removed item: {item_name}")
        else:
            print(f"Item not found: {item_name}")

    def update_item(item_name, quantity):
        """
        This function updates the quantity of an item in the inventory.
        """
        if item_name in inventory:
            inventory[item_name] = quantity
            print(f"Updated item: {item_name} - New Quantity: {quantity}")
        else:
            print(f"Item not found: {item_name}")

    def view_inventory():
        """
        This function displays all items in the inventory.
        """
        if inventory:
            print("Current Inventory:")
            for item_name, quantity in inventory.items():
                print(f"{item_name} - Quantity: {quantity}")
        else:
            print("Inventory is empty.")

    # Main menu for the inventory management system
    while True:
        print("\nSelect an option:")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Update Item")
        print("4. View Inventory")
        print("5. Exit")
        
        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == '1':
            item_name = input("Enter item name: ")
            try:
                quantity = int(input("Enter quantity: "))
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue
            add_item(item_name, quantity)
        elif choice == '2':
            item_name = input("Enter item name to remove: ")
            remove_item(item_name)
        elif choice == '3':
            item_name = input("Enter item name to update: ")
            try:
                quantity = int(input("Enter new quantity: "))
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue
            update_item(item_name, quantity)
        elif choice == '4':
            view_inventory()
        elif choice == '5':
            print("Exiting the Inventory Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
    
    """
    Important Points:
    - This mini project demonstrates the use of dictionaries and sets to manage an inventory.
    - Functions for adding, removing, updating, and viewing inventory items are implemented.
    - The inventory management system provides an interactive menu for managing inventory items.
    - Interactive projects like this inventory management system make learning Python fun and engaging.
    """

if __name__ == "__main__":
    main()


