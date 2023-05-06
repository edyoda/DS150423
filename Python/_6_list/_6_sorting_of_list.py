l = []
num = int(input("Enter number of elements in list: "))
for i in range(1, num + 1):
    ele = int(input("Enter elements: "))
    l.append(ele)

print("og : ",l)

for i in range(len(l)): # i = 6
    for j in range(i + 1, len(l)): # j = 5
          print(f"{l[i]} > {l[j]} = {l[i] > l[j]}")
          if l[i] > l[j]:
           l[i], l[j] = l[j], l[i]
           print(l)

           
print(l)

[4,5,6,3,2]