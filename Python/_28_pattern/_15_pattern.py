#     A 
#    B C 
#   C D E
#  D E F G
# E F G H I

for i in range(1,6):
    for j in range(5-i):
        print(' ', end = '')
    for k in range(i):
        print(chr(64+k+i), end = ' ')
    print()

#     *
#    * *
#   * * *
#  * * * * 
#   * * *
#    * *
#     *