"""
    Breath first search
    tree = gcbaedfihjk, where g=root
    Outcome should be:
                g
             /    \
            c      i
          /  \     /\
         b    e   h  j
        /    /\       \
       a    d  f       k
"""

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data



    def insert(self, data):
        if None == self.data:                # if no data in the root node
            self.data = data                 # set current data to the root
        else:
            if data < self.data:             # if current data less than root node
                if self.left is None:        # if left is empty
                    self.left = Node(data)   # set current data to the left node
                else:                        # if left-node already full,
                    self.left.insert(data)   # goes to the next left node

            elif data > self.data:           # if current data greater than root node
                if self.right is None:       # if right is empty
                    self.right = Node(data)  # set current data to the right node
                else:                        # if right-node already full,
                    self.right.insert(data)  # goes to the next left node




root = Node('g')
root.insert('c')
root.insert('b')
root.insert('a')
root.insert('e')
root.insert('d')
root.insert('f')
root.insert('i')
root.insert('h')
root.insert('j')
root.insert('k')

