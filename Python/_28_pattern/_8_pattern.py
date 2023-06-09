
#   *  
#   *
# *****
#   * 
#   *

# 11 12 13 14 15
# 21 22 23 24 25
# 31 32 33 34 35
# 41 42 43 44 45
# 51 52 53 54 55

for i in range(5):
    for j in range(5):
        if i == 2 or j == 2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()