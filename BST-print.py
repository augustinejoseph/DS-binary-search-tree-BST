class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



def printBst(tree):
    if tree is not None:
        printBst(tree.left)
        print(tree.data)
        printBst(tree.right)

# Creating the BST
tree = Node(5)
tree.left = Node(3)
tree.right = Node(7)
tree.left.left = Node(2)
tree.left.right = Node(4)
tree.right.left = Node(6)
tree.right.right = Node(8)

# Printing the BST
print("Binary Search Tree:")
printBst(tree)