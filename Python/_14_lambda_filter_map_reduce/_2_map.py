lst = [6,7,23,8,4,3,39,76,10]

# create a function, which takes list as parameter and returns a new list with 
# square of every value from the parameter list

# def get_squared_values(input_list):
#     squared_list = []
#     for num in input_list:
#         squared_list.append(num ** 2)
#     return squared_list
# numbers = [6,7,23,8,4,3,39,76,10]
# squared_numbers = get_squared_values(numbers)
# print("Squared numbers:", squared_numbers)

def get_squared_values(input_list):
    return input_list ** 2

squared_numbers = list(map(get_squared_values,lst))
print("Squared numbers:", squared_numbers)