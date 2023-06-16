"""
Traversal techniques in a given Tree
    Binary search tree =
                10
              /   \
            12     9
            /\     /\
           5  6   2  15

    - work out INORDER traversal - left->root->right
    - recursive method
    - VERSION: the tree is applied in the code
"""
class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


'''
Algorithm: inorder(root->left)
           display(root->data)
           inorder(root->right)
'''
def inorder(root):
    if root:                                       # if root exists
        inorder(root.left)                         # visit left
        print(str(root.value) + "->", end='')      # visit root
        inorder(root.right)                        # visit right


''' The Given Tree'''
root = Node(1)
root.left = Node(12)
root.right = Node(9)
root.left.left = Node(5)
root.left.right = Node(6)
root.right.left = Node(2)
root.right.right = Node(15)

print("Inorder traversal: ")
inorder(root)



