# function

# set a code which you might need to reuse, you can put it 
# inside a function and use it

# DRY - Don't repeat yourself

# syntax : 
# def <function_name>():
#     // body

def addition():            # defining the function
    no1 = int(input("Enter no1 : "))
    no2 = int(input("Enter no2 : "))
    add = no1 + no2
    print(f'Addition : {add}')

# addition()                 # calling the function
# addition()

def looping():
    for x in range(21,35,3):
        print(x)

looping()