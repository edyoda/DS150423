# funs = dir(str)
# print(funs)

# helping = help(str)
# print(helping)


str1 = "Python sessIon is goinG on!"
print("Original : ",str1)

capital = str1.capitalize() # converts initial letter into capital
print("Capital : ",capital)

ends_with = str1.endswith('on!')
print("Ends with : ",ends_with)

starts_with = str1.startswith("Python")
print("Starts with : ",starts_with)

index_demo = str1.index('s')
print("Index : ",index_demo)

length = len(str1)
print("Length : ",length)

strip_demo = str1.strip()   # remove starting and ending spaces
print("Strip : ",strip_demo)

rstrip_demo = str1.rstrip()   # removes right hand side spaces
print("Rstrip : ",rstrip_demo)

lstrip_demo = str1.lstrip()   # removes left hand side spaces
print("Lstrip : ",lstrip_demo)

title_demo = str1.title()
print("Title : ",title_demo)

istitle_demo = str1.istitle()
print("Is title : ",istitle_demo)

lst = ["Python","Java","CPP"]
join_demo = "#".join(lst)
print("Join : ",join_demo)

replace_demo = str1.replace("python","java")
print("Replace : ",replace_demo)

split_demo = str1.split(" ") # it will split the string on the bases of " " and return list of string
print("Split : ",split_demo, type(split_demo))

for i in split_demo:
    print(i)

swap_demo = str1.swapcase()
print("Swap : ",swap_demo)

is_digit = str1.isdigit()
print("Is digit : ",is_digit)

count_demo = str1.count('s')
print("Count : ",count_demo)

contains_demo = str1.__contains__("thon")
print("Contains : ",contains_demo)

upper_demo = str1.upper()
print("Upper : ",upper_demo)

lower_demo = str1.lower()
print("Lower : ",lower_demo)

is_lower_demo = str1.islower()
print("Islower : ",is_lower_demo)

is_upper_demo = str1.isupper()
print("Isupper : ",is_upper_demo)

enumerate_demo = enumerate(str1) # returns list of tuple which contains each character and it's index
print("Enumerate : ",list(enumerate_demo))

ord_demo = ord("A") # returns ascii value of character
print("Ord : ",ord_demo)

chr_demo = chr(65)
print("Chr : ",chr_demo)

find_demo = str1.find("o",7,14)
print("Find : ",find_demo)

