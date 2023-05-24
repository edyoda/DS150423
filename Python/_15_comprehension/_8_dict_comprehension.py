# Dict Comprehension - it is use to create new dict from another type of data

str1 = "Python"
# {'p':'P','y':'Y','t':'T','h':'H','o':'O','n':'N'}

dict_comp = {i.lower():i.upper() for i in str1}
print(dict_comp)

