import requests
# # response value to get information of dad jokes
response = requests.get(f"https://icanhazdadjoke.com/",
                        headers = {"accept":"application/json"})
dad_joke = response.json()
# # print put dad jokes using json() method
# print(dad_joke)

# ask user to enter a word to find a dad joke
search_term = input("Enter a word: ")
url = requests.get(f"https://icanhazdadjoke.com/search?term={search_term}",
                        headers = {"accept":"application/json"})
joke = url.json()
print(f'joke:{joke["results"][0]}')

