# Logical Operator - it returns bool value

# and - it will return True only if all the mentioned conditions are True
# or  - it will return True only if atleast one of the mentioned conditions is True
# not - it returns the reverse of the actual result

no1 = int(input("Enter your first number : ")) # 4
no2 = int(input("Enter your second number : ")) # 4
no3 = int(input("Enter your third number : ")) # 3

and_demo = no1 == no2 and no1 > no3 and no2 > no3
print("And : ",and_demo)

or_demo = no1 < no2 or no1 < no3
print("Or : ",or_demo)

not_demo = not(no1 == no2 and no1 > no3)
print("Not : ",not_demo)