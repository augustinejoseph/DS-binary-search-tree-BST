# Binary Search Tree (BST)

A binary search tree (BST) is a binary tree data structure in which each node has a key (or value) associated with it. The key in each node is greater than all keys in its left subtree and smaller than all keys in its right subtree.

## Difference between Tree, Binary Tree and Binary Search Tree.
1. ### Tree:

* A hierarchical data structure composed of nodes.
* Consists of a collection of nodes where each node can have zero or more child nodes.
* No specific rules or constraints regarding the organization of the nodes.


2. ### Binary Tree:

* A type of tree structure where each node has at most two children, referred to as the left child and the right child.
* Each node can have zero, one, or two children.
* The order or arrangement of the children is not significant.
* Useful for representing hierarchical relationships and recursive data structures.

3. ### Binary Search Tree:

* A specific type of binary tree that satisfies an additional property or constraint.
* Each node in a binary search tree has a key value associated with it.
* The key value in each node is greater than all keys in its left subtree and smaller than all keys in its right subtree.
* Provides efficient search, insertion, and deletion operations for sorted data.
* Allows for efficient binary search by recursively traversing left or right subtrees based on the comparison of key values.

<hr>
<br/>

## Nodes properties of a BST

The nodes are arranged in a binary search tree according to the following properties:

- The left subtree of a particular node will always contain nodes with keys less than that node’s key.
- The right subtree of a particular node will always contain nodes with keys greater than that node’s key.
- The left and the right subtree of a particular node will also, in turn, be binary search trees.

## **Time Complexity**

- Average cases : *O*(*logn*)
- Worst case : *O*(*n*) , when the tree is unbalanced.
- Space Complexity : O(n)

## **Types of Traversals**

[Medium Article on Traversals](https://augustinejoseph.medium.com/ds-tree-inorder-preorder-and-postorder-traversal-in-python-8d7c271b76b2)
1. Pre-order Traversal
2. In-order Traversal
3. Post-order Traversal

### In-order Traversal
```python
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
<hr>
<br>

### Pre-order Traversal

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
<hr>
<br>

### Post-order Traversal
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

<hr>
<br>

## Insert data to BST
```
1. Compare the value with the current node.
2. If the node is None, create a new node with the value and return it.
3. If the value is equal to the node's data, indicate that the value already exists and return.
4. If the value is less than the node's data, recursively insert it into the left subtree.
5. If the value is greater than the node's data, recursively insert it into the right subtree.
```
```python
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

# Output : 2,3,4,5,6,7,8
```
<hr>
<br>

## Deleting Node from BST
