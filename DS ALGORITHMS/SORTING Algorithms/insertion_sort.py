"""
 -Another way of sorting an unsorted list, as a new sorted list
  --in ascending/descending order

 - Every INDEX that is being sorted is a STEP in iteration

 - The first element in the array is assumed to be sorted.
   -- Take the second element and store it separately in key.

 - Compare key with the first element.
   -- If the first element is greater than key, then key is placed in front of the first element.

 - the first two elements are sorted.
   -- Take the third element and compare it with the elements on the left of it.
   --Place it just behind the element smaller than it.
     -- If there is no element smaller than it, then place it at the beginning of the array.

 - Similarly, place every unsorted element at its correct position.

Source: https://www.programiz.com/dsa/insertion-sort

"""


def insert_sort(array1):

    for i_step in range(1, len(array1)):       # for (initial) unsorted list
        key = array1[i_step]                   # the current item of the current step
        j = i_step - 1                         # the immediate previous item

        # ascending order
        while (j >= 0):
            if (key < array1[j]):              # when present item is smaller than the item to the immediate LHS (as long as the index of j is 0 or more)
               array1[j+1] = array1[j]         # shift the value in arr[j] to the right
               array1[j] = key                 # place the key at the recently empty spot
               j -= 1                          # goes down the list incrementally

            else:
                break



items = [7, 5, 1, 3, 9, 10, 2]
insert_sort(items)
print('Sorted Array in Ascending Order:', items)