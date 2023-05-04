user = int(input("Enter a number: ")) # 5 - 1 - 5 

# initialize factorial to 1
factorial = 1

# loop multiply factorial by each number
for i in range(1, user+1):
    factorial *= i # factorial = factorial * i

print("Factorial of", user, "is", factorial)

# display all the numbers which are divisible by 5 but not 2 between 10 - 1001