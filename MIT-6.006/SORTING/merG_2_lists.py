"""
Merge sort algorithms
1) a single sorted list formed, from 2 sorted lists {merge_sorted_lists}
2) An UNSORTED list is divided into 2 unsorted lists(arrays), {merge_sort}
   - "left" will take the function of "a"
   - "right" will take the function of "b"
   - merge_sorted_list will; be returned here
3) the merge_sort function will be executed in the end
"""



# STAGE 2
# recursive function
# exit condition: when array size<=1
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2               # midpoint is half or the array length
        left = arr[:mid]                  # slicing the leftmost half
        right = arr[mid:]                 # slicing the rightmost half

    merge_sort(left)                      # calling the merge_sort function of left array
    merge_sort(right)                     # calling the merge_sort function of right array

    merge_sorted_lists(left, right, arr)  # the called functions are returned in the STAGE1 function



# STAGE 1
def merge_sorted_lists(a, b, arr):        # 2 sorted lists will be merged
    len_a = len(a)                        # length of list a
    len_b = len(b)                        # length of list b
    i = j = k = 0                         # two pointers; i for a, j for b; k is for sorted array (arr)

    # ---------------comparing both the list pointers and merging accordingly ----------------------
    while i < len_a and j < len_b:
        if a[i] <= b[j]:                  # if pointer at array "a" is smaller than pointer of array b
            arr[k] = a[i]                 # current pointer place at "arr" will take the current pointer of "a"
            i += 1                        # go to next iteration by incrementing i
        else:
            arr[k] = b[j]                 # otherwise, the current pointer place at "arr" will take the current pointer of "a"
            j += 1                        # go to next iteration by incrementing j
        k += 1                            # for both if-else, increment k
    # ---------run ONE TIME loop on each list so all the value will end up in merged list--------------
    while i < len_a:
        arr[k] = a[i]                     # add current pointer of array "a" to the "arr"
        i += 1                            # go to next iteration by incrementing i
        k += 1                            # increment k
    while j < len_b:
        arr[k] = b[j]                     # add current pointer of array "b" to the "arr"
        j += 1                            # go to next iteration by incrementing j
        k += 1                            # increment k



# FINAL STAGE
if __name__ == '__main__':
    arr = [4, 90, 67, 1, 3, 56, 100, 73, 12, 6]

    merge_sort(arr)
    print(arr)                             # final execution is the function of STAGE2

