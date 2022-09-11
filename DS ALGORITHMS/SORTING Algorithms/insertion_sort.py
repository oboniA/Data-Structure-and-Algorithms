"""
 -Another way of sorting an unsorted list, as a new sorted list
  --in ascending/descending order

 - Every INDEX that is being sorted is a STEP in iteration

 - The first element in the array is assumed to be sorted.
   -- Take the second element and store it separately in key.


Source: https://www.programiz.com/dsa/insertion-sort
        https://www.youtube.com/watch?v=nKzEJWbkPbQ&list=PLO7b4_Ct_NMiFPHgq_WxsOZBhZ9upyQSA&index=46
        https://www.youtube.com/watch?v=lEA31vHiry4&list=PLO7b4_Ct_NMiFPHgq_WxsOZBhZ9upyQSA&index=45

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
