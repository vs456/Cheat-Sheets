# Import the queue class from the Linked List implementation of Queues
from linked_list_queue import Queue

class Node():

    def __init__(self, value):
        
        self.value = value
        self.leftchild = None
        self.rightchild = None

def preorderTraversal(root):

    if not root:
        return
    
    print(root.value)
    preorderTraversal(root.leftchild)
    preorderTraversal(root.rightchild)

def InOrderTraversal(root):

    if not root:
        return
    InOrderTraversal(root.leftchild)
    print(root.value)
    InOrderTraversal(root.rightchild)

def postOrderTraversal(root):

    if not root:
        return
    postOrderTraversal(root.leftchild)
    postOrderTraversal(root.rightchild)
    print(root.value)
    
# Requires queue implementation before running.
def levelOrderTraversal(root):

    if not root:
        return

    customqueue = Queue()
    customqueue.enqueue(root)

    while not customqueue.isEmpty():
        root = customqueue.dequeue()
        print(root.value.value)
        if root.value.leftchild:
            customqueue.enqueue(root.value.leftchild)
        if root.value.rightchild:
            customqueue.enqueue(root.value.rightchild)

# Function to search an element in the binary tree
def search(root, value):

    if not root:
        return None
    else:
        customqueue = Queue()
        customqueue.enqueue(root)

        while not customqueue.isEmpty():
            root = customqueue.dequeue()
            if root.value.value == value:
                return True
            else:
                if root.value.leftchild:
                    customqueue.enqueue(root.value.leftchild)
                if root.value.rightchild:
                    customqueue.enqueue(root.value.rightchild)
        return False


def insert(root, value):

    newnode = Node(value)
    if not root:
        root = newnode
        return True
    customqueue = Queue()
    customqueue.enqueue(root)

    while not customqueue.isEmpty():
        root = customqueue.dequeue()
        if root.value.value == value:
            return True
        else:
            if root.value.leftchild:
                customqueue.enqueue(root.value.leftchild)
            else:
                root.value.leftchild = newnode
            if root.value.rightchild:
                customqueue.enqueue(root.value.rightchild)
            else:
                root.value.rightchild = newnode
 
    

newBT = Node("Drinks")
hot = Node("hot")
cold = Node("cold")
newBT.leftchild = hot
newBT.rightchild = cold
tea = Node("tea")
coffee = Node("coffee")
hot.leftchild = tea
hot.rightchild = coffee
cola = Node("cola")
fanta = Node("fanta")
cold.leftchild = cola
cold.rightchild = fanta

# preorderTraversal(newBT)
# InOrderTraversal(newBT)
# postOrderTraversal(newBT)
# levelOrderTraversal(newBT)
print(search(newBT, "tea"))


