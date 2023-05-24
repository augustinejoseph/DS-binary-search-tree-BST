class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def findSuccessor(node):
    if node is not None:
        while node.left is not None:
            node = node.left
        return node

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
        node.left = delete(node.left, value)
    elif value > node.data:
        node.right = delete(node.right, value)
    else:
        # if node is a leaf node
        if node.left is None and node.right is None:
            node = None 
        # if root has one left child
        elif node.left is None:
            node = node.right
        # if node has one right child
        elif node.right is None:
            node = node.left
        # if node has both left and right child
        else:
            successor = findSuccessor(node.right)
            node.data = successor.data
            node.right = delete(node.right, successor.data)
    return node

node = Node(5)
insert(node, 3)
insert(node, 7)
insert(node, 2)
insert(node, 4)
insert(node, 6)
insert(node, 8)

print("Before Deletion")
printNode(node)

delete(node, 6)

print("After Delete")
printNode(node)