# name = int(input("Enter your name : "))
# print(name)

try:
    name = int(input('Enter your name:  '))
except:
    name = input('Enter your name:  ')
    
print(name)