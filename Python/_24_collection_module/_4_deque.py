# deque

# it is open from both end
# you can add/delete the elements from both the ends

from collections import deque

deque_obj = deque([1,2,3,4,5])
print(deque_obj)

deque_obj.append(100)
print(deque_obj)

deque_obj.appendleft(200)
print(deque_obj)

deque_obj.pop()
print(deque_obj)

deque_obj.popleft()
print(deque_obj)

deque_obj.extend([500,600,700])
print(deque_obj)

deque_obj.extendleft([500,600,700])
print(deque_obj)

