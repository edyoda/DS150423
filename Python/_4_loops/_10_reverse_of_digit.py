num = int(input("enter the positive integer number :")) # 123
rev = 0
while num>0 :
    mod = num%10          # 1
    rev = rev * 10 + mod  # 3 * 10 + 2  = 321
    num = num//10         # 0
    
print ("reverse is : ",rev)



