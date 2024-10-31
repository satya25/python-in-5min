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
# File Name         :       lesson_7_9_mini_project_contact_list.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Oct 26, 2024
# version           :       1.0
# Release           :       R1
# Dependencies      :       NONE
# Installation      :       NONE
# Usage             :       python ./src/lesson_7_9_mini_project_contact_list.py
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
Lesson 7.9 - Mini Project: Contact List
----------------------------------------
This mini project demonstrates the use of lists in Python by creating a simple contact list application.
We will implement functions to add, remove, and search for contacts in the list.
"""

# All imports whenever be applicable comes here.

def main():
    # Welcome to the Contact List Application!
    print("Welcome to the Contact List Application!")

    # Creating an empty contact list
    contacts = []

    # Defining functions for the contact list
    def add_contact(name, phone):
        """
        This function adds a new contact to the contact list.
        """
        contacts.append({"name": name, "phone": phone})
        print(f"Added contact: {name} - {phone}")

    def remove_contact(name):
        """
        This function removes a contact from the contact list.
        """
        for contact in contacts:
            if contact["name"] == name:
                contacts.remove(contact)
                print(f"Removed contact: {name}")
                return
        print(f"Contact not found: {name}")

    def search_contact(name):
        """
        This function searches for a contact by name and prints the contact details.
        """
        for contact in contacts:
            if contact["name"] == name:
                print(f"Found contact: {name} - {contact['phone']}")
                return
        print(f"Contact not found: {name}")

    def display_contacts():
        """
        This function displays all contacts in the contact list.
        """
        if contacts:
            print("Contact List:")
            for contact in contacts:
                print(f"{contact['name']} - {contact['phone']}")
        else:
            print("Contact list is empty.")

    # Main menu for the contact list application
    while True:
        print("\nSelect an option:")
        print("1. Add Contact")
        print("2. Remove Contact")
        print("3. Search Contact")
        print("4. Display Contacts")
        print("5. Exit")
        
        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter contact phone: ")
            add_contact(name, phone)
        elif choice == '2':
            name = input("Enter contact name to remove: ")
            remove_contact(name)
        elif choice == '3':
            name = input("Enter contact name to search: ")
            search_contact(name)
        elif choice == '4':
            display_contacts()
        elif choice == '5':
            print("Exiting the Contact List Application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
    
    """
    Important Points:
    - This mini project demonstrates the use of lists to manage a contact list.
    - Functions for adding, removing, searching, and displaying contacts are implemented.
    - The contact list application provides an interactive menu for managing contacts.
    - Interactive projects like this contact list make learning Python fun and engaging.
    """

if __name__ == "__main__":
    main()


