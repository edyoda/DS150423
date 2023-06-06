import requests

url = "http://ip.jsontest.com/"

response = requests.get(url).json()
print(response["ip"])