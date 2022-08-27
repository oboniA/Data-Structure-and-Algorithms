"""
 -Another way of sorting an unsorted list
  --in ascending order

 - by dividing the unsorted list
   -- into 2 sublist
   -- a sorted and an unsorted sublist
   -- sorted sublist is initially length of 1
   -- rest of the items will go to unsorted list
 - when algorithm starts:
   -- the leftmost item in unsorted list moves in the sorted list,
   -- now in sorted list, the values are compared and swapped accordingly
 - the comparison is between the last item of sorted list and first item of unsorted list
   -- that is after the first item of unsorted list is sent to the sorted list,
   -- meaning last 2 items of the sorted lists are compared
   -- makes more comparisons along the way in sorted list when required
 - NOTE: the sorted list gets bigger every iteration, and vice versa for unsorted list,

Source: https://www.youtube.com/watch?v=byHi41L9vTM&t=30s
"""


def insert_sort(list_a):
    for i in range(1, len(list_a)):                          # for (initial) unsorted list
        while list_a[i-1] > list_a[i] and i > 0:             # when present item is smaller than the item to the immediate LHS (and is greater than 0)
                                                             # list_a[i-1] = the immediate LHS item; list_a[i] = current item that needs to be sorted
            list_a[i], list_a[i-1] = list_a[i-1], list_a[i]  # swap the value, LHS with RHS
            i -= 1                                           # goes down the list incrementally

    return list_a


print(insert_sort([7, 5, 1, 3, 9, 10, 2]))
