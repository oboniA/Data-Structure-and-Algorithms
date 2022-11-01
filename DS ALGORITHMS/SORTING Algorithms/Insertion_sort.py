"""
 -Another way of sorting an unsorted list, as a new sorted list
   --in ascending/descending order

 - Every INDEX that is being sorted is a STEP in iteration

 - The first element in the array is assumed to be sorted.
   -- Take the second element and store it separately in key.

 - in a step, it keeps iterating till the "sorted side" is fully sorted

Source: https://www.programiz.com/dsa/insertion-sort
        https://www.youtube.com/watch?v=nKzEJWbkPbQ&list=PLO7b4_Ct_NMiFPHgq_WxsOZBhZ9upyQSA&index=46
        https://www.youtube.com/watch?v=lEA31vHiry4&list=PLO7b4_Ct_NMiFPHgq_WxsOZBhZ9upyQSA&index=45
        https://www.youtube.com/watch?v=8G-PB-RAzdg
"""

# building Insertion sort code (2)
def insert_sort(arr):
    for i_step in range(1, len(arr)):  # from index1 to the length of array;
        i = i_step                     # current index is same as current step; index2 at step2

        # ascending order
        # when index is NOT 0
        while (i > 0) and (arr[i] < arr[i-1]):         # current index less than previous index
                print("\nbefore swapping: ", arr)

                arr[i-1], arr[i] = arr[i], arr[i-1]    # swap
                i -= 1                                 # iteration from right to lef

                print(f"{i_step}'th swap: {arr} \n")


# Driver code (1)
dataset = [7, 5, 1, 3, 9]
print("The dataset: ", dataset)

insert_sort(dataset)
print('Sorted data in Ascending Order:', dataset)  # final (3)
