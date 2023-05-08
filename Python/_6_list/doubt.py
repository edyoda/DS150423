size = int(input("please enter the total no.of elements"))
lst = []
sorted_list=[]
for i in range (size):
    element = int(input(("please enter the element")))
    lst.append(element)


while size>0:
    big = lst[0]

    for y in (lst):
       if y<big:
        big=y 
    sorted_list.append(big)
    lst.remove(big)
    size-=1    

print(f"sorted list is : {sorted_list} in ascending order")