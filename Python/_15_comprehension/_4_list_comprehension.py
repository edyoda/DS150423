# 1st Way
# lst = ["Aeroplane","ac","mouse","laptop","apple","desk"]
# lst1 = [i for i in lst if (i[0]=="a" or i[0]=="A") and len(i)>=5]
# print(f"Required list is {lst1}")


# 2nd Way
lst = ['Aeroplane', 'ac', 'mouse', 'laptop', 'apple', 'desk']
newlst = [string for string in lst if string.lower().startswith('a') and len(string) >= 5]
print(newlst)