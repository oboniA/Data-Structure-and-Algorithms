"""
Circular incrementation : i = (i+1)%size

"""


# STEP (1)
class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1  # track the first element of the queue
        self.rear = -1  # track the last elements of the queue

    # ENQUEUE / INSERT (1.1)
    def enqueue(self, data):
        # insert element to the queue
        if self.front == (self.rear + 1) % self.size:  # check if the queue is full
            print("Circular queue is full")
        elif self.front == -1:
            self.front = self.rear = 0  # set front&rear to 0; to the same (first) index
            self.queue[self.rear] = data  # the data of the rear is added to the queue
        else:
            self.rear = (self.rear + 1) % self.size  # when rear>=0, update the rear
            # if the rear reaches the end (remainder 6~0), next it would reset the queue
            self.queue[self.rear] = data  # add the data of current rear to the queue
