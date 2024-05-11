# stack class with python list of unlimited size
class Stack:
    # Initializes an empty stack
    def __init__(self):
        self.stack = []

    # Prints the stack
    def __str__(self):
        values = [str(x) for x in reversed(self.stack)]
        return("\n".join(values))
    
    # Checks the stack is empty or not
    def isEmpty(self):
        if not self.stack:
            return True
        else:
            return False
        
    # Add a new element to the stack
    def push(self, value):
        
        self.stack.append(value)
        return True
    
    # Deletes the most recent element in stack
    def pop(self):

        if self.isEmpty():
            return False
        else:
            return self.stack.pop()
        
    # Returns the most recently added to stack
    def peek(self):

        if self.isEmpty():
            return None
        else:
            return self.stack[-1]
    
    # Deletes the entire stack
    def delete(self):

        self.stack = []
