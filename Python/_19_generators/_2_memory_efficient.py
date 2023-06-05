import memory_profiler as memory

# def fun(n):
#     lst = []
#     for i in range(n):
#         lst.append(i)
#     return lst

# print("Before calling : ",memory.memory_usage(),"MB")
# fun(10000000)
# print("After calling : ",memory.memory_usage(),"MB")

def gen(n):
    for i in range(n):
        yield i

print("Before calling : ",memory.memory_usage(),"MB")
gen(10000000)
print("After calling : ",memory.memory_usage(),"MB")