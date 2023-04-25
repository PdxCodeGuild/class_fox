"""
Adam
Date: Mar 27th, 2023
Lab 7: Contact List
"""

# Create a CSV file named "contacts.csv"
file = open('contacts.csv', 'r')
# Read the contents of the file using file.read(), and split the contents into lines using the split('\n') method.
lines = file.read().split('\n')
file.close()
# print(lines)

# Extract the header row from the list of lines, and split the header row into a list of header keys using the split(',') method
header_row = lines.pop(0).split(",")
# Initialize an empty list called contacts to store the dictionaries representing each contact
contacts = []

# Iterate over the remaining lines in the CSV file
for info in lines:
    # Split the line into a list of values using the split(',') method.
    info = info.split(",")
    # print(info)
    # Create an empty dictionary called contact.
    contact = {}    
    # Iterate over the header keys and the corresponding values 
    for x in range(len(header_row)):
        contact.update({header_row[0]: info[0]})
        contact.update({header_row[1]: info[1]})
        contact.update({header_row[2]: info[2]})
     # Append the contact dictionary to the contacts list.
    contacts.append(contact)
# print(contacts)

# Create a function called create_contact() 
def create_contact():
    # Prompt the user for the contact's name, favorite fruit, and favorite color.
    user_name = input("What is your name?: ")
    user_fruit = input("What is your favorite fruit?: ")
    user_color = input("What is your favorite color?:  ")
    # Create a dictionary called contact with the keys "name", 
    # "favorite fruit", and  "favorite color", and the values entered by the user.
    contact = {"name":user_name,
    "favorite fruit":user_fruit,
    "favorite color":user_color}
    # Append the contact dictionary to the contacts list
    contacts.append(contact)
    return contacts

# create = create_contact()
# print(create)

# Create a function called retrieve_contact()
def retreive_contact():
    # Prompt the user for the contact's name
    name = input("Who's information do you wanna see: ")
    # Iterate through the contacts list and find the contact with the given name.
    for contact in contacts:
        # Display the contact's information if found,
        # or print a message indicating that the contact was not found.
        if contact['name'] == name:
            print(contact)
            return contact
    else:
        print("Contact was not found")
# retreive = retreive_contact()
# print(retreive)

# Create a function called update_contact() 
def update_contact(): 
    # Prompt the user for the contact's name.
    contact_name = input("What is the contact's name?: ")
    found_contact = None
    # Iterate through the contacts list and find the contact with the given name.
    for x in range(len(contacts)):
        if contact_name == contacts[x]['name']:
         found_contact = contacts[x]
         print(found_contact) 
         update_attributes = input("""What would you like to update 
            1.)name.
            2.)favorite fruit.
            3.)favorite color.
            > """)
        # else:
        #     print("Contact was not found")
        #     break
    
    if update_attributes == '1':
        change_contact = contacts[x]
        change_contact = input("What would you like to change the name to?: ")
        found_contact['name'] = change_contact         
    elif update_attributes == '2':
        change_fruit = input("What would you like to change your favorite fruit to?: ")
        found_contact['favorite fruit'] = change_fruit
    elif update_attributes == '3':
        change_color = input("What do you want to change your favorite color to?: ")
        found_contact['favorite color'] = change_color
    return contacts
# print(contacts)
# update_contact()


# Create a function called delete_contact() 
# that does the following
def delete_contact():
    # Prompt the user for the contact's name.
    name = input("What contact would you like to delete: ")
    # Iterate through the contacts list and find the contact with the given name.
    for x in range(len(contacts)):
        #  If the contact is found, remove the contact from the contacts list.
         if contacts[x]['name'] == name:
            (contacts.remove(contacts[x]))
            return contacts

    # Otherwise, print a message indicating that the contact was not fo
    print("Contact is not in list")
             

# while loop to start CRUD REPL
def main_loop():
    while True:
        contact_edit = input("""Choose one of the following:
    1) Create.
    2) Retrieve.
    3) Update.
    4) Delete.
    5) Quit.
    >  """)
    # if user enters "1" create_contact() will run
        if contact_edit == "1":
            create_contact()
    # if user enters "2" retrieve_contact() will run
        elif contact_edit == "2":
            retreive_contact()
    # if user enters "3" update_contact() will run
        elif contact_edit == "3":
         update_contact()
    # if user enters "4" delete() will run
        elif contact_edit == "4":
            delete_contact()
    # if user enters "5"
        elif contact_edit == "5":
            break
  
# Create a function called save_contacts()
def save_contacts():
    
    # Create a list of header keys
    header_row = ["name", "favorite fruit", "favorite color"]
    
    # Convert the contacts list into a list of CSV lines, 
    # including the header row
    # by iterating over the contacts list and 
    # joining the values of each dictionary with commas.
    for contact in contacts:
        new_contacts_list = contact["name"] + "," + contact["favorite fruit"] + "," + contact["favorite color"]
        
        header_row.append(new_contacts_list)
    
#    Join the list of CSV lines with newline characters (\n)
#  to form a single string.
    new_contacts = "\n".join(header_row)
    file = open("contacts.csv", "w")
    # Open the "contacts.csv" file in write mode
    file.write(new_contacts)
    file.close()
    
# Call the main_loop() function with the contacts list 
# to start the CRUD REPL.
main_loop()
# Call the save_contacts() function so that 
#  after the main_loop() function exits to save the updated contact information to the CSV file.
save_contacts()

    

    
     



    

