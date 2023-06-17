"""
    Generate Binary Numbers from 1 to n using the queue:

     """"IMPORT Queue from queue""""

    ** use .put() to enqueue
    ** use .get() to dequeue
    - Create an empty queue of strings
    - Enqueue the first binary number “1” to the queue.
    - Now run a loop for generating and printing n binary numbers.
      -- Dequeue and Print the front of queue.
      -- Append “0” at the end of front item and enqueue it.
      -- Append “1” at the end of front item and enqueue it.

Sources: https://practice.geeksforgeeks.org/problems/generate-binary-numbers-1587115620/1?page=1&category[]=Queue&sortBy=submissions
         https://www.geeksforgeeks.org/interesting-method-generate-binary-numbers-1-n/

"""


def generateBin(n):
    # create empty queue of strings
    from queue import Queue
    q = Queue()

    # enqueue the first bin no.
    q.put("1")

    temp = []
    while n > 0:
        n = n - 1

        # print front/head of queue
        h1 = q.get()
        temp.append(h1)

        # store h1 in new variable before updating
        h2 = h1

        """   h1 = h2 
              +     +
             0       1
        Note that h2 contains the previous front(h1)
        """
        # Append “0” at the end of h1 and enqueue it
        q.put(h1 + "0")
        # Append “1” at the end of h2 and enqueue it
        q.put(h2 + "1")

    return temp


# Driver code
if __name__ == "__main__":
    num = 10
    # Function call
    generateBin(num)
