dict1 = {"a":10,"b":15,"c":10,"d":100}
dict2 = dict1.copy()
index = 0
for i in dict2.keys():               # [a,b,c,d]   # i = b
    index += 1
    list1 = dict2.keys()[index:]                   # list1 = [c,d]
    for j in list1:                                # j = d
        if dict2[i] == dict2[j]:
            dict1.pop(i)
            dict1.pop(j)

print(dict1)     