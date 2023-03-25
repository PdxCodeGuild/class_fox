
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


def load_todos():
    # Open todos.txt
    todo = open("todos.txt")
    # Read the contents of todos.txt
    content = todo.read()
    todo.close()
    # Convert the contents into the following data structure
    todo_items = content.split("\n")

    todo_list = {}
    for item in todo_items:
        item = item.split(",")
        key = int(item[0])
        value = item[1]
        todo_list.update({key: value})
        # todo_list[key] = value

    return todo_list


def save_todos(todo_list):
    todo_list = list(todo_list.items())
    for x in range(len(todo_list)):
        todo_list[x] = str(todo_list[x][0]) + "," + todo_list[x][1]

    todo_list = "\n".join(todo_list)

    todo = open("todos.txt", "w")
    todo.write(todo_list)
    todo.close()


# Create a dictionary to store todos
todo_list = load_todos()

next_key = len(todo_list) + 1

# REPL
# Create an infinite loop
while True:
    print(todo_list)
    # Ask the user for what they would like to do
    # Choices: Create new item, retrieve an item, update an item, delete an item, or done
    user_input = input("""Choose one of the following:
1) Create a new todo.
2) Retrieve a todo.
3) Update a todo.
4) Delete a todo.
5) Done.
> """)

    # user chooses create:
    if user_input == "1":
        # Ask the user for the title of their todo
        todo_title = input("What would you like to do? ")
        # append a new todo to our list
        todo_list[next_key] = todo_title
        next_key = next_key + 1

    # user chooses retrieve:
    elif user_input == "2":
        # Ask the user for which todo
        todo_choice = input("Which todo would you like to retrieve? ")  # 2
        # Get a particular item from our dictionary and print it
        print(todo_list[int(todo_choice)])

    # user chooses update:
    elif user_input == "3":
        # retrieve item
        todo_choice = input("Which todo would you like to update? ")
        todo_title = input("What would you like to update this too? ")
        # Update a single item
        todo_list[int(todo_choice)] = todo_title

    # user chooses delete:
    elif user_input == "4":
        # retrieve item
        todo_choice = input("Which todo would you like to delete? ")
        # Remove item from dictionary
        del todo_list[int(todo_choice)]

        # user chooses done
    elif user_input == "5":
        save_todos(todo_list)
        break

    else:
        print("Invalid choice, please choose 1-5")
