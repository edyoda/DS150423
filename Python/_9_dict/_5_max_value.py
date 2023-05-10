# 1st Way
# dict1 = {"a":100,"b":10,"c":17,"d":102}
# reference = 0
# for k,v in dict1.items():
#     if v > reference:  # 100 > 0 | 10 > 100 | 17 > 100 | 102 > 100
#         reference = v  # 100                           | 102
#         output = k     # a                             | d

# print(output)



# 2nd Way
dict1 = {"a":100,"b":10,"c":17,"d":102}
max_no = max(dict1,key=dict1.get)
print("Maximum Value Key: ",max_no)