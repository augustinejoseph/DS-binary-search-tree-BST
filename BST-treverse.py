class Node():
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def insert(node, value):
    if node is None:
        return Node(value)
    if value < node.data:
        node.left = insert(node.left, value)
    else:
        if value > node.data:
            node.right = insert(node.right, value)
    return node

def inOrderTraverse(node):
    if node is not None:
        inOrderTraverse(node.left)
        print(node.data)
        inOrderTraverse(node.right)

def preOrderTraversal(node):
    if node is not None:
        print(node.data)
        preOrderTraversal(node.left)
        preOrderTraversal(node.right) 
        
def postOrderTraversal(node):
    if node is not None:
        postOrderTraversal(node.left)
        postOrderTraversal(node.right)
        print(node.data)

node = Node(5)
insert(node, 3)
insert(node, 7)
insert(node, 2)
insert(node, 4)
insert(node, 6)
insert(node, 8)


print("Inorder Traversal")
inOrderTraverse(node)
print("--------------------")

print("Preorder Traversal")
preOrderTraversal(node)
print("---------------------")

print("Postorder Traversal")
postOrderTraversal(node)

