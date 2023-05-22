lst = [6,7,23,8,4,3,39,76,10]

# create a function, which takes list as parameter and returns a new list with 
# all the even values from the parameter list

# def is_even_num(lst):
#     even = []
#     for i in lst:
#         if i % 2 == 0:
#             even.append(i)
#     return even
# even_lst = is_even_num([6, 7, 23, 8, 4, 3, 39, 76, 10])
# print(even_lst)


# def is_even_num(lst):
#     return lst % 2 == 0
# even_lst = list(filter(is_even_num,lst))
# print(even_lst)


even_lst = list(filter(lambda lst:lst % 2 == 0,lst))
print(even_lst)
