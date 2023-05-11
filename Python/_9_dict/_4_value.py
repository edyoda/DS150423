# 1st Way
# no = int(input("Enter the number of key value pairs you want to insert : "))
# dicty = {}
# for i in range(no):
#     key = input()
#     value = input()
#     dicty[key] = value
# print(dicty)

# key1 = input("Enter the key : ")
# print(dicty[key1])


# 2nd Way
# no_of_entries = int(input('Enert no. of items you want in your dict:   '))
# lst = []
# for i in range(no_of_entries):
#     key_in = input('Enter your key:   ')
#     value_in = input('Enter your value:   ')
#     tup1 = (key_in, value_in)
#     lst.append(tup1)
# dictionary = dict(lst)
# # print(dictionary)

# inquiry = input('Enter key to search:   ')
# if inquiry in dictionary.keys():
#     value = dictionary[inquiry]
# else:
#     value = 'No such Key is there in this dictionary!'

# print(f'Output:   {value}')



# 3rd Way
no_of_entries = int(input('Enert no. of items you want in your dict:   '))
lst = []
for i in range(no_of_entries):
    key_in = input('Enter your key:   ')
    value_in = input('Enter your value:   ')
    tup1 = (key_in, value_in)
    lst.append(tup1)
dictionary = dict(lst)

inquiry = input('Enter key to search:   ')
value = dictionary.get(inquiry,'No such Key is there in this dictionary!')

print(f'Output:   {value}')



dict1 = {"a":100,"b":10,"c":17,"d":102}
# o/p : d