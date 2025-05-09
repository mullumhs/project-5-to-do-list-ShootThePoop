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
    print("5. Play Diceroller")


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
            if choice == 5:
                break
            else:
                print("Please enter a number between 1 and 3")

        except:
            print("Please enter a valid number")

def add():
    print("What would you like to add to your list?")
    print(viewlist())
    addtolist = input()
    todolist.append(addtolist)
    print(f"Your new list is {viewlist()}")

def delete():
    print("What would you like to delete from your list?")
    viewlist()
    deletefromlist = input()
    try:
        todolist.remove(deletefromlist)

    except:
        print("You cannot delete something not in your list..")

    print(f"Your new list is {viewlist()}")

def edit():
    print("What would you like to edit?")

    remove = input()
    try:
        remove = todolist.index(remove)
        print("Enter your replacement")
        add = input()
        todolist[remove] = add
        
    except:
        print("You cannot edit something not in your list...")    


def viewlist():
    print("In your list you have:")
    for i, item in enumerate(todolist):
        print(f"{i+1}: {item}")


while True:
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
    if ch == 5:
        break

