no = 3982384793284 # 3

count = 0

# mod = no % 10   # 4
# count += 1      # 1
# no = no // 10   # 65

# mod = no % 10   # 5
# count += 1      # 2
# no = no // 10   # 6

# mod = no % 10   # 6
# count += 1      # 3
# no = no // 10   # 0

no = 3897
while no!=0 :
    mod = no % 10   #  7     # 9    # 8    # 3
    count += 1      #  1     # 2    # 3    # 4
    no = no // 10   #  389   # 38   # 3    # 0

print(count)



