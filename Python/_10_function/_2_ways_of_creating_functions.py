# without parameter and without return statement

# def addition():            
#     no1 = int(input("Enter no1 : "))
#     no2 = int(input("Enter no2 : "))
#     add = no1 + no2
#     print(f'Addition : {add}')

# addition()




# without parameter and with return statement

# def subtraction():            
#     no1 = int(input("Enter no1 : "))
#     no2 = int(input("Enter no2 : "))
#     sub = no1 - no2
#     return sub

# answer = subtraction()
# print(f"Subtraction : {subtraction()}")


# with parameter and without return statement
# def multiplication(no1,no2): # parameters / arguments
#     mul = no1 * no2
#     print(f"Multiplication : {mul}")

# multiplication(5,6)


# with parameter and with return statement
def division(no1,no2):
    div = no1 / no2
    return div

no1 = int(input("Enter a no1: "))
no2 = int(input("Enter a no2: "))

data = division(no1,no2)
print("Division: ",data)


