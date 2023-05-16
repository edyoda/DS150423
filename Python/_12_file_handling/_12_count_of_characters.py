# 1st Way
# ask = input('Desired file name:    ')
# content = input('Enter your content:   ')
# print(f"{ask}.txt")
# file1 = open(f'{ask}.txt', "w+")
# file1.write(content)
# file1.seek(0)
# something = file1.read()
# cur_pos = file1.tell()

# print(f'{something} has {cur_pos} no of charactes')





# 2nd Way
# fileName = str(input("Enter the Name of File: "))
# fileHandle = open(fileName, "r")
# tot = 0
# for char in fileHandle.read():
#     tot = tot+1
# fileHandle.close()

# print(f"\nThere are {tot} Characters available in the File")



# 3rd Way
file = open("demo.txt","w+")
file.write("Good Night All!")
file.seek(0)
data = file.read()

number_of_characters = len(data)

print('Number of characters in text file :', number_of_characters)