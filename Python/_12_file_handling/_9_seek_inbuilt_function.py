# seek() ---> use to change the position of cursor

# seek(offset,from_where)

# offset     - no. of position
# from_where - reference

# from_where
# 0 - beginning 
# 1 - current position of the cursor
# 2 - end

# but for text file, it will only accept 0, which is bydefault

file = open("coding.txt","w")

cur_pos = file.tell()
print("Before : ",cur_pos)

file.seek(10,0)

cur_pos = file.tell()
print("After : ",cur_pos)


