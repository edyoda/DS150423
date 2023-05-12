# types of variable

# 1. local variable
# - are the variables which are define inside the function
# - scope is also within the function itself
# - the parameters/arguments are also local variables

# 2. global variable
# - are the variables which are define outside the function
# - scope is within that .py file
# - we can define global variable in function 
#   syntax : 
#       global <variable_name>
#       <variable_name> = <value>

school_name = "Edyoda"       # global variable

def info(rno):
    name = "Bharati"         # local variable
    global college_name      # global variable
    college_name = "Coder"
    print(name)
    print(rno)
    print("inside function : ",college_name)    
    print("inside function : ",school_name)    

info(10)
print("outside function : ",school_name)
print("outside function : ",college_name)
