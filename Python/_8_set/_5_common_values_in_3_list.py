lst1 = [1, 5, 8, 6, 45, 255, 789, 25]
lst2 = [65, 85, 74, 1, 5, 6, 8, 1147, 658]
lst3 = [1, 5, 8, 6, 98, 74, 25, 369, 45, 57]

set1 = set(lst1).intersection(set(lst2))
set1.intersection_update(set(lst3))

print(set1)