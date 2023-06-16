"""
Python program to interchange first and last elements in a list
"""

def interchange(a):

    start, *middle, end = a
    a = [end, *middle, start]

    return a


list1 = [12, 35, 9, 56, 24]
print(interchange(list1))