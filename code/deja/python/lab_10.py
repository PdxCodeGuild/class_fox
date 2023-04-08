import requests
#Version 1:
quote = requests.get("https://favqs.com/api/qotd")
quote = quote.json()
quote = quote['quote']['body']
author = requests.get("https://favqs.com/api/qotd")
author = author.json()
author = author['quote']['author']
print(quote,author)

#Version 2
keyword = input("Enter a keyword to search for quotes: ")
quote_keyword = f"https://favqs.com/api/quotes?page=1&filter={keyword}"
response = requests.get(quote_keyword, headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})
response = response.json()
response = response['quotes']
response = list(response)
def get_quotes():
    for x in range(len(response)):
        quote = response[x]['body']
        print(quote)
    print(f"There are {len(quote)} quotes associated with '{keyword}' on page 1.")
get_quotes()
page = 1
quote_keyword = f"https://favqs.com/api/quotes?page={page}=1&filter={keyword}"
while True:
    user_input = input("Enter 'next page' or 'done': ")
    if user_input == "next page":
            page = int(page) + 1
            quote_keyword = f"https://favqs.com/api/quotes?page={page}=1&filter={keyword}"
            response = requests.get(quote_keyword, headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})
            response = response.json()
            response = response['quotes']
            response = list(response)
            for x in range(len(response)):
                 quote = response[x]['body']
                 print(quote)
            print(f"There are {len(quote)} quotes associates with '{keyword}' on page {page}")
    if user_input == "done":
        break


