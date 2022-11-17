"""
    Circular incrementation : i = (i+1)%size

Source: https://www.youtube.com/watch?v=KqTJ5MAUj80
        https://www.youtube.com/watch?v=8sjFA-IX-Ww&t=389s
        https://www.programiz.com/dsa/circular-queue
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
        if self.front == (self.rear + 1) % self.size:  # check if the queue is full
            print("Circular queue is full")
        elif self.front == -1:
            self.front = self.rear = 0  # set front&rear to 0; to the same (first) index
            self.queue[self.rear] = data  # the data of the rear is added to the queue
        else:
            self.rear = (self.rear + 1) % self.size  # when rear>=0, update the rear
            # if the rear reaches the end (remainder 6~0), next it would reset the queue
            self.queue[self.rear] = data  # add the data of current rear to the queue

    # DEQUEUE / DELETION (1.2)
    def dequeue(self):
        if self.front == -1:
            print("Empty Queue!")
        elif self.front == self.rear:  # if NOT empty; and front=rear: ONLY 1 element in the queue
            temp_data = self.queue[self.front]  # store the present data temporary to return it (1.2.1)
            self.front = self.rear = -1  # set them both to -1
            return temp_data   # return removed value that was stored at s1.2.1
        else:                                     # if NOT empty; more than 1 element in the queue
            temp_data = self.queue[self.front]  # store the present data temporary to return it (1.2.2)
            self.front = (self.front + 1) % self.size  # update the front; goes to the next front
            return temp_data    # return removed value that was stored at s1.2.2

    def printCQueue(self):
        if self.front == -1:
            print("No element in the circular queue")
        elif self.rear >= self.front:
            for i in range(self.front, self.rear+1):
                print(self.queue[i], end=" ")
            print()
        else:
            for i in range(self.front, self.size):
                print(self.queue[i], end=" ")
            for i in range(0, self.rear + 1):
                print(self.queue[i], end=" ")
            print()


# Driver code (2)
obj = CircularQueue(5)  # 5=size
obj.enqueue(1)
obj.enqueue(2)
obj.enqueue(3)
obj.enqueue(4)
obj.enqueue(5)
print("Initial queue")
obj.printCQueue()

obj.dequeue()
print("After removing an element from the queue")
obj.printCQueue()
