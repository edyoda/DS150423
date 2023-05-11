def get_input():
    no1 = int(input("Enter no1 : "))
    no2 = int(input("Enter no2 : "))
    return no1,no2

def addition():            
    no1,no2 = get_input()
    add = no1 + no2
    print(f'Addition : {add}')

def subtraction():            
    no1,no2 = get_input()
    sub = no1 - no2
    return sub

def multiplication(no1,no2): 
    mul = no1 * no2
    print(f"Multiplication : {mul}")

def division(no1,no2):
    div = no1 / no2
    return div


addition()

answer = subtraction()
print(f"Subtraction : {answer}")

no1,no2 = get_input()
multiplication(no1,no2)

no1,no2 = get_input()
data = division(no1,no2)
print("Division: ",data)


