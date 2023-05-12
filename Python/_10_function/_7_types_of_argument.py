# types of arguments 

# 1. required/postional argument
# 2. default argument
# 3. keyword argument
# 4. variable-length argument
#       4.1. Arbitrary positional argument
#       4.2. Arbitrary keyword argument




# required / positional argument

# def add(no1,no2):
#     return no1 + no2

# result = add(2,3)
# print(result)





# default argument
# def add(no1,no2=90):
#     return no1 + no2

# result = add(6,100)
# print(result)





# keyword argument
# def add(no1,no2=90,no3=10):
#     return no1 + no2 + no3

# result = add(no1=100,no3=200)
# print(result)





# variable-length argument
# 1. arbitary positional argument
# args
# tuple
# *

# def users(*args):
#     print(args)
#     print(type(args))
#     print(args[10])
#     data = args[10]
#     print(data.upper())

# users(1,2,3,4,5,6,7,8,9,10,"Bharati",6.7)




# 2. arbitary keyword argument
# kwargs
# dict
# **

def users(**kwargs):
    print(kwargs)
    print(type(kwargs))
    print(kwargs["two"])

users(one="Raj",two="Ram")




