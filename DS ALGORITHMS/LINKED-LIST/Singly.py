"""
Singly Linked List
 - Traversal of a linked list (3.1)
   -- no data in the list so returns empty list
 - Add/Insert operation (3.2)
   -- at the beginning O(1)
   -- at the end O(n)
   -- between nodes O(n)
"""


# Create Node class (2)
class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


# creating a linked list (3)
class Linkedlist:
    def __init__(self):
        self.head = None

    # writing the traversal method for a linked list (3.1)
    def print_linked_list(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref  # next head is the next ref_node


# Driver code (1)
list1 = Linkedlist()
list1.print_linked_list()
