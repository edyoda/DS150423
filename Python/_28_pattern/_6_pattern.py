# 1 0 1 0
# 1 0 1 0
# 1 0 1 0
# 1 0 1 0

for i in range(4):
    for j in range(4):
        if j % 2 == 0:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()

# 1 2 3 4
# 5 6 7 8
# 9 10 11 12
# 13 14 15 16
