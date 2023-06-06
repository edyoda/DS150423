import requests

url = "https://jsonplaceholder.typicode.com/todos"

request_data = {
    'rno' : 100,
    'name': 'Bharati'
}

response = requests.request('POST',url,json=request_data)
print(response.json())

response = requests.post(url,json=request_data)
print(response.json())