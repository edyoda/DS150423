#     *
#    * *
#   * * *
#  * * * * 
# * * * * *

for i in range(1,6):
    for j in range(6-i):
        print(" ", end="")
    for j in range(i):
        print("*", end=" ")
    print()

for i in range(5,0,-1):
    print(i*" ",(6-i)*"* ")
