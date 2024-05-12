# Creates a queue using the queue module in python
import queue as q

customqueue1 = q.Queue(maxsize=4)

customqueue1.put(1)
customqueue1.put(2)
customqueue1.put(3)
print(customqueue1)
# <queue.Queue object at 0x1010fe990>
print(customqueue1.qsize)
# <bound method Queue.qsize of <queue.Queue object at 0x1010fe990>>
print(customqueue1)
# <queue.Queue object at 0x1010fe990>
customqueue1.get()
print(customqueue1)
# <queue.Queue object at 0x1010fe990>
# customqueue1.clear()
print(customqueue1)
# <queue.Queue object at 0x1010fe990>
