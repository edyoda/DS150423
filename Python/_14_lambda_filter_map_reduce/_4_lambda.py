# Lambda Function

# it is an anonymous function
# it is a function without a name
# it can have any number of arguments but can have only one expression (condition)
# it helps to create one liner function
# it doesnot have return statment 
# can be defined as parameter in a function

# Function

# function with name
# it can have return statement, if you don't mention return statement it will return None
# cannot be defined as parameter in a function


def fun(a,b):
    return a+b

# syntax : 
# lambda <parameter1,parameter2> : <condition/expression>

data = lambda a,b : a + b
print(data(5,6))

