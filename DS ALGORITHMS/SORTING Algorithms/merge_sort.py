def merge_sorting(arr):
    if len(arr) <= 1:
        return arr

    else:

        left_arr = arr[:len(arr) // 2]                    # everything before the mid-point is left_arr array (l)
        right_arr = arr[len(arr) // 2:]                   # everything after the mid-point is left_arr array (r)

        '''----recursion----'''
        merge_sorting(left_arr)
        merge_sorting(right_arr)

        '''----merge----'''
        i = 0                                            # left_arr-most index of left_arr
        j = 0                                            # left_arr-most index of right_arr
        k = 0                                            # left_arr-most index of merged array
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:               # if value of i is less than j
                arr[k] = left_arr[i]                     # add i to the first index of merged array
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1                                       # k keeps incrementing

        ''' ---------run ONE TIME loop on each list so all the value will end up in merged list--------------'''
        while i < len(left_arr):
            arr[k] = left_arr[i]                        # add current pointer of array "a" to the "arr"
            i += 1                                      # go to next iteration by incrementing i
            k += 1                                      # increment k

        while j < len(right_arr):
            arr[k] = right_arr[j]                       # add current pointer of array "b" to the "arr"
            j += 1                                      # go to next iteration by incrementing j
            k += 1                                      # increment k


array_test = [4, 90, 67, 1, 3, 56, 100, 73, 12, 6]
merge_sorting(array_test)
print(array_test)