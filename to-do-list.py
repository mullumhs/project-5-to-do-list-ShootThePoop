"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                GUESSING GAME
---------------------------------------------------------------------------------
- File Name: to-do-list.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Complete a functional dice roller app in Python.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import time


todolist = []

def menu():
    print("Please select an option:")
    print("1. Add something to the list")
    print("2. Delete something from the list")
    print("3. Edit something from the list")
    print("4. View list")


def choice():
    while True:
        try:
            choice = int(input())
            if choice == 1:
                return choice
            if choice == 2:
                return choice
            if choice == 3:
                return choice
            if choice == 4:
                return choice
            else:
                print("Please enter a number between 1 and 3")

        except:
            print("Please enter a valid number")

def add():
    print("What would you like to add to your list?")
    print(todolist)
    addtolist = input()
    todolist.append(addtolist)
    print(f"Your new list is {todolist}")

def delete():
    print("What would you like to delete from your list?")
    print(todolist)
    deletefromlist = input()
    todolist.remove(deletefromlist)
    print(f"Your new list is {todolist}")

def edit():
    print("What would you like to edit?")
    print(todolist)
    remove = todolist.index(input())
    print(f"Your new list is {todolist}")

    print("Enter a new item: ")
    add = input()
    todolist[remove] = add
    print(todolist)

def viewlist():
    print("In your list you have:")
    for i, item in enumerate(todolist):
        print(f"{i+1}: {item}")


while True:
    time.sleep(2)
    menu()
    ch = choice()
    if ch == 1:
        add()
    if ch == 2:
        delete()
    if ch == 3:
        edit()
    if ch == 4:
        viewlist()

