from collections import deque

# Queue using the deque class from collection module
customqueue1 = deque(maxlen= 4)
customqueue1.append(1)
customqueue1.append(2)
customqueue1.append(3)
print(customqueue1)
# deque([1, 2, 3], maxlen=4)
customqueue1.append(4)
customqueue1.append(5)
print(customqueue1)
# deque([2, 3, 4, 5], maxlen=4)
customqueue1.popleft()
print(customqueue1)
# deque([3, 4, 5], maxlen=4)
customqueue1.clear()
print(customqueue1)
# deque([], maxlen=4)
