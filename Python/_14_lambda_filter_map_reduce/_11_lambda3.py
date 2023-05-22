nums = [12,15,17,39,30,33,25]
print("Orginal list:")
print(nums) 

result = list(filter(lambda x: (x % 3== 0 and x % 5 == 0), nums)) 
print("\nNumbers of the above list divisible by three and five:")
print(result)