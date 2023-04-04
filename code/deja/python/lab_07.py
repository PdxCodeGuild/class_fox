def load_contacts():
   # opening contacts file 
    contacts_file = open("contact-list.csv")
   # reading contents of file
    content = contacts_file.read()
   # closing file 
    contacts_file.close()
    contact_list = content.split("\n")
    contact_list.pop(0)
    
    contacts = []

    for item in contact_list:
        item = item.split(",")
        contact = {}
        name = item[0]
        fruit = item[1]
        color = item[2]
        contact.update({"name": name, "favorite_fruit": fruit, "favorite_color": color})
        contacts.append(contact)
    return contacts

contacts = load_contacts()

def create_contact():
    name = input("Enter name: ")
    fruit = input("Enter favorite fruit: ")
    color = input("Enter favorite color: ")
    contacts.append({"name": name, "fruit": fruit, "color": color})
    return contacts


    
def retrieve_contact():
    user_input = input("Who is the contact you would like to retrieve? ")
    for name in contacts:
      if user_input == name["name"]:
        return name

def update_contact():
    user_input = input("Which contact would you like to update? ") 
    
    for name in contacts:
        if user_input == name["name"]:
            choice = input("Do you want to update name, favorite fruit, or favorite color?")
            new = input("What is the update?")
            name.update({choice:new})
            return name

def delete_contact():
    user_input = input("Who would like to delete? ")
    for name in contacts:
        if user_input == name["name"] :
            contacts.remove(name)
    return contacts

def save_contacts():
    contact_data = ["name,favorite_fruit,favorite_color"]
    for contact in contacts:
        name = contact["name"]
        favorite_fruit = contact["favorite_fruit"]
        favorite_color = contact["favorite_color"]
        values = name + "," + favorite_fruit + "," + favorite_color
        contact_data.append(values)
    data = "\n".join(contact_data) 
    contacts_file = open("contact-list.csv", "w")
    contacts_file.write(data)
    contacts_file.close()
  
save_contacts()
  



 
def main_loop():
    load_contacts()
    while True:
        user_input = input("""Chose one of the following or type 'Done':
    C: Create a new contact
    R: Retrieve a contact
    U: Update a contact
    D: Delete a contact 
    Done
    > """)

        if user_input == "C":
            create_contact()
        elif user_input == "R":
           retrieve_contact()
        elif user_input == "U":
            update_contact()
        elif user_input == "D":
            delete_contact()
        elif user_input == "Done" or "done":
            break
        else:
            print("Invalid input. Please try again.")
main_loop()
save_contacts()






