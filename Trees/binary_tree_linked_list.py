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
    
def levelOrderTraversal(root):

    if not root:
        return

    print(root.value)
    levelOrderTraversal(root.leftchild)
    levelOrderTraversal(root.rightchild)
    

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
levelOrderTraversal(newBT)


