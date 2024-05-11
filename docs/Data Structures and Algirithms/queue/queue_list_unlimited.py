# Queue implementation using python list of an unlimited size
class Queue:

    def __init__(self):
        self.queue = []

    def __str__(self):
        
        values = [str(x) for x in self.queue]
        return ("->".join(values))

    def isEmpty(self):

        if self.queue:
            return False
        else:
            return True

    def enqueue(self, value):

        self.queue.append(value)
        return True
    
    def dequeue(self):

        if self.isEmpty():
            return None
        value = self.queue[0]
        self.queue.pop(0)
        return value
    
    def peek(self):

        if self.isEmpty():
            return None
        return self.queue[0]
        
    def delete(self):

        self.queue = []
    
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
print(queue)
queue.dequeue()
print(queue)