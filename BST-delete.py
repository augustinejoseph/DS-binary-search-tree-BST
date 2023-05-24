class Node():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def findSuccessor(node):
    if node is not None:
        

def insert(node, value):
    if node is None:
        return Node(value)
    if value < node.data:
        node.left = insert(node.left, value)
    elif value > node.data:
        node.right = insert(node.right, value)
    return node

def printNode(node):
    if node is not None:
        printNode(node.left)
        print(node.data)
        printNode(node.right)

def delete(node, value):
    if node is None:
        return node
    if value < node.data:
        delete(node.left. value)
    elif value > node.data:
        delete(node.right, value)
    else:
        if node.left is None and node.right is None:
            node = None
        elif node.left is None:
            node = node.right
        elif node.right is None:
            node = node.left
        else:


node = Node(5)
insert(node, 3)
insert(node, 7)
insert(node, 2)

printNode(node)
