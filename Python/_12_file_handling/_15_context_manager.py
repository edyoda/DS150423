# Context Manager

# it automatically closes the file
with open("demo.txt","w") as file: # file = open("demo.txt","w")
    file.write("Hey")

is_close = file.closed
print("Close : ",is_close)



