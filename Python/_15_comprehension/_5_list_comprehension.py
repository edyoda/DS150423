lst = [4,6,10,9,3,5,11,45]
# 0,3,5,6,9
# [6,10,3]

lst = [4, 6, 10, 9, 3, 5, 11, 45]
output = [lst[num] for num in range(len(lst)) if num not in [0, 3, 5, 6, 9]]
print(output)

