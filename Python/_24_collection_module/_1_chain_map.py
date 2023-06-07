# ChainMap

# used to combine multiple dictionaries together

from collections import ChainMap

dict1 = {'a':'A','b':'B','c':'C'}
dict2 = {'1':'One','2':'Two'}
dict3 = {'rno':'1','name':'Bharati'}

chain_map = ChainMap(dict1,dict2,dict3)
print(chain_map)
print(chain_map['rno'])

dict4 = {"xyz":"xyz"}

chain_map1 = chain_map.new_child(dict4)
print(chain_map1)

