
class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def __iter__(self):
        currnode = self.head

        while currnode:
            
            yield currnode
            currnode = currnode.next

class Stack:

    def __init__(self):
        self.stack = LinkedList()

    def __str__(self):
        values = [str(x.value) for x in self.stack]
        return "\n".join(values)

    def isEmpty(self):

        if self.stack.head:
            return False
        else:
            return True
        
    def push(self, value):

        new_node = Node(value)
        new_node.next = self.stack.head
        self.stack.head = new_node

    def pop(self):

        if self.isEmpty():
            return False
        pop_node = self.stack.head.value
        self.stack.head = self.stack.head.next

        return pop_node
    
    def peek(self):

        if self.isEmpty():

            return None
        return self.stack.head.value
    
    def delete(self):

        self.stack.head = None

        return self.stack


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(3)
stack.push(4)
# print(stack)
stack.delete()
print(stack)