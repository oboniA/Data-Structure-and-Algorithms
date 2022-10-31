"""
    INSERTION Implementation of an AVL tree

    KEY POINTS:
    1) It is a balanced binary search tree.
    2) The worst case scenario of a binary tree is a linked list; complexity becomes O(N)
    3) AVL trees solve this problem!
    4) We have to maintain the "height" of each node and its children.
    5) The height of any node is the number of layers in the tree;
       - the longest path from the parent node to the leaf node.
       - "height = max(left child's height, right child's height) + 1",
          to compensate the None(None = -1)
    6) The difference(balance factor) in the heights of the left subtree and the right subtree cannot be more than 1.
       - If the difference is more than 1, we rotate the node to the left or the right, to keep the tree balanced.
    7) We have 4 conditions to take care of:
       A) left-left heavy; Left child's height - Right child's height > 1, node rotated to the right
       B) left-right heavy; balance factor of node.left is < -1 or 0
       C) right-right heavy; Left child's height - Right child's height < -1, node rotated to the left
       D) right-left heavy; balance factor of node.right is > 1 or 0

       a) LEFT LEFT         b) LEFT RIGHT           c) RIGHT RIGHT          d) RIGHT LEFT
             1                    1                         1                       1
           2                    2                             2                       2
         3    t2                   3                         t   3                  3

             2                     1                        2                       1
          3     1                3                       1     3                       3
              t2               2                          t                                 2

                                  3                                                  3
                                2    1                                            1     2

Source: https://www.youtube.com/watch?v=GDBhbnkI6aw
        https://www.programiz.com/dsa/avl-tree
        https://www.askpython.com/python/examples/avl-tree-in-python
"""


# Tree TreeNode structure (1)
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1  # initialized the height


class AVLTree:

    # Function to insert a node (2)
    def insert(self, root, value):
        if root is None:                                 # if no root
            return TreeNode(value)                       # recursion call (1); make the current value as the node

        elif value < root.value:                         # if root exists & current value is less than root
            root.left = self.insert(root.left, value)    # insert on the left side of the root

        else:                                            # if root exists & current value is greater than root
            root.right = self.insert(root.right, value)  # insert on the right side of the root

        # Update height values of nodes
        # using step (3) to complete this
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        # update the balance factor and balance the tree
        # using step (4) to complete this
        balanceFactor = self.getBalance(root)            # recursion from (4)
        if balanceFactor > 1:                            # if factor greater than limit 1: LL
            if value < root.left.value:                  # if the current value is less than the "left of the root": LL
                return self.left_rotate(root)            # execute (5)
            else:                                        # if the current value is greater than the "left of the root": LR
                root.left = self.left_rotate(root.left)  # rotate the root_left subtree
                return self.right_rotate(root)           # then execute (5)

        if balanceFactor < -1:                              # if factor less than limit -1: RR
            if value > root.right.value:                    # if the current value is greater than the "right of the root": RR
                return self.left_rotate(root)               # execute (6)
            else:                                           # if the current value is less than the "right of the root": RL
                root.right = self.right_rotate(root.right)  # rotate the root_right subtree
                return self.left_rotate(root)               # then execute (6)

        return root

    # Get the height of the node (3)
    def getHeight(self, root):
        if root is None:
            return 0
        else:
            return root.height

    # Get balance factor of the node (4)
    def getBalance(self, root):
        if root is None:
            return 0
        else:
            # the diff between the height of the left subtree and right subtree
            return self.getHeight(root.left) - self.getHeight(root.right)  # from (3)

    # Function to perform left rotation for RR (5)
    def left_rotate(self, root):
        temp_right_node = root.right  # node2
        t = temp_right_node.left      # refer to (c) at the description

        # update the references
        temp_right_node.left = root   # temporary right node2 swaps with root=node1
        root.right = t                # t added to the right of root=node1 after swapping

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        temp_right_node.height = 1 + max(self.getHeight(temp_right_node.left), self.getHeight(temp_right_node.right))

        return temp_right_node

    # Function to perform right rotation for LL (6)
    def right_rotate(self, root):
        temp_left_node = root.left    # node2
        t2 = temp_left_node.right     # refer to (a) at the description

        # update the references
        temp_left_node.right = root   # temporary right node2 swaps with root node1
        root.left = t2                # t added to the right of node1 after swapping

        root.height = 1 + max(self.getHeight(root.right), self.getHeight(root.left))
        temp_left_node.height = 1 + max(self.getHeight(temp_left_node.right), self.getHeight(temp_left_node.left))

        return temp_left_node

    # create traversal for BST (7)
    def preOrder(self, root):
        if not root:
            return
        print("{0} ".format(root.value), end="")
        self.preOrder(root.left)
        self.preOrder(root.right)


# FINAL Execution (8)
get_tree = AVLTree()
root = None
root = get_tree.insert(root, 40)
root = get_tree.insert(root, 60)
root = get_tree.insert(root, 50)
root = get_tree.insert(root, 70)

print("Pre-Order:")
get_tree.preOrder(root)