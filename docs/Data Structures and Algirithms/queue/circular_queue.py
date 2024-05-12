# Class to implement circular queue using list. This will have fixed size
class circular_queue:

    # Initializes a circular queue with fixed size
    def __init__(self, size):
        self.queue = [None] * size
        self.size = size
        self.start = -1
        self.tail = -1

    # Method to print the queue
    def __str__(self):

        values = [str(x) for x in self.queue]
        return ("->".join(values))
    
    # Method to check if the queue is full
    def isFull(self):

        if (self.tail + 1 == self.head) or self.start == 0 and (self.tail +1 == self.size):
            return True
        else:
            return False
    
    # Method to check if the queue is empty
    def isEmpty(self):

        if self.start == -1:
            return True
        else:
            return False
        
    # Method to add an element to the queue
    def enqueue(self, value):
        
        if self.isFull():
            
            return None
        else:
            # Checks if the last element is full, moves the tail to the start of the list
            if self.tail + 1 == self.size:
                self.tail = 0
            else:
                self.tail += 1
                # Checks if the queue is empty
                if self.start == -1:
                    self.start = 0
        self.start[self.tail] = value
        return True
    
    # Method to delete an element in queue
    def dequeue(self):

        # Checks if the queue is already empty
        if self.isEmpty():
            return False
        else:
            first_element = self.queue[self.start]
            start = self.start
            # Checks if there is only 1 element in the queue
            if self.start == self.tail:
                self.start = -1
                self.tail = -1
            # Checks if the first element is at the last position in the list
            elif self.start + 1 == self.size:
                self.start = 0
            else:
                self.start += 1
            self.queue[start] = None
        return first_element
    
    # Method to return the first element in the queue
    def peek(self):

        if self.isEmpty():
            return None
        else:
            return self.queue[self.start]
        
    # Method to delete all the elements and reset the queue
    def delete(self):

        self.queue = [None] * self.size
        self.start = -1
        self.tail = -1
    

queue = circular_queue(10)
print(queue)