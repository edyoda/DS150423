age = int(input("Enter your age : "))

if age >= 18:
    qualification = int(input("Enter your qualification (in number) : "))
    if qualification > 12:
        print("You are hired!")
    else:
        print("Complete your education and re-apply.")
else:
    print("You are still a kid!")

# int input
# even or odd