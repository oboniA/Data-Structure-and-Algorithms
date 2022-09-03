"""
Given a list in Python and provided the positions of the elements,
write a program to swap the two elements in the list.
"""

def swap_position(a, pos1, pos2):

    t = a[pos1]
    a[pos1] = a[pos2]
    a[pos2] = t

    return a


print(swap_position([1, 2, 3, 4, 5], 1, 4))