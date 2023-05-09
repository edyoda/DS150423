lst1 = [1, 95, 78, 63, 52, 54, 19]
lst2 = [1, 42, 45, 9, 78, 63, 5, 58, 1]

set1 = set(lst1).intersection(set(lst2))
print(set1)
if set1 == set():
    print('No common Values')
else:
    print('Have common values')
