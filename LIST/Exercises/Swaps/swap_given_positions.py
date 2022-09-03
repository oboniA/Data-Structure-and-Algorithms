"""
Given a list in Python and provided the positions of the elements,
write a program to swap the two elements in the list.
"""

def swap_position(a, pos1, pos2):

    a[pos1], a[pos2] = a[pos2], a[pos1]
    return a


list1 = [23, 65, 19, 90]
pos1, pos2  = 1, 3
print(swap_position(list1, pos1-1, pos2-1))