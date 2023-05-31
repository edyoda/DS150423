import pdb # python debugger

def addition(no1,no2):
    add = no1 + no2
    return add

# pdb.set_trace()
no1 = input("Enter a no1 : ")
no2 = input("Enter a no2 : ")
res = addition(no1,no2)
print("Addition : ",res)


# Command to run it in pdb mode :
# python -m pdb .\_1_pdb_demo.py