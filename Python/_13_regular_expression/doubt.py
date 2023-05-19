# import re

# string_input = input('Enter your String Here: ')
# result = re.findall('^ab*', string_input)
# print(result)

# if result:
#     print('This is Valid One ')
# else:
#     print('This is Invalid One')


import re
def match_num(string):
    value = int(input("Enter : "))
    text = re.compile(f"^{value}")
    if text.match(string):
        return True
    else:
        return False
print(match_num('5-2345861'))
print(match_num('6-2345861'))
print(match_num('5Edyoda'))