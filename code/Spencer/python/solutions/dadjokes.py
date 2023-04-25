"""
Lab 9: Dad Joke API
Use the Dad Joke API to get a dad joke and display it to the user. You may want to also use time.sleep to add suspense.

Part 1
Use the requests library to send an HTTP request to https://icanhazdadjoke.com/ with the accept header as application/json. 
This will return a dad joke in JSON format.
 You can then use the .json() method on the response to get a dictionary. Get the joke out of the dictionary and show it to the user.

Part 2 (optional)
Add the ability to "search" for jokes using another endpoint. Create a REPL that allows one to enter a search 
term and go through jokes one at a time. You can also add support for multiple pages.
"""
import requests

search_word = input("Enter a key word you would like to search for. ")
url = requests.get(f"https://icanhazdadjoke.com/", headers={"accept":"application/json"})
search_url = requests.get(f"https://icanhazdadjoke.com/search?term={search_word}", headers={"accept":"application/json"})
dad_jokes = search_url.json()

print(dad_jokes["results"][0])

counter = 0
while True:
    another_joke = input("Would you like to hear another joke? ")
    if counter > 3:
        print("That was the end of the dad jokes. ")
    if another_joke == "yes":
        print(dad_jokes["results"][counter])
        counter = counter + 1
    elif another_joke == "no":
        break
    else:
        print("That was not a valid input, please type yes or no") 


print(dad_jokes)
