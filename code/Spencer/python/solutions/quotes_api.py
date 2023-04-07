"""
Lab 10: Quotes API
For this lab we'll be using the Favqs Quotes API to first get a random quote, 
and then allow the user to find quotes by keyword. To accomplish this we'll be using the requests library.

Version 1: Get a Random Quote
The URL to get a random quote is https://favqs.com/api/qotd, send a request here,
 parse the JSON in the response into a python dictionary, and show the quote and the author.

Version 2: List Quotes by Keyword
The Favqs Quote API also supports getting a list of quotes associated with a given keyword
 https://favqs.com/api/quotes?page=<page>&filter=<keyword>. Prompt the user for a keyword, 
 list the quotes you get in response, and prompt the user to either show the next page or enter a new keyword.
 You can use string concatenation to build the URL.

> enter a keyword to search for quotes: nature
25 quotes associated with nature - page 1
<list of quotes>
> enter 'next page' or 'done': next page
25 quotes associated with nature - page 2
<list of quotes>
> enter 'next page' or 'done': done
> enter a keyword to search for quotes:
This API endpoint requires an API key be included in a request header. You can find documentation of specifying request headers here and documentation on authorization with the Favqs API here under "Authorization".

headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
Other Quote APIs
Programming Quotes
Quotes Garden
get random quote https://quote-garden.herokuapp.com/quotes/random
get quotes by keyword https://quote-garden.herokuapp.com/quotes/search/<keyword/
"""

import requests
search_word = input("Enter a key word you would like to search for. ")
page = 1
#print(type(searched_quote["quotes"]))
#print(searched_quote)
while True:

    url = requests.get(f"https://favqs.com/api/qotd", headers={'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})
    keyword_url = requests.get(f"https://favqs.com/api/quotes?page={page}&filter={search_word}", headers={'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})
    quote_of_the_day = url.json()
    searched_quote = keyword_url.json()

    for i in range(len(searched_quote["quotes"])):
        print(f'\nAuthor: {searched_quote["quotes"][i]["author"]} \nQuote: {searched_quote["quotes"][i]["body"]} \n')
    next_page = input("Enter 'next page' or 'done': ")
    if next_page == "next page":
            page = page + 1
    elif next_page == "done": 
        search_again = input("Would you like to search for another key word? ")

        if search_again == "yes":
            page = 1
            search_word = input("Enter a key word you would like to search for. ")
        
        elif search_again == "no":
            break
        else:
            print("That was not a valid input, please type yes or no")

        




#print(f'Author: {searched_quote["quotes"]["author"]} \nQuote: {searched_quote["quotes"]["body"]}')

#print(dad_jokes["results"][0])