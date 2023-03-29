# Lab 7: Contact List


Let's build a program to manage a list of contacts. To start, we'll build a CSV ('comma separated values') together, and go over how to load that file. Headers might consist of `name`, `favorite fruit`, `favorite color`. Open the CSV, convert the lines of text into a **list of dictionaries**, one dictionary for each user. The text in the header represents the **keys**, the text in the other lines represent the **values**.

```python
file = open('contacts.csv', 'r'):
lines = file.read().split('\n')
file.close()
print(lines)
```

Once you've processed the file, your list of contacts will look something like this...
```python
contacts = [
    {'name':'matthew', 'favorite fruit':'blackberries', 'favorite color':'orange'},
    {'name':'sam', 'favorite fruit':'pineapple' ...}
]
```

*Note: There is a `csv` library in Python that will do much of this for you. It is what you would use normally in a project, but for this lab you need to write all the logic yourself.*

<details>
<summary>If you need help, or get stuck.</summary>

1. Create a CSV file named "contacts.csv" containing the contact information with headers "name", "favorite fruit", and "favorite color". Each row should represent a different contact, and the values should be separated by commas.

Example:

```csv
name,favorite fruit,favorite color
matthew,blackberries,orange
sam,pineapple,blue
```

2. Open the CSV file in read mode using the with open statement. This will ensure that the file is properly closed after the block of code is executed.

3. Read the contents of the file using file.read(), and split the contents into lines using the split('\n') method. This will create a list of strings, where each string represents a line in the CSV file.

4. Extract the header row from the list of lines, and split the header row into a list of header keys using the split(',') method. This will help you create the keys for the dictionaries later.

5. Initialize an empty list called contacts to store the dictionaries representing each contact.

6. Iterate over the remaining lines in the CSV file (excluding the header row), and do the following for each line:

    a. Split the line into a list of values using the split(',') method.

    b. Create an empty dictionary called contact.

    c. Iterate over the header keys and the corresponding values from the line, and add them as key-value pairs to the contact dictionary. You can use the enumerate function to loop over the header keys and their indexes, and then use the index to access the corresponding value from the list of values.

    d. Append the contact dictionary to the contacts list.

7. Print the contacts list to see the final output, which should look like this:

```python
contacts = [    {'name':'matthew', 'favorite fruit':'blackberries', 'favorite color':'orange'},    {'name':'sam', 'favorite fruit':'pineapple', 'favorite color':'blue'},    ...]
```

> Remember not to use the csv library for this lab assignment.

</details>

## Version 2

Implement a CRUD REPL

- **C**reate a record: ask the user for each attribute, add a new contact to your contact list with the attributes that the user entered.
- **R**etrieve a record: ask the user for the contact's name, find the user with the given name, and display their information
- **U**pdate a record: ask the user for the contact's name, then for which attribute of the user they'd like to update and the value of the attribute they'd like to set.
- **D**elete a record: ask the user for the contact's name, remove the contact with the given name from the contact list.

<details>
<summary>If you need help, or get stuck.</summary>

1. Create a function called create_contact() that does the following:

    a. Prompt the user for the contact's name, favorite fruit, and favorite color.

    b. Create a dictionary called contact with the keys "name", "favorite fruit", and "favorite color", and the values entered by the user.

    c. Append the contact dictionary to the contacts list.

1. Create a function called retrieve_contact() that does the following:

    a. Prompt the user for the contact's name.

    b. Iterate through the contacts list and find the contact with the given name.

    c. Display the contact's information if found, or print a message indicating that the contact was not found.

1. Create a function called update_contact() that does the following:

    a. Prompt the user for the contact's name.

    b. Iterate through the contacts list and find the contact with the given name.

    c. If the contact is found, ask the user which attribute they'd like to update ("name", "favorite fruit", or "favorite color") and the new value for that attribute. Update the contact's attribute with the new value.

    d. If the contact is not found, print a message indicating that the contact was not found.

1. Create a function called delete_contact() that does the following:

    a. Prompt the user for the contact's name.

    b. Iterate through the contacts list and find the contact with the given name.

    c. If the contact is found, remove the contact from the contacts list. Otherwise, print a message indicating that the contact was not found.

1. Create a function called main_loop() that does the following:

    a. Continuously prompt the user for an action to perform ("C" for create, "R" for retrieve, "U" for update, "D" for delete, or "Q" for quit).

    b. Call the appropriate function (created in steps 2-5) based on the user's input, or exit the loop if the user enters "Q".

    c. Print a message indicating the current state of the contacts list after each action.

1. Call the main_loop() function to start the CRUD REPL.
</details>

## Version 3

When REPL loop finishes, write the updated contact info to the CSV file to be saved. I highly recommend saving a backup `contacts.csv` because you likely won't write it correctly the first time.

<details>
<summary>If you need help, or get stuck.</summary>

1. Modify the main_loop() function to accept the contacts list as an argument.

1. Create a function called save_contacts() that takes the contacts list as an argument and does the following:

    a. Create a list of header keys (e.g., ["name", "favorite fruit", "favorite color"]).

    b. Convert the contacts list into a list of CSV lines, including the header row, by iterating over the contacts list and joining the values of each dictionary with commas.

    c. Join the list of CSV lines with newline characters (\n) to form a single string.

    d. Open the "contacts.csv" file in write mode using the with open statement. This will ensure that the file is properly closed after the block of code is executed.

    e. Write the CSV string to the file.

1. Call the load_contacts() function at the beginning of the program to load the contacts from the CSV file into the contacts list.

1. Call the main_loop() function with the contacts list as an argument to start the CRUD REPL.

1. Call the save_contacts() function with the contacts list as an argument after the main_loop() function exits to save the updated contact information to the CSV file.

> Remember to create a backup of the "contacts.csv" file before running the program, as the file may not be written correctly the first time.
</details>