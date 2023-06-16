"""
Given a list in Python and provided the positions of the elements,
write a program to swap the two elements in the list.
"""

def swap_position(a, pos1, pos2):

    # popping both the elements from list
    first_element = a.pop(pos1)
    second_element = a.pop(pos2-1)

    # inserting in each others positions
    a.insert(pos1, )
    a.insert(pos2, )

    return a


list1 = [23, 65, 19, 90]
list2 = ['dr','tx', 'yw', 'rt', 'qs']
pos1, pos2  = 1, 3

print(swap_position(list1, pos1-1, pos2-1))
print(swap_position(list2, pos1-1, pos2-1))