import requests

response = requests.get("https://icanhazdadjoke.com/", headers={"accept": "application/json"})
response = response.json()
response = response['joke']
print(response)
