from functools import reduce

lst = [6,7,23,8,4,3,39,76,10]

# create a function, which takes list as parameter and 
# returns the sum of all the elements in the list

# def sum(lst):
#     total = 0
#     for i in lst:
#         total += i
#     return total
# total_of_element = sum(lst)
# print(total_of_element)


def sum(lst1,lst2):
    return lst1 + lst2
total_of_element = reduce(sum,lst)
print(total_of_element)

reduced_numbers = reduce(lambda lst1, lst2: lst1+lst2, lst)
print(reduced_numbers)



