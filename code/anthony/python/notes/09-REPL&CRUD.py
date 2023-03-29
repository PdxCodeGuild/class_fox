
# REPL
# Read Evaluate Print Loop
"""
while True:
    play_again = input("Would you like to play again? ")
    if play_again == "yes":
        continue
    elif play_again == "no":
        break
    else:
        print("Invalid input")
"""


# CRUD
# Create Retrieve Update Delete
# Contact List
# Shopping List
# YouTube watch history
# Search History

"""
CRUD - TodoList w/ repl

C - Make new todo items
R - Get a single todo item from list
U - Edit title of todo, change its completed status
D - Remove items from list

Version 1: Use a python list to store all todos
Version 2: Save our todos to a file (CSV)

"""

# Function to load todos from the "todos.txt" file


def load_todos():
    # Open "todos.txt" for reading
    todo = open("todos.txt")
    # Read the contents of the file
    content = todo.read()
    todo.close()
    # Convert the contents into a list of todo items by splitting at newline characters
    todo_items = content.split("\n")

    # Initialize an empty dictionary to store the todo items
    todo_list = {}
    # Iterate through the todo_items list
    for item in todo_items:
        # Split the item into a key and value pair separated by a comma
        item = item.split(",")
        key = int(item[0])
        value = item[1]
        # Add the key-value pair to the todo_list dictionary
        todo_list.update({key: value})

    # Return the todo_list dictionary
    return todo_list

# Function to save the todo_list dictionary to the "todos.txt" file


def save_todos(todo_list):
    # Convert the todo_list dictionary into a list of key-value pairs
    todo_list = list(todo_list.items())
    # Iterate through the list and convert each key-value pair into a string with a comma separator
    for x in range(len(todo_list)):
        todo_list[x] = str(todo_list[x][0]) + "," + todo_list[x][1]

    # Join the list of strings with newline characters to form a single string
    todo_list = "\n".join(todo_list)

    # Open "todos.txt" for writing
    todo = open("todos.txt", "w")
    # Write the todo_list string to the file
    todo.write(todo_list)
    todo.close()


# Load the todos from the "todos.txt" file into a dictionary
todo_list = load_todos()

# Initialize the next_key variable to be used as the next dictionary key
next_key = len(todo_list) + 1

# REPL (Read, Evaluate, Print, Loop) for user interaction
while True:
    # Print the current todo list
    print(todo_list)
    # Prompt the user for an action
    user_input = input("""Choose one of the following:
1) Create a new todo.
2) Retrieve a todo.
3) Update a todo.
4) Delete a todo.
5) Done.
> """)

    # User chooses to create a new todo item
    if user_input == "1":
        # Prompt the user for the title of their todo
        todo_title = input("What would you like to do? ")
        # Add the new todo item to the todo_list dictionary
        todo_list[next_key] = todo_title
        # Increment the next_key variable
        next_key = next_key + 1

    # User chooses to retrieve a todo item
    elif user_input == "2":
        # Prompt the user for the key of the todo item they want to retrieve
        todo_choice = input("Which todo would you like to retrieve? ")
        # Print the requested todo item
        print(todo_list[int(todo_choice)])

    # User chooses to update a todo item
    elif user_input == "3":
        # Prompt the user for the key of the todo item they want to update
        todo_choice = input("Which todo would you like to update? ")
        # Prompt the user for the new title of the todo item
        todo_title = input("What would you like to update this to? ")
        # Update the todo item in the todo_list dictionary
        todo_list[int(todo_choice)] = todo_title

        # User chooses to delete a todo item
    elif user_input == "4":
        # Prompt the user for the key of the todo item they want to delete
        todo_choice = input("Which todo would you like to delete? ")
        # Remove the specified todo item from the todo_list dictionary
        del todo_list[int(todo_choice)]

    # User chooses to exit the program
    elif user_input == "5":
        # Save the updated todo_list dictionary to the "todos.txt" file
        save_todos(todo_list)
        # Break out of the loop to exit the program
        break

    # User enters an invalid choice
    else:
        # Print an error message
        print("Invalid choice, please choose 1-5")
