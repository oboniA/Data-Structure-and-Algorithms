"""
Write a function that takes two lists
and returns True
if they have at least one common member.
"""

list1 = [2, 3, 4, 7, 8]
list2 = [2, 5, 6, 9, 10]

def common_value(list1, list2):
    result = False                 # default result initiated, meaning if condition don't meet, result will be false

    for i in list1:                # for list1 elements,
        for j in list2:            # for list2 elements
            if i == j:             # ONLY if the count_item of list1 and list2 are the same
                result = True      # return True
    return result                  # return result accordingly

print(common_value(list1, list2))


"""
Write a Python program to get the unique values in the two lists
as a single list
removes the duplicates from both lists
USES SET
"""

l1_l2_diff = list(set(list1) - set(list2))
l2_l1_diff = list(set(list2) - set(list1))
unique_list = l2_l1_diff + l1_l2_diff
print(unique_list)