"""
    FIFO: First in (left most), First out
    - .appendleft()
    - .pop()

SOURCE: https://www.youtube.com/watch?v=rUUrmGKYwHw
        https://www.programiz.com/dsa/queue
"""

# use deque instead of list
# insertion and deletion from the beginning of a list is slow (easy from the end)
# because al the elements have to be shifted by 1
# deque - double ended items
from collections import deque


# create class Queue (1)
class Queue:
    def __init__(self):
        self.items = deque()  # setting to an empty deque

    def is_empty(self):
        # return len(self.items) == 0
        return not self.items  # when deque not empty

    def enqueue(self, item):
        self.items.append(item)  # inserting the value in the left of the items

    def dequeue(self):
        if len(self.items) < 1:
            return None
        else:
            return self.items.popleft()  # remove the first-in

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[0]  # front peek

    # Display  the items
    def __str__(self):
        return str(self.items)


if __name__ == "__main__":
    q = Queue()

    q.enqueue(3)
    q.enqueue(5)
    q.enqueue(2)
    q.enqueue(7)
    print(q)

    q.peek()
    print(q)

    q.dequeue()
    print(q)

    q.enqueue(9)
    print(q)

