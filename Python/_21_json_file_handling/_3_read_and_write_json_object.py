import json

data = """{
    "name":"Bharati",
    "female":true,
    "qualification":null,
    "day":false
}"""

# convert json object to dict
dict_obj = json.loads(data)
print(dict_obj)
dict_obj["name"] = "Swaraj"
print(type(dict_obj))

# convert dict object to json
json_obj = json.dumps(dict_obj)
print(json_obj)




