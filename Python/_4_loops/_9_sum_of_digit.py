num = int(input("enter the positive integer number :"))
sum = 0
while num>0 :
    mod = num%10
    sum += mod
    num = num//10
    
print ("sum is : ",sum)



