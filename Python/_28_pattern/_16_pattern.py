#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 
#  * * * *
#   * * *
#    * *
#     *

# for i in range(5,0,-1):
#     print(i*' ',(6-i)*'* ')
# for i in range(2,6):
#     print(i*' ',(6-i)*'* ')

for i in range(1,6):
    for j in range(5-i):
        print(' ', end = '')
    for k in range(i):
        print('*', end = ' ')
    print()
for i in range(4,0,-1):
    for j in range(4-i):
        print(' ', end = '')
    for k in range(i):
        print(' *', end = '')
    print()



