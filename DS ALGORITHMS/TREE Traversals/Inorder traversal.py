"""
    Binary search tree =
               10
              /  \
            12    9
            /\    / \
           5  6  2  15

    - work out INORDER traversal
    - recursive method
    - VERSION: the tree is applied in the code
"""
class Node:
    def __init__(self, n):
        self.left = None
        self.right = None
        self.node_val = n


def inorder(root):
    if root:
        inorder(root.left)                         # Traverse left
        print(str(root.node_val) + "->", end='')   # Traverse root
        inorder(root.right)                        # Traverse right


root = Node(1)
root.left = Node(12)
root.right = Node(9)
root.left.left = Node(5)
root.left.right = Node(6)
root.right.left = Node(2)
root.right.right = Node(15)

print("Inorder traversal: ")
inorder(root)



