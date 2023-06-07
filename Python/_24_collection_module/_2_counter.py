# Counter

# it's a child class of dict class
# it will consider elements as key
# and count of elements as value 

# ["a","a","b","a","c","b"]
# {"a":3,"b":2,"c":1}

from collections import Counter

lst = ["a","a","b","a","c","b"]

counter = Counter(lst)
print(counter)

counter1 = Counter(a=4,b=9,c=8)
print(counter1)