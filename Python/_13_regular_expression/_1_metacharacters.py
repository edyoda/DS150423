import re

# data = "Hello"
# res = re.findall("[a-z]",data) # checks for small letters
# print(res)

# if res: print("It matched!")
# else: print("It didn't match!")

# print("It matched!") if res else print("It didn't match!")


# data = "Hello"
# res = re.findall("[A-Z]",data) # checks fo capital letter
# print(res)


# data = "Hello"
# res = re.findall("[A-z]",data) # checks for capital and small letters both
# print(res)


# data = "Hello123"
# res = re.findall("[A-Za-z]",data) # checks for capital and small letters both
# print(res)


# data = "Hello"
# res = re.findall("[a-g]",data) # checks for specific range, letters from a-g
# print(res)


# data = "Hello123"
# res = re.findall("\d",data) # checks for digits
# print(res)


# data = "Hello"
# res = re.findall("^He",data) # checks if data starts with "He"
# print(res)


# data = "Hello"
# res = re.findall("o$",data) # checks if data ends with "o"
# print(res)


# data = "Hello"
# res = re.findall("He.*o",data) # checks if the data starts with "He" and ends with "o" with 0 or more characters in between them ".*"
# print(res)


# data = "Heo"
# res = re.findall("He.+o",data) # checks if the data starts with "He" and ends with "o" with 1 or more characters in between them ".+"
# print(res)


# data = "Hello"
# res = re.findall("He.?o",data) # checks if the data starts with "He" and ends with "o" with 0 or 1 character in between them ".?"
# print(res)


# data = "Hello"
# res = re.findall("He.{2}o",data) # checks if the data starts with "He" and ends with "o" with 1 or more characters in between them ".+"
# print(res)


# data = "Hello all!"
# res = re.findall("all",data) # checks if the data starts with "He" and ends with "o" with 1 or more characters in between them ".+"
# print(res)

data = "Hello all! How are you?"
res = re.findall("all|are|you|Bharati",data) # checks if the data starts with "He" and ends with "o" with 1 or more characters in between them ".+"
print(res)