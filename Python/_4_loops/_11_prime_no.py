# prime no - no which is divisible only by 1 and itself 

# int input user
# it is a prime no / it is not a prime no

no = int(input("Enter a value : "))

for i in range(2,no):
    if no % i == 0:
        print("It is not a prime no.")
        break
else:
    print("It is a prime number")
