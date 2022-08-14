""" removes duplicate elements from a given list
 return new list without the duplication """

nums = [1, 3, 67, 89, 1, 3, 45, 66]
no_duplicate = []  # every number stored here will occur once

"""
every number will be checked, and see if it exists in the no_duplicate list,
if doesn/t exist, will be added to the list,
if exists already, will be discarded
will print the list with every number occurring only once 
(hence duplicate removed)
"""
for element in nums:
    if element not in no_duplicate:  # if the current element is not in the list,
        no_duplicate.append(element) # add the element to the list
print(no_duplicate)




