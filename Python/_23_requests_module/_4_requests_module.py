import requests

url = "https://mocki.io/v1/d4867d8b-b5d5-4a48-a4ab-79131b5809b8"
response = requests.get(url).json()

# print(response)
task1 = response[3]['name']
print('task1:  ', task1)
task2 = {response[1]['name']:response[2]['city']}
print('task2:  ', task2)