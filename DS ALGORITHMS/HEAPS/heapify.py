"""
    Max Heapify
    Source: https://www.youtube.com/watch?v=CUuuBsNqMpw
"""
# define max_heapify (4)
def max_heapify(arr, n, i):            # n = size of array, i = position
    largest = i                        # initiated largest value (root)
    left = 2*i + 1                     # left of i
    right =  2*i + 2                   # right of i

    # largest so far is compared with the left (5)
    if left < n and arr[left] > arr[i]:
        largest = left                 # left is now the largest

    # largest so far is compared with the right (6)
    if right < n and arr[right] > arr[i]:
        largest = right                # right is now the largest

    # swap the new largest with the previous largest: swap parent with child (7)
    if largest != i:                   # swapping the new with the old
        arr[i], arr[largest] = arr[largest], arr[i]

        # recursive call (8)
        max_heapify(arr, n, largest)


# driver code: executes all the functions (1)
arr = [22, 37, 5, 92, 1, 12]           # the array
n = len(arr)                           # size of the array


# build max heap (2)
for i in range(n//2-1, -1, -1):        # range starts from a, ends at b, c = value decrements by 1
    max_heapify(arr, n, i)             # call the heapify func (won't exist, so need to define(4) it afterwards)


# display (3)
print("Max heap is: ")
for i in range(n):                     # entire array
    print(arr[i])                      #


