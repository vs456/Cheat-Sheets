class Tree:
    def __init__(self, data, children = []):
        self.data = data
        self.children = children

    def __str__(self, level = 0):
        ret = " " * level + str(self.data) + "\n"
        for child in self.children:
            ret = child.__str__(level + 1)
        return ret
    
    def addChild(self, Tree):
        self.children.append(Tree)

tree = Tree("Drinks", [])
hot = Tree("Hot", [])
cold = Tree("Cold", [])
tree.addChild(hot)
tree.addChild(cold)
