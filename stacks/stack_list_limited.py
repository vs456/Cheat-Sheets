
class Stack:

    # Defines a new list, and a parameter maxsize
    def __init__(self, maxsize):
        
        self.maxsize = maxsize
        self.stack = []

    # Prints the stack
    def __str__(self):
        
        print("/n".join(reversed(self.stack)))

    # Checks if the stack is empty
    def isEmpty(self):

        if self.stack:
            return False
        else:
            return True
        
    # Deletes the most recent element added
    def pop(self):

        if self.isEmpty():
            return None
        else:
            return self.stack.pop()
        
    # Adds a new element to the stack
    def push(self, value):

        if len(self.stack) == self.maxsize - 1:
            return "The stack is full"
        
        self.stack.append(value)

    # Prints the latest element in the stack
    def peek(self):

        return self.stack[-1]
    
    # Checks if the stack is full
    def isFull(self):

        return len(self.stack) == self.maxsize - 1
    
    # Deletes the stack
    def delete(self):

        self.stack = []
