# Dict Comprehension - it is use to create new dict from another type of data

str1 = "Python"
# {'p':'P','y':'Y','t':'T','h':'H','o':'O','n':'N'}

dict_comp = {i.lower():i.upper() for i in str1}
print(dict_comp)


keys = [1,2,3,4,5]
values = [10,20,30,40,50]
{1:10,2:20,3:30,4:40,5:50}