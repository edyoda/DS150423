# 1st Way
text = input("Enter the string: ")
unique = ""
for i in text:
    if i not in unique:
        unique += i
print(len(unique))


# 2nd Way
string=input("Enter a Name: ")
leng=len(set(string))
print(leng)