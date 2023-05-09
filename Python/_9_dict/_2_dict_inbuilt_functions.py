dict1 = {1:"Ram",2:"Laxman",3:"Sita"}
print("Original : ",dict1)

key = dict1.keys()
print(key)

value = dict1.values()
print(value)

# for i in key:
for i in dict1.keys():
    print(i)

# for i in value:
for i in dict1.values():
    print(i)


for k,v in dict1.items():
    print(k,"--->",v)


print(dict1.items())

# dict1.clear()
# print(dict1)

dict2 = dict1.copy()
print(dict2)

dict3 = dict([(1, 'Ram'), (2, 'Laxman'), (3, 'Sita')])
print(dict3)

# dict1.pop(2)
# print(dict1)

dict1[1] = "Raj"
print(dict1)

dict1.update({3:"Gita"})
print(dict1)

# value = dict1[1]
# print(value)

value = dict1.get(1,"Not Present")
print(value)