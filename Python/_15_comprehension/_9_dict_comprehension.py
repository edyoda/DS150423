keys = [1,2,3,4,5]
values = [10,20,30,40,50]
# {1:10,2:20,3:30,4:40,5:50}

# 1st Way
keyss = [1,2,3,4,5,6,7,8,9,10,11,12]
valuee = [12,45,67,43,56,43,21,89,7,54,66,77]
dict1 = {keyss[i]:valuee[i] for i in range(len(keyss))}
print(dict1)

# 2nd Way
keys = [1, 2, 3, 4, 5]
values = [10, 20, 30, 40, 50]
output = {key: value for key, value in zip(keys, values)}
print(output)
