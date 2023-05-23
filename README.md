```python
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

node = Node(5)
node.left = Node(3)
node.right = Node(7)
node.left.left = Node(2)
node.left.right = Node(4)
node.right.left = Node(6)
node.right.right = Node(8)

# output : 
Inorder Traversal
2
3
4
5
6
7
8
--------------------
```

```python
class Node():
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def preOrderTraversal(node):
    if node is not None:
        print(node.data)
        preOrderTraversal(node.left)
        preOrderTraversal(node.right) 

node = Node(5)
node.left = Node(3)
node.right = Node(7)
node.left.left = Node(2)
node.left.right = Node(4)
node.right.left = Node(6)
node.right.right = Node(8)

# output : 
Preorder Traversal
5
3
2
4
7
6
8
---------------------
```

```python
class Node():
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

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

# output : 
Postorder Traversal
2
4
3
6
8
7
5
```