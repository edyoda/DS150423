import json

file = open(r"C:\Users\vashi\OneDrive\Documents\DS150423\Python\_21_json_file_handling\json_file.json","r")

# it read the file and converted json data into dict and returned it to us
data = json.load(file)
print(data)
print(type(data))


file1 = open(r"C:\Users\vashi\OneDrive\Documents\DS150423\Python\_21_json_file_handling\json_file1.json","w")
# it converted the dict into json and then stored it inside the file
json.dump(data,file1)
