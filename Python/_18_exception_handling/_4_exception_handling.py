# lst = [7,8,4,2,1]
# data = lst[5]
# print(data)

lst = [7,8,4,2,1]
try:
    data = lst[7]
except:
    print('no such index found')
    data = None
    
    
print('data is:',data)