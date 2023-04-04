
def load_contacts():
    file = open("contacts.csv")
    lines = file.read().split("\n")
    file.close()

    header_row = lines.pop(0).split(",")
    contacts = []
    for item in lines:
        item = item.split(",")
        contact = {
            "name": item[0],
            "favorite fruit": item[1],
            "favorite color": item[2]
        }

        contacts.append(contact)

    return contacts, header_row


def save_contacts(contacts, headers):

    data = []
    data.append(",".join(headers))

    for contact in contacts:
        values = list(contact.values())
        data.append(",".join(values))

    data_to_write = "\n".join(data)
    file = open("contacts.csv", "w")
    file.write(data_to_write)
    file.close()


# CRUD REPL

# CREATE
def create_contact(contacts):
    name = input("Enter the name of your new contact: ")
    fav_fruit = input("Enter their favorite fruit: ")
    fav_color = input("Enter their favorite color: ")

    contacts.append({
        "name": name,
        "favorite fruit": fav_fruit,
        "favorite color": fav_color
    })

    return contacts


# RETRIEVE
def retrieve_contact(contacts):
    contact = input("What is the contacts name? ").lower()
    for i in range(len(contacts)):
        if contact == contacts[i]["name"].lower():
            return contacts[i]

    return "Contact not found."


# UPDATE
def update_contact(contacts):
    contact = retrieve_contact(contacts)

    if contact == "Contact not found.":
        print(contact)
        return contacts

    key_to_update = input(
        "What would you like to update? 1) Name. 2) Favorite Color. 3) Favorite Fruit: ")

    match key_to_update:
        case "1":
            contact["name"] = input("What is the new name: ")
        case "2":
            contact["favorite color"] = input(
                "What is the new favorite color: ")
        case "3":
            contact["favorite fruit"] = input(
                "What is the new favorite fruit: ")
        case _:
            print("Invalid choice...")

    return contacts


# DELETE
def delete_contact(contacts):
    contact = retrieve_contact(contacts)
    if contact == "Contact not found.":
        print(contact)
        return contacts
    contacts.remove(contact)
    return contacts


def main_loop():
    contacts, headers = load_contacts()

    while True:
        user_input = input("""
        Choose one of the following:
        C - create
        R - retrieve
        U - update
        D - delete
        or 'done'
        """)

        match user_input:
            case "C":
                contacts = create_contact(contacts)
                print(contacts)
            case "R":
                contact = retrieve_contact(contacts)
                print(contact)
            case "U":
                contacts = update_contact(contacts)
                print(contacts)
            case "D":
                contacts = delete_contact(contacts)
                print(contacts)
            case "done":
                save_contacts(contacts, headers)
                break
            case _:
                print("Invalid choice, try again.")

        save_contacts(contacts, headers)


main_loop()
