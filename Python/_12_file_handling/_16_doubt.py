import os
file2 = open("correct_paths.txt", "a+")
with open("path.txt") as file:
    lst = file.readlines()
    for i in lst:
        i = i.replace('\n', '')
        i = i.replace('\\\\','\\')
        print(i)
        is_true = os.path.exists(i)
        if is_true:
            file2.write(f'{i}\n')

file2.seek(0)
validpath = file2.read()
print(f'Valid paths from these are:   {validpath}')
file2.close()