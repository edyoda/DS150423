file = open("testing.txt","a+")
file.write("Bye")
data = file.read()
print(data)