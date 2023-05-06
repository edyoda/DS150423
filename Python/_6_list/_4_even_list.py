# 1st Way
# lst = []
# iteraaation = int(input('How many input yu want to give?  '))
# for i in range(iteraaation):
#  lst_app = int(input('Enter your input:  '))
#  lst.append(lst_app)

# print(f'Your input is {lst}')

# for j in lst:
#     if j%2 != 0 :
#        lst.remove(j)

# print(f'Even number list is {lst}')



# 2nd Way
length_1 = int(input("please enter the total no.of elements"))
lst = []
even_list = []
for i in range (length_1):
    element = int(input(("please enter the element")))
    lst.append(element)

for x in lst:
    if x%2==0:
        even_list.append(x)


print(f"The even number list is : {even_list}")


