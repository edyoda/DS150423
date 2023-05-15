file = open("test.txt","r+")
file.write("Hello")
data = file.read()
print(data)