"""

Version 2
Implement a CRUD REPL

Create a record: ask the user for each attribute, add a new contact to your contact list with the attributes that the user entered.
Retrieve a record: ask the user for the contact's name, find the user with the given name, and display their information
Update a record: ask the user for the contact's name, then for which attribute of the user they'd like to update and the value of the attribute they'd like to set.
Delete a record: ask the user for the contact's name, remove the contact with the given name from the contact list.
If you need help, or get stuck.
Create a function called create_contact() that does the following:

a. Prompt the user for the contact's name, favorite fruit, and favorite color.

b. Create a dictionary called contact with the keys "name", "favorite fruit", and "favorite color", and the values entered by the user.

c. Append the contact dictionary to the contacts list.

Create a function called retrieve_contact() that does the following:

a. Prompt the user for the contact's name.

b. Iterate through the contacts list and find the contact with the given name.

c. Display the contact's information if found, or print a message indicating that the contact was not found.

Create a function called update_contact() that does the following:

a. Prompt the user for the contact's name.

b. Iterate through the contacts list and find the contact with the given name.

c. If the contact is found, ask the user which attribute they'd like to update ("name", "favorite fruit", or "favorite color") and the new value for that attribute. Update the contact's attribute with the new value.

d. If the contact is not found, print a message indicating that the contact was not found.

Create a function called delete_contact() that does the following:

a. Prompt the user for the contact's name.

b. Iterate through the contacts list and find the contact with the given name.

c. If the contact is found, remove the contact from the contacts list. Otherwise, print a message indicating that the contact was not found.

Create a function called main_loop() that does the following:

a. Continuously prompt the user for an action to perform ("C" for create, "R" for retrieve, "U" for update, "D" for delete, or "Q" for quit).

b. Call the appropriate function (created in steps 2-5) based on the user's input, or exit the loop if the user enters "Q".

c. Print a message indicating the current state of the contacts list after each action.

Call the main_loop() function to start the CRUD REPL.

"""



#created a list for contacts
contacts = []


#opened file and read the contense
file = open('contacts.csv', 'r')
lines = file.read().split('\n')
file.close()

#turned every line into a seperated list
headers = lines.pop(0).split(',')

for line in lines:
    line = line.split(',')
    contact = {}
    for x in range(len(headers)):
            
            key = headers[x]       
            value = line[x]
        
            contact.update({key : value})
    contacts.append(contact)

def contact_list():
      contact_name = input("What is the conctacts name? ")
      fav_fruit = input("What is their favorite fruit? ")
      fav_color = input("What is their favorite color? ")
      contact = {"name" : contact_name,
                 "favorite fruit" : fav_fruit,
                 "favorite color" : fav_color}
      contacts.append(contact)
      return contacts

# Create a function called retrieve_contact() that does the following:
def retrieve_contact():
# a. Prompt the user for the contact's name.
    contact = input("What is the contacts name? ")
# b. Iterate through the contacts list and find the contact with the given name.
    for x in range(len(contacts)):
        if contact == contacts[x]['name']:
             return contact
    
    print("Contact not found")
    return contact
# c. Display the contact's information if found, or print a message indicating that the contact was not found
#contact_list()
#Create a function called update_contact() that does the following:
def update_contact():
#a. Prompt the user for the contact's name.
    contact = input("What is the name of the contact you would like to update? ")
#b. Iterate through the contacts list and find the contact with the given name.
    new_contact = None
    for x in range(len(contacts)):
        if contact == contacts[x]['name']:
            new_contact = contacts[x]
    if new_contact == None:
        print("We could not find the contact")
        return

#c. If the contact is found, ask the user which attribute they'd like to update ("name", "favorite fruit", or "favorite color") and the new value for that attribute. Update the contact's attribute with the new value.
    update = input("Would you like to update name, favorite fruit, or favorite color? ")
    if update == 'name':
        updated_name = input("What would you like to update the name too? ")
        new_contact['name'] = updated_name
    elif update == "favorite fruit":
        updated_fruit = input("What would you like to update the fruit too? ")
        new_contact['favorite fruit'] = updated_fruit
    elif update == "favorite color":
            updated_color = input("What would you like to update the color too? ")  
            new_contact['favorite color'] = updated_color
    #d. If the contact is not found, print a message indicating that the contact was not found.
    
    else:
       print("The contact was not found.")
       return contact
#update_contact()



# Create a function called delete_contact() that does the following:
def delete_contact(contacts):
# a. Prompt the user for the contact's name.
    contact = input("What is the name of the contact you would like to delete? ")
# b. Iterate through the contacts list and find the contact with the given name.
    for x in range(len(contacts)):
        if contact == contacts[x]['name']:
            contacts.remove(contacts[x])
    if contact not in contacts:
        print("Contact not found")
        #else:
         #   print("We could not find the contact.")
    return contact

#delete_contact(contacts)

# Create a function called main_loop() that does the following:
def main_loop():
     while True:
# a. Continuously prompt the user for an action to perform ("C" for create, "R" for retrieve, "U" for update, "D" for delete, or "Q" for quit).
        user_input = input("Type C for create, R for retrieve, U for update, D for delete, or Q for quit. ")
# b. Call the appropriate function (created in steps 2-5) based on the user's input, or exit the loop if the user enters "Q".
        if user_input == "C":
             contact_list()
        elif user_input == "R":
             print(retrieve_contact())
        elif user_input == "U":
            update_contact()
        elif user_input == "D":
             delete_contact(contacts)
        elif user_input == "Q":
             break
        else:
             print("That was not a valid input")
# c. Print a message indicating the current state of the contacts list after each action.
        print(contacts)
        return user_input
# Call the main_loop() function to start the CRUD REPL.
#main_loop()

# Create a function called save_contacts() that takes the contacts list as an argument and does the following:
def save_contacts():
# a. Create a list of header keys (e.g., ["name", "favorite fruit", "favorite color"]).
    header_keys = "name, favorite fruit, facorite color"
# b. Convert the contacts list into a list of CSV lines, including the header row, by iterating over the contacts list and joining the values of each dictionary with commas.
    new_contact = []
    new_contact.append(header_keys)
    for contact in contacts:
        contact = list(contact.values())
        new_contact.append(",".join(contact))
    new_contact = "\n".join(new_contact)
     # Open "todos.txt" for writing
    update = open("contacts.csv", "w")
    # Write the todo_list string to the file
    update.write(new_contact)
    update.close()
    print(contacts)
main_loop()
save_contacts()
# c. Join the list of CSV lines with newline characters (\n) to form a single string.

# d. Open the "contacts.csv" file in write mode using the with open statement. This will ensure that the file is properly closed after the block of code is executed.

# e. Write the CSV string to the file.

# Call the load_contacts() function at the beginning of the program to load the contacts from the CSV file into the contacts list.

# Call the main_loop() function with the contacts list as an argument to start the CRUD REPL.

# Call the save_contacts() function with the contacts list as an argument after the main_loop() function exits to save the updated contact information to the CSV file.