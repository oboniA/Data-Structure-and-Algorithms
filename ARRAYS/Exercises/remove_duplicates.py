"""
Write a Python program to remove all duplicate elements from a given array and returns a new array
"""

from array import *

nums = array('i', [1, 3, 67, 89, 1, 3, 45, 66])
print('Given array: ', nums)

def remove_dup(nums):
    no_duplicate = []               # every number stored here will occur once

    for i in nums:
        if i not in no_duplicate:   # if the current count_item is not in the list, USE not in INSTEAD OF !=
            no_duplicate.append(i)  # add the count_item to the list
    return no_duplicate             # will output thr new list with no duplicates


print('After removing the duplicate numbers: ', remove_dup(nums))