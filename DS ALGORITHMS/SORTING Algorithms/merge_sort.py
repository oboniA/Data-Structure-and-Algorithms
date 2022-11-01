"""
  - data distributed into 2 halves
    -- left half
    -- right half
  - each half are divided into further halves
  - now merge each element by comparing with its other half



SOURCE: https://www.youtube.com/watch?v=cVZMah9kEjI&list=PLO7b4_Ct_NMiFPHgq_WxsOZBhZ9upyQSA&index=23
        https://www.youtube.com/watch?v=8G-PB-RAzdg
"""


# Merging code (2)
def merge_sorting(arr):
    if len(arr) <= 1:
        return arr

    else:
        mid = len(arr) // 2
        left = arr[0:mid]        # everything before the midis left array (l)
        right = arr[mid:]        # everything after the mid is right array (r)
        print("Left array", left, "\nright array: ", right)

        # recursively call ;left and right array
        # this gives the individual elements
        merge_sorting(left)
        merge_sorting(right)

        # merge the elements in sorted order
        i = 0                                   # index0 of left array
        j = 0                                   # index0 of right array
        k = 0                                   # counter for merged array
        while i < len(left) and j < len(right):
            if left[i] < right[j]:              # if value of i is less than j
                arr[k] = left[i]                # add i to index0 merged array
                i += 1                          # go to next index
            else:
                arr[k] = right[j]               # add j to index0 merged array
                j += 1                          # go to next index

            k += 1                              # k keeps incrementing

        # if dataset is ODD, some elements might remain un-compared. In that case:
        # iterates through remaining left array
        while i < len(left):
            arr[k] = left[i]                    # add remainder of left array to merged list
            i += 1                              # increment i
            k += 1                              # increment k

        # iterates through remaining right array
        while j < len(right):
            arr[k] = right[j]                   # add remainder of right array to merged list
            j += 1                              # increment j
            k += 1                              # increment k

        print(arr)

# Driver code (1)
dataset = [14, 30, 57, 1, 21]
print("The original dataset: ", dataset)

merge_sorting(dataset)
print("after merging: ",dataset)      # final (3)
