class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(node, value):
    if node is None:
        return Node(value)
    if value == node.data:
        print("value alredy exists")
        return
    elif value < node.data:
        node.left = insert(node.left, value)
    else:
        if value > node.data:
            node.right = insert(node.right, value)
    return node
    
def printNode(node):
    if node is not None:
        printNode(node.left)
        print(node.data)
        printNode(node.right)

node = Node(5)
insert(node, 3)
insert(node, 7)
insert(node, 2)
insert(node, 4)
insert(node, 6)
insert(node, 8)

printNode(node)