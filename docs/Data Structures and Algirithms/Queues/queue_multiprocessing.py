# Class to create queue using multiprocessing
from multiprocessing import Queue

customqueue1 = Queue(maxsize=3)

customqueue1.put(1)
print(customqueue1.get())
