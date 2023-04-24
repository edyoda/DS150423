# ==
# !=
# >
# <
# >=
# <=

# NOTE : all the above operators will return bool value

no1 = int(input("Enter your no1 : "))
no2 = int(input("Enter your no2 : "))

eq = no1 == no2
print("Equal : ",eq)

noteq = no1 != no2
print("Not equal : ",noteq)

greaterthan = no1 > no2
print("Greater than : ",greaterthan)

lessthan = no1 < no2
print("Less than : ",lessthan)

greaterthaneq = no1 >= no2
print("Greater than equal to : ",greaterthaneq)

lessthaneq = no1 <= no2
print("Less than equal to : ",lessthaneq)
