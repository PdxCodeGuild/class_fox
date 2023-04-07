"""
Adam
April 4th, 2023
Lab 10: Quotes API
"""

# version 1
import requests
# requesting to allow to pull info from api
response = requests.get("https://favqs.com/api/qotd")
# get info from website and convert it to json
quotes = response.json()
# print(quotes)
# print(f'author:{quotes["quote"]["author"]}')
# print(f'quote:{quotes["quote"]["body"]}')
# print("----------------------------")


# version 2

keyword = input("enter a keyword: ")
page = 1
url = requests.get(f"https://favqs.com/api/quotes?page={page}&filter={keyword}", headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})
response_2 = url
list_quotes = response_2.json()
number_of_quotes = len(list_quotes["quotes"][0])
print(f"{number_of_quotes} quotes associated with keyword: {keyword} - page: {page}")

page = 1
for x in range(len(list_quotes["quotes"])):
        print(f'\nquote:{list_quotes["quotes"][x]["body"]}')
        print(f'author: {list_quotes["quotes"][x]["author"]}')
new_page = input("Enter 'new page' or 'done' to quit: ")
while True:
    if new_page == "new page":
        # add a new number to page if the user decides to  pick new page
        page = page + 1
        print(f"{number_of_quotes} quotes associated with keyword: {keyword} - page: {page}")
        print(f'\nquote:{list_quotes["quotes"][x]["body"]}')
        print(f'author: {list_quotes["quotes"][x]["author"]}')
    elif new_page == "done":
        # ask user if they want to look up a new word
        # if yes let them enter a new one, if not break
        new_keyword = input("Do you want to look up another word?: ")
    if new_keyword == "yes":
        keyword_2 = input("enter a keyword: ")
    elif new_keyword == "no":
        break
    
    




