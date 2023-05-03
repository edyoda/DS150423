print("The divisible by 5 but not 2 between 10 and 1000:",end=" ")
for x in range(10,1001):
    if x%5==0 and x%2!=0:
        print(x,end=" ")