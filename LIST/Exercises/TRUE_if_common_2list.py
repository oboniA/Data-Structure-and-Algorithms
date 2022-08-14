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
            if i == j:             # ONLY if the element of list1 and list2 are the same
                result = True      # return True
    return result                  # return result accordingly

print(common_value(list1, list2))