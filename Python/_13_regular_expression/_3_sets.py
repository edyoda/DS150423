import re

# data = "Python"
# res = re.findall("[tjkn]",data) # checks for t,j,l,n
# print(res)


# data = "The rain in Spain"
# res = re.findall("[^arn]",data) # checks for all charactes except a,r,n
# print(res)


# data = "The rain in Spain"
# res = re.findall("[c-m]",data) # checks for all charactes between c-m
# print(res)

# data = "The rain in Spain87"
# res = re.findall("[9857]",data) # checks for 9,8,5,7
# print(res)

# data = "78 92"
# res = re.findall("[0-8][5-9]",data) # checks for first digit between 0-8 and second digit between 5-9
# print(res)

# data = "The rain in Spain ____ #"
# res = re.findall("[@#]",data) # checks for @,#
# print(res)

# data = "The rain in Spain"
# res = re.findall("[a-z]{2}",data) # checks for 4 lower letters
# print(res)