# Queue implementation using python list of an unlimited size
class Queue:

    def __init__(self):
        self.queue = []

    def __str__(self):
        
        values = [str(x) for x in self.queue]
        print("->".join(values))

    def push(self, value):

        self.queue.append(value)
        return True