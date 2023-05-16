file = open("contacts.txt","r")
data = file.readlines()

contacts  = []
for i in data:
    i = i.replace("\n","")
    if i.isdigit() and len(i) == 10:
        contacts.append(i)

print(contacts)