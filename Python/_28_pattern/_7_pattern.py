# 1  2  3  4
# 5  6  7  8
# 9  10 11 12
# 13 14 15 16

i=1
for x in range(4):
    for y in range(4):
        print(i,end=" ")
        i+=1
    print(" ")    

x=1
for i in range(4):
    for j in range(4):
        print(x,end = '\t')
        x+=1
    print()

value = 1
for i in range(4):
    for j in range(4):
        para = '  ' if value//10==0 else ' '
        print(value, end = para)
        value += 1
    print()