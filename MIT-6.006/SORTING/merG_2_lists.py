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



if __name__ == '__main__':
    a = [3, 5, 7, 11, 21]
    b = [2, 6, 7, 9, 13, 16, 19]

    print(merge_sorted_lists(a, b))

