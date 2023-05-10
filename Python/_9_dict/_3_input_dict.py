# 1st Way
# no_of_entries = int(input('Enter no. of items you want in your dict:   '))
# lst = []
# for i in range(no_of_entries):
#     key_in = input('Enter your key:   ')
#     value_in = input('Enter your value:   ')
#     tup1 = (key_in, value_in)
#     lst.append(tup1)
# dictionary = dict(lst)
# print(dictionary)



# 2nd Way
no_of_entries = int(input('Enter no. of items you want in your dict:   ')) # 3
lst = []
dictionary = {}
for i in range(no_of_entries):
    key_in = input('Enter your key:   ')
    value_in = input('Enter your value:   ')
    dictionary[key_in] = value_in

print(dictionary)

