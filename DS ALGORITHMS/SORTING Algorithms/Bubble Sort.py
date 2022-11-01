"""
    BUBBLE SORT
    2 iterations:
                 - to set the largest elements
                 - recheck again to set the next largest element

    Source: https://www.youtube.com/watch?v=8G-PB-RAzdg
"""


# building Bubble sort code (2)
def bubbleSort(arr):
    n = len(arr)       # length of the array; is 5

    # outer loop
    # 5 times
    for i in range(n):      # runs from 0 to 5;
        # inner loop
        for j in range(0, n-i-1):   # till nth last element
            print("j=", j)
            print("j+1=", j+1)
            print("before swapping:", arr)     # unsorted array

            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                print("After swapping", arr)      # sorted array
                print(" ")



# Create Driver Code (1)
dataset = [9, 4, 6, 8, 5]
print("Original data: ", dataset)

bubbleSort(dataset)              # will be declared next
print("sorted data: ", dataset)  # final execution (3)
