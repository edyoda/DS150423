# * * * * *
#   * * * *
#     * * * 
#       * *
#         *

for i in range(5):
    for j in range(i):
        print(" ", end=" ")
    for k in range(5-i):
        print("*", end=" ")
    print()


for i in range(5):
    print(i*" ",(5-i)*"*")