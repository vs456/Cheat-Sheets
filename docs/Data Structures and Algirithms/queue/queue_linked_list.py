# Class to create the queue node
class Node:

    # Creates the node with value, and the next pointer
    def __init__(self, value):
        self.value = value
        self.next = None

    # Prints the node value
    def __str__(self) -> str:
        return str(self.value)

class LinkedList:

    # Creates a linked list with head and tail
    def __init__(self):
        self.head = None
        self.tail = None

    # Iterator which gives the next value in the linked list
    def __iter__(self):

        currNode = self.head
        while currNode:
            yield currNode
            currNode = currNode.next

# The queue class
class Queue:

    # Creates an object of the linked list class
    def __init__(self):

        self.linkedlist = LinkedList()

    # Prints the queue
    def __str__(self):
        
        values = [x for x in self.linkedlist]
        return ("->".join(values))
    
    # Adds a new element to the queue
    def enqueue(self, value):

        new_node = Node(value)
        # Checks if the queue is empty
        if self.linkedlist.head is None:
            self.linkedlist.head = new_node
            
        else:
            self.linkedlist.tail.next = new_node
        # Updates the tail of the queue to the newly added element
        self.linkedlist.tail = new_node

        return True
            
    # Checks if the queue is empty
    def isEmpty(self):

        if self.head is None:
            return True
        else:
            return False
    
    # Removes the first element from the queue
    def dequeue(self):

        if self.isEmpty():
            return False
        dequeu_node = self.linkedlist.head
        if self.linkedlist.head == self.linkedlist.tail:
            self.linkedlist.head = None
            self.linkedlist.tail = None
        else:
            self.linkedlist.head = dequeu_node.next
        return dequeu_node
    
    # Returns the firts element added
    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.linkedlist.head
         
        
