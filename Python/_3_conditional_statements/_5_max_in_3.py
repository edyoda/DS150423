no1 = int(input("Enter the first number : "))
no2 = int(input("Enter the second number : "))
no3 = int(input("Enter the third number : "))

if no1>no2 and no1>no3 :
    print(no1," no1 is greatest.")
elif no2>no1 and no2>no3 :
    print(no2," no2 is greatest.")
elif no1 == no2 == no3:
    print("all values are equal")
else:
    print(no3," no3 is greatest.")