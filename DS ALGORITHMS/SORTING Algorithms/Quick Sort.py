"""
   - divide and conquer algorithm (similar to merge)
   - Choose pivot element
     -- store <pivot in Left sub Array
     -- store >pivot in Right sub Array
     -- keep storing recursively in left and right sub-array
   - call quick sort recursively in left and right sub arrays
Hence, it's a recursive algorithm based on the choice of the pivot element
       pivot is GENERALLY the rightmost element in the array

Source: https://www.youtube.com/watch?v=8G-PB-RAzdg
        https://www.youtube.com/watch?v=kFeXwkgnQ9U&t=215s
"""

# Build quick srt code
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr.pop()    # removes the last element; also returns it

    left = []
    right = []
    for item in arr:
        if item > pivot:           # if the current item greater than pivot
            left.append(item)      # add it to the left sub-array
        else:                      # if the current item less than pivot
            right.append(item)     # add it to the right sub-array

    # recursion call to run the logic in the left and right subtrees
    return quicksort(left) + [pivot] + quicksort(right)



# driver code (1)
dataset = [3, 10, 5, 1, 12, 9]
print("original data", dataset)

print("sorted data:")         # final step (3)
print(quicksort(dataset))



