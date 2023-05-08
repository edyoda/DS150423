# 1st Way
# lst = ["cat","mat","sun","moon","fat","sat"]
# lst1 = []
# for i in lst:
#     if i.endswith("at"):
#         lst1.append(i)
# print(lst1)


# 2nd Way
# lst=["cat","mat","sun","moon","fat","sat"]
# list_=[]
# for x in lst:
#     if x[-1]=='t' and x[-2]=='a':
#         list_.append(x)
# print("The List ends with word 'a' and 't' :""",list_)  



# 3rd Way
lst = ["cat","mat","sun","moon","fat","sat"]
new_lst = []
for i in lst:
    if i.find('at') != -1 :
        new_lst.append(i)
        
print(new_lst)

