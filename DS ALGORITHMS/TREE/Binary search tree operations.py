"""
    Binary search tree operations

    - create insert
    - tree traverse
    - build the tree
    - print the tree (sorted) (ascending: root is the smallest)
    Source: https://www.programiz.com/dsa/binary-search-tree
            https://www.youtube.com/watch?v=lFq5mYUWEBk&t=665s
"""


# creating class (2)
class BSTNode:
    # just for a node, without any left or right
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # method for inserting values to the tree (3)
    def insert(node, value):
        if value == node.value:  # if the value already exists
            return  # returns, prevents duplicates

        if value < node.value:  # if the value is less than it's parent node
            # add data to left subtree
            if node.left:  # if left node contains value (not leaf-node)
                node.left.insert(value)  # recursion of (3): starts creating sub-tree
            else:  # if left node is empty (is a leaf-node)
                node.left = BSTNode(value)  # recursion of (2)
        else:
            # add to right subtree
            if node.right:  # if right node contains value (not leaf-node)
                node.right.insert(value)  # recursion of (3)
            else:  # if right node is empty (is a leaf-node)
                node.right = BSTNode(value)  # recursion of (2)

    # method for traversal (4)
    # will return a list of tree elements in specific order
    def inOrder(node):
        tree_elements = []  # elements initiated in empty list

        # visit left tree
        if node.left:
            tree_elements += node.left.inOrder()  # recursion of (4) added to the element list

        # visit base node
        tree_elements.append(node.value)

        # visit right tree
        if node.right:
            tree_elements += node.right.inOrder()  # recursion of (4) added to the element list

        return tree_elements

    # method for searching a particular value in the tree/ existence check (6)
    def search(node, s_val):  # s_val = value to be searched from the tree
        if node.value == s_val:  # if s_val is the node
            return True

        if s_val < node.value:  # if less that node
            # might be in left sub-tree
            if node.left:  # if node has children
                return node.left.search(s_val)  # recursion (6); searches value
            else:  # if no sub-tree
                return False

        if s_val > node.value:  # if greater than node
            # might be in right sub-tree
            if node.right:  # if node has children
                return node.right.search(s_val)  # recursion (6); searches value
            else:  # if leaf-node
                return False


# building the tree (5)
def build_tree(tree_elements):
    root = BSTNode(tree_elements[0])  # assigned first element as the root node

    for i in range(1, len(tree_elements)):
        root.insert(tree_elements[i])

    return root


# The numbers in the tree (1)
if __name__ == '__main__':
    numbers = [65, 7, 32, 4, 12, 9, 7, 44]
    tree_numbers = build_tree(numbers)  # calling (5)

    print(tree_numbers.inOrder())  # prints in-order traversal in ascending order; sorts; prints set

    print(tree_numbers.search(9))  # calling (6); searching/checking if a value exists
