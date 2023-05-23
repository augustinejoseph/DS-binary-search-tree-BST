class Node():
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

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
node.left = Node(3)
node.right = Node(7)
node.left.left = Node(2)
node.left.right = Node(4)
node.right.left = Node(6)
node.right.right = Node(8)

print("Inorder Traversal")
inOrderTraverse(node)
print("--------------------")

print("Preorder Traversal")
preOrderTraversal(node)
print("---------------------")

print("Postorder Traversal")
postOrderTraversal(node)

