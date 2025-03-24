import random
import time

def diceroller():


    def get_number(prompt):
        while True:
            try:
                number = int(input(prompt))  # Convert input to integer
                if number > 0:  # Ensure the number is positive
                    return number
                else:
                    print("Please enter a positive number.")
            except ValueError:
                print("Invalid input. Please enter a whole number.")


    def roll(sides, qty):
        total = 0
        for i in range(1, qty):
            time.sleep(0.4)
            rnd = random.randint(1, sides)
            total = total + rnd
            print(f"Rolled: {rnd}")
        time.sleep(0.5)
        print(f"The total is {total}.")
        

    sides = get_number("How many sides would you like the dice to have?: ")
    qty = get_number("How many dice would you like to roll?: ")


    print("Rolling the dice...")
    time.sleep(0.2)
    roll(sides, qty+1)
    print("Back to the main menu...")
    time.sleep(1.5)
    run()



todolist = []

def run():
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
                diceroller()
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
    viewlist()
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
    run()
    ch = choice()
    if ch == 1:
        add()
    if ch == 2:
        delete()
    if ch == 3:
        edit()
    if ch == 4:
        viewlist()
