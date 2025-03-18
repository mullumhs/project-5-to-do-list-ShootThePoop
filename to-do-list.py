"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                GUESSING GAME
---------------------------------------------------------------------------------
- File Name: to-do-list.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Complete a functional dice roller app in Python.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import time

print("Welcome to ---===THE+LIST===---")
time.sleep(1)
def Menu():
    print("Would you like to:")
    print("1. Add to the list")
    print("2. Edit the list")
    print("3. Remove something from the list")
    choice = input("Make your choice: ")
    while True:
        try:
            int(choice)

        except:
            print("Please enter a number.")

    
Menu()