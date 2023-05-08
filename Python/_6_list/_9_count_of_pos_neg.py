# 1st Way
# list1 = []
# iteraaation = int(input('How many input yu want to give?  '))
# for i in range(iteraaation):
#     lst_app = int(input('Enter your input:  '))
#     list1.append(lst_app)
# pos_count = 0
# neg_count = 0

# for num in list1:
#     if num >= 0:
#         pos_count += 1 # pos_count = pos_count + 1
#     else:
#         neg_count += 1
# print("Positive numbers in the list: ", pos_count)
# print("Negative numbers in the list: ", neg_count)




# 2nd Way
# size=int(input("Enter a size: "))
# lst=[]
# count_positive=0
# count_negative=0
# for x in range(size):
#     print("Enter a element",x+1,":",end=" ")
#     ele=int(input())
#     lst.append(ele)

# for x in range(size):
#     if lst[x]>0:
#         count_positive+=1
#     else:
#         count_negative+=1
# print("Count of Positive numbers:",count_positive)
# print("Count of Negative numbers:",count_negative)



lst = []
iteraaation = int(input('How many input yu want to give?  '))
for i in range(iteraaation):
    lst_app = int(input('Enter your input:  '))
    lst.append(lst_app)

print(f'Your input is {lst}')

positi = 0
negati = 0
zerooo = 0
for i in lst :
    if i > 0 :
        positi += 1
    elif i < 0 :
        negati += 1
    elif i == 0:
        zerooo += 1
    else:
        print('Your number is not an integer')

print(f'No of positive integers {positi}')
print(f'No of negative integers {negati}')
print(f'No of neutral integers {zerooo}')


