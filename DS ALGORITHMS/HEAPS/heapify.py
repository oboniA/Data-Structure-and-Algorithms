"""
    Max Heapify
    Source: https://www.youtube.com/watch?v=CUuuBsNqMpw
            https://www.programiz.com/dsa/heap-data-structure
            https://www.youtube.com/watch?v=lCLcQe1Wgkg
"""


# build max_heapify (1)
def max_heapify(arr, i):  # i = position of root of a tree/subtree
    largest = i  # initiated the largest value (root)
    left = 2 * i  # left of i
    right = 2 * i + 1  # right of i

    # largest so far is compared with the left
    if left < len(arr) and arr[left] > arr[i]:
        largest = left  # set left as the root

    # largest so far is compared with the right
    if right < len(arr) and arr[right] > arr[i]:
        largest = right  # set right as the root

    # swap the new largest with i; swap parent with child
    if largest != i:  # if i not the largest
        arr[i], arr[largest] = arr[largest], arr[i]  # swap i with the largest

        max_heapify(arr, largest)  # recursive call (from 2)


# insertion (2)
def insert(arr, data):
    n = len(arr)
    if n == 0:  # if array empty
        arr.append(data)  # insert the number to the array
    else:  # if not empty
        arr.append(data)  # add the num to array list
        # a = (n // 2 - 1) = first index of non-leaf root
        # b = -1 = down to zero
        # c = -1 = decrement by 1
        for item in range((n // 2 - 1), -1, -1):  # recursive call (from 1)
            max_heapify(arr, item)


# deletion (3)
def deletion(arr, d_data):
    n = len(arr)
    item = 0
    for item in range(n):
        if d_data == arr[item]:  # if data is present at current index
            break  # stop looping further

    # swap data to be deleted with the very last item
    arr[item], arr[n - 1] = arr[n - 1], arr[item]
    # now delete the very last element/leaf
    arr.remove(d_data)

    for item in range((n // 2 - 1), -1, -1):  # recursive call (from 1)
        max_heapify(arr, item)


# driver code: executes all the functions (4)
a = []  # the array

insert(a, 22)
insert(a, 37)
insert(a, 52)
insert(a, 92)
insert(a, 1)
insert(a, 12)
print("Max heap is: " + str(a))

deletion(a, 92)
print("After deleting an element: " + str(a))
