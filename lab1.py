"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    LAB 1
---------------------------------------------------------------------------------
- File Name: lab1.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Create and use lists in Python
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Create a list named favorite_foods and add at least five different food items to it
favourite_foods = ["banana", "apple", "pickles", "twitzle"]

# Change the third item in the list to a different food
favourite_foods[2] = "pringles"

# Print out only the first and fourth items in the list
print(favourite_foods[0])
print(favourite_foods[3])


# Ask the user for a food item
food = input("Please enter a food item to add to your list: ")

# Append the user's food item to the list
favourite_foods.append(food)

# Print out the entire list of food items
for i in favourite_foods:
    print(i)