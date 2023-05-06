value = "Python is a programming language brogramming"
lst = value.split(" ")
print(lst)

max_len = 0
for i in lst: # i = language - 8
    if len(i) > max_len:
        max_len = len(i) # 6       | 12
        result = i       # Python  | programming
    
print(result)


# str input 
# count of all the vowels