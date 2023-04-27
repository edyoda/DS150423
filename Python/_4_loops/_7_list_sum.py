# lst = [2,3,5,1,6]
# sum = 0
# for x in lst:     # x=3
#     sum += x      # sum = x + sum  # sum = 2 + 0 # 3 + 2 =  #17
# print(sum)



total = 0
list1 = [2,3,5,1,6]
for ele in range(0, len(list1)):
    total = total + list1[ele]
print("Sum of all elements in given list: ", total)