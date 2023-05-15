# tell() ---> returns the position of cursor

file = open("demo.txt","w")

cur_pos = file.tell()
print("Before : ",cur_pos)

file.write("Good Evening!")

cur_pos = file.tell()
print("After : ",cur_pos)
