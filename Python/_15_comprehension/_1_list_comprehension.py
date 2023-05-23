# List Comprehension - it is use for creating new list from another list

# for i in lst:
#     if <condition>:
#         expression

# syntax : 
# [expression for i in lst if <condition>]

nums = [6,4,3,7,4,3,5]

# lst = []
# for i in nums:
#     lst.append(i)

# print(lst)

lst = [i for i in nums]
print(lst)