"""
    Max Heapify
    Source: https://www.youtube.com/watch?v=CUuuBsNqMpw
            https://www.programiz.com/dsa/heap-data-structure
"""
# driver code: executes all the functions (1)
arr = []                               # the array
n = len(arr)                           # size of the array


# define max_heapify (3)
def max_heapify(arr, n, i):            # n = size of array, i = position
    largest = i                        # initiated the largest value (root)
    left = 2 * i + 1                   # left of i
    right = 2 * i + 2                  # right of i

    # largest so far is compared with the left
    if left < n and arr[left] > arr[i]:
        largest = left                 # left is now the largest

    # largest so far is compared with the right
    if right < n and arr[right] > arr[i]:
        largest = right                # right is now the largest

    # swap the new largest with the previous largest: swap parent with child
    if largest != i:                   # swapping the new with the old
        arr[i], arr[largest] = arr[largest], arr[i]
        # recursive call (from 2)
        max_heapify(arr, n, largest)


# insertion (4)
def insert(arr, num):                  # array and size created again
    n = len(arr)
    if n == 0:                         # if array empty
        arr.append(num)                # add insert the number to the array list
    else:                              # if not empty
        arr.append(num)                # add the num to array list
        # recursive call (from 2)      # and do the heapify so the number is placed to the correct position
        for i in range((n // 2 - 1), -1, -1):
            max_heapify(arr, n, i)


# build max heap (2) : this will be called at every Method
for i in range(n//2-1, -1, -1):        # range starts from a, ends at b, c = value decrements by 1
    max_heapify(arr, n, i)             # heapify func that will be called (won't exist, so need to define(4) it afterwards)


# the arrays are ready to be inserted (5)
insert(arr, 22)
insert(arr, 37)
insert(arr, 52)
insert(arr, 92)
insert(arr, 1)
insert(arr, 12)


# displays (6)
print("Max heap is: " + str(arr))
