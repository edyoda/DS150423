# Generators

# generators are function
# it is memory efficient
# does not allocate memory to all the objects at the sametime
# it yields the data and returns the elements of data when it is demanded

# normal function
# def fun(n):
#     return n * 2

# print(fun(10))

# generator function
# def fun(n):
#     yield n * 2

# data = fun(10)
# print(next(data))


gen = (2*i for i in range(1,11)) # 2,4,6,8,10,12,14,16,18,20
print(gen)

print(next(gen)) # 4,6,8,10,12,14,16,18,20
print(next(gen)) # 6,8,10,12,14,16,18,20
print(next(gen))

