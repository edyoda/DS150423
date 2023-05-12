no_of_entries = int(input('Enter no. of items you want in your dict:   '))
lst = []
for i in range(no_of_entries):
    key_in = input('Enter your key:   ')
    value_in = input('Enter your value:   ')
    tup1 = (key_in, value_in)
    lst.append(tup1)
dictionary = dict(lst)
# print(dictionary)

def quiz_function(variable_as_dict):
    list_of_key = list(variable_as_dict.keys())
    list_of_value = list(variable_as_dict.values())
    for i in range(len(list_of_key)):
        for j in range(i+1, len(list_of_key)):
            if list_of_key[i]>list_of_key[j]:
                list_of_key[i], list_of_key[j] = list_of_key[j], list_of_key[i]
                list_of_value[i], list_of_value[j] = list_of_value[j], list_of_value[i]
    
    return dict(zip(list_of_key, list_of_value))

print(quiz_function(dictionary))