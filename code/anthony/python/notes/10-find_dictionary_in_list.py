contacts = [
    {'name': 'Anthony', 'favorite_color': 'blue', 'favorite_fruit': 'apple'},
    {'name': 'Bob', 'favorite_color': 'red', 'favorite_fruit': 'banana'},
    {'name': 'Cindy', 'favorite_color': 'green', 'favorite_fruit': 'grape'},
]


def print_contact():
    name = input("Who's information do you want to see? ")
    found_contact = None

    # Look at every contact in list
    for x in range(len(contacts)):
        # Check to see if its name is equal to the users searched name
        if name == contacts[x]['name']:
            # if so, store that contact dictionary into a variable for later use
            found_contact = contacts[x]

    found_contact['name'] = "Coco"
    print(found_contact)


print_contact()
