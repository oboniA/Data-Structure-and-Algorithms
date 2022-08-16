""" removes duplicate elements from a given list
 return new list without the duplication

every number will be checked, and see if it exists in the no_duplicate list,
if doesn't exist, will be added to the list,
if exists already, will be discarded
will print the list with every number occurring only once 
(hence duplicate removed)
"""
nums = [1, 3, 67, 89, 1, 3, 45, 66]
print('Given list: ', nums)

def remove_dup(nums):
    no_duplicate = []               # every number stored here will occur once

    for i in nums:
        if i not in no_duplicate:   # if the current count_element is not in the list, USE not in INSTEAD OF !=
            no_duplicate.append(i)  # add the count_element to the list
    return no_duplicate             # will output thr new list with no duplicates


print('After removing the duplicate numbers: ',remove_dup(nums))



# using SET method
nums1 = [1, 3, 67, 89, 1, 3, 45, 66]
print('Given list: ', nums1)

nums1_set = set(nums1)                # making a SET
print('Unique SET of numbers: ', nums1_set)                      # prints the SET (no duplicates)
nums1_set_to_list = list(nums1_set)   # converting from SET to list
print('Unique LIST of numbers: ',nums1_set_to_list)              # prints the list with no duplicates/unique numbers
