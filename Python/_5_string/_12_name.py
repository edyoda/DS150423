# name = input('Enter name   ').split()
# initials = ''
# for i in name:
#     if i in name[0:-1] :
#         initials += i[0] + '.'

# print('\n', initials, name[-1])


name = input("enter the name:")
name_divisions = name.split()
initials = ""
for divisions in name_divisions [:-1]:
    initials += divisions[0].upper() + ". "
surname = name_divisions[-1].capitalize()
print(initials + surname)