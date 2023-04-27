# Type Conversion / Type Casting

# int()
# float()
# str()
# bool()
# complex()


# no = -1
# print("int into int : ",int(no),"----->",type(int(no)))
# print("int into float : ",float(no),"----->",type(float(no)))
# print("int into str : ",str(no),"----->",type(str(no)))
# print("int into complex : ",complex(no),"----->",type(complex(no)))
# print("int into bool : ",bool(no),"----->",type(bool(no)))


# percentage = 89.9
# print("float into int : ",int(percentage),"----->",type(int(percentage)))
# print("float into float : ",float(percentage),"----->",type(float(percentage)))
# print("float into str : ",str(percentage),"----->",type(str(percentage)))
# print("float into complex : ",complex(percentage),"----->",type(complex(percentage)))
# print("float into bool : ",bool(percentage),"----->",type(bool(percentage)))


# name = "Ram"
# # print("str into int : ",int(name),"----->",type(int(name)))
# # print("str into float : ",float(name),"----->",type(float(name)))
# print("str into str : ",str(name),"----->",type(str(name)))
# # print("str into complex : ",complex(name),"----->",type(complex(name)))
# print("str into bool : ",bool(name),"----->",type(bool(name)))

#! NOTE : if string has only digits then it will allow you to convert it 
# into int,float and complex else it will not


# qualified = False 
# print("bool into int : ",int(qualified),"----->",type(int(qualified)))
# print("bool into float : ",float(qualified),"----->",type(float(qualified)))
# print("bool into str : ",str(qualified),"----->",type(str(qualified)))
# print("bool into complex : ",complex(qualified),"----->",type(complex(qualified)))
# print("bool into bool : ",bool(qualified),"----->",type(bool(qualified)))


# comp = 1+1j
# # print("complex into int : ",int(comp),"----->",type(int(comp)))
# # print("complex into float : ",float(comp),"----->",type(float(comp)))
# print("complex into str : ",str(comp),"----->",type(str(comp)))
# print("complex into complex : ",complex(comp),"----->",type(complex(comp)))
# print("complex into bool : ",bool(comp),"----->",type(bool(comp)))



# list()
# set()
# tuple()
# dict()

lst = [7,5,3,7,7,7,7]
print(lst)

unique = set(lst)
print(unique)

lst1 = list(unique)
print(lst1)