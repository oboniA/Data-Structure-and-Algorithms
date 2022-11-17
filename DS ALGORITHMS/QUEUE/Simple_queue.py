"""
    FIFO: First in (left most), First out
    - .appendleft()
    - .pop()

SOURCE: https://www.youtube.com/watch?v=rUUrmGKYwHw
        https://www.programiz.com/dsa/queue
"""

from collections import deque


# create class Queue (1)
class Queue:
    def __init__(self):
        self.queue = deque()  # queue is an instance of deque(); need this for .appendleft()

    def enqueue(self, value):
        self.queue.appendleft(value)  # inserting the value in the left of the queue

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        else:
            return self.queue.pop()

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    # Display  the queue
    def display(self):
        print(self.queue)


# Driver (2)
q = Queue()
q.enqueue(2)
q.enqueue(23)
q.enqueue(45)
q.enqueue(90)
print("The Queue: ")
q.display()

print("\nAfter de-queuing: ")
q.dequeue()
q.display()

