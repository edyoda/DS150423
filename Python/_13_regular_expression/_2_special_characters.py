import re

# data = "Python is high level programming language"
# res = re.findall('\APython is',data) # checks if string starts with "Python is"
# print(res)

# data = "Python is high level programming language"
# res = re.findall('uage\Z',data) # checks if string ends with "uage"
# print(res)

# data = "Python is high level programming language"
# res = re.findall(r'\bpro',data) # checks if any word is starting with "pro"
# print(res)

# data = "Python is high level programming language"
# res = re.findall(r'\Bing',data) # checks if any word is ending with "ing"
# print(res)

# data = "Python is high level programming language 123"
# res = re.findall(r'\d',data) # checks for digits
# print(res)

# data = "Python is high level programming language 123"
# res = re.findall(r'\D',data) # checks for non-digits
# print(res)

# data = "Python is high level programming language 123"
# res = re.findall(r'\s',data) # checks for spaces
# print(res)

# data = "Python is high level programming language 123"
# res = re.findall(r'\S',data) # checks for non-spaces
# print(res)

data = "Python123@ "
res = re.findall(r'\w',data) # checks for a-z,A-Z,0-9,_
print(res)

data = "Python123@ "
res = re.findall(r'\W',data) # checks for not (a-z,A-Z,0-9,_)
print(res)


