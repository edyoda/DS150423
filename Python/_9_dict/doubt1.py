def get_user_info():
    name = input("Enter a name: ")
    age = input("Enter an age: ")
    return {'name': name, 'age': age}

def group_by_names(users):
    result = {}
    for user in users:
        name = user.get('name')
        if name:
            if name not in result:
                result[name] = [user]
            else:
                result[name].append(user)
    return result  

# Example usage:
users = []
for i in range(3):
    users.append(get_user_info())
print(group_by_names(users))

