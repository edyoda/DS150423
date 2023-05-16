file = open("demo.txt")
print(file.read())
# file.close()

is_close = file.closed
print("Is close : ",is_close)

file_name = file.name
print("File name : ",file_name)

mode = file.mode
print("File Mode : ",mode)