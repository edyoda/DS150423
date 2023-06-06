import requests

url = "https://randomuser.me/api/"

response = requests.request('GET',url).json()
print(response)
print(response['results'][0]['location']['street']['number'])