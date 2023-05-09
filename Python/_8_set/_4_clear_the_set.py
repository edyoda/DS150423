# # 1st Way
# set1 = set()
# iteraaation = int(input('How many input yu want to give?  '))
# for i in range(iteraaation):
#     set_add = int(input('Enter your input:  '))
#     set1.add(set_add)

# print(f'Your Input is {set1}')
# set2 = set1.copy()
# print('\n Now to clear the set \n')

# for i in set2:
#     set1.remove(i)

# print(f'Your Cleared is {set1}')


# # 2nd Way
# set1 = set()


no = int(input("Enter the number of values you want to insert : "))
lst = []
for i in range(no):
    ele = int(input())
    lst.append(ele)
set1 = set(lst)
print(set1)

set2 = set1.copy()
for x in set2:
    set1.remove(x)
    
print(set1)


# Python program to find common elements in three lists using sets