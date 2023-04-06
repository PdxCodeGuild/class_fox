"""
# Lab 10: Quotes API

For this lab we'll be using the [Favqs Quotes API](https://favqs.com/api) to first get a
random quote, and then allow the user to find quotes by keyword. To accomplish this we'll
be using the `requests` library.


## Version 1: Get a Random Quote

The URL to get a random quote is [https://favqs.com/api/qotd](https://favqs.com/api/qotd),
send a request here, parse the JSON in the response into a python dictionary, and show the
quote and the author.

## Version 2: List Quotes by Keyword

The Favqs Quote API also supports getting a list of quotes associated with a given keyword
`https://favqs.com/api/quotes?page=<page>&filter=<keyword>`. Prompt the user for a keyword,
list the quotes you get in response, and prompt the user to either show the next page or
enter a new keyword. You can use string concatenation to build the URL.

This API endpoint requires an API key be included in a request header. You can find
documentation of specifying request headers
[here](https://requests.readthedocs.io/en/master/user/quickstart/#custom-headers)
and documentation on authorization with the Favqs API [here](https://favqs.com/api/)
under "Authorization".

```python
headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
```

"""
import requests


def qotd():
    url = "https://favqs.com/api/qotd"
    response = requests.get(url)
    quotes = response.json()
    print(f"Author: {quotes['quote']['author']}\n")
    print(f"Body: {quotes['quote']['body']}")


search_word = input("Enter a keyword you would like to search for: ")
page = 1

while True:
    search_url = f"https://favqs.com/api/quotes?page={page}&filter={search_word}"
    headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}

    response = requests.get(search_url, headers=headers)
    response = response.json()
    last_page = response["last_page"]
    response = response["quotes"]

    for x in range(len(response)):
        quote = response[x]["body"]
        author = response[x]["author"]
        print(quote)
        print(f"\t-{author}")
        print()
    print(f"There are {len(response)} quotes associated with `{search_word}`")

    if last_page == False:
        next_page = input("Enter 'next page' or 'done': ")
        if next_page == "next page":
            page = page + 1
            continue

    new_search = input("Do you want to search for a new keyword? y/n: ")
    if new_search == "y":
        search_word = input("Enter new keyword: ")
        page = 1
    else:
        break
