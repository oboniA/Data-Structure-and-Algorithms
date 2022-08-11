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
        mid = len(arr) // 2            # midpoint is half or the array length
        left = arr[:mid]               # slicing the leftmost half
        right = arr[mid:]              # slicing the rightmost half

    left = merge_sort(left)            # calling the merge_sort function of left array
    right = merge_sort(right)          # calling the merge_sort function of right array

    return merge_sorted_lists(left, right)  # the called functions are returned in the STAGE1 function



# STAGE 1
def merge_sorted_lists(a, b):          # 2 sorted lists will be merged
    merging_list = []                  # empty list initialized, where the both lists are merged
    len_a = len(a)                     # length of list a
    len_b = len(b)                     # length of list b
    i = j = 0                          # two pointers; i for a, j for b

    # ---------------comparing both the list pointers and merging accordingly ----------------------
    while i < len_a and j < len_b:
        if a[i] <= b[j]:               # if pointer at array "a" is smaller than pointer of array b
            merging_list.append(a[i])  # add pointer of array to the merging list
            i += 1                     # go to next iteration by incrementing i
        else:
            merging_list.append(b[j])  # otherwise, add pointer of array "b"
            j += 1                     # go to next iteration by incrementing j

    # ---------run ONE TIME loop on each list so all the value will end up in merged list--------------
    while i < len_a:
        merging_list.append(a[i])      # add current pointer of array "a" to the merging list
        i += 1                         # go to next iteration by incrementing i
    while j < len_b:
        merging_list.append(b[j])      # add current pointer of array "b" to the merging list
        j += 1                         # go to next iteration by incrementing j

    return merging_list



# FINAL STAGE
if __name__ == '__main__':
    arr = [4, 90, 67, 1, 3, 56, 100, 73, 12, 6]

    print(merge_sort(arr))             # final execution is the function of STAGE2

