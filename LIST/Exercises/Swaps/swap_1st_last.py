"""
Python program to interchange first and last elements in a list
"""

def interchange(a):

    a[0], a[-1] = a[-1], a[0]

    return a


list1 = [12, 35, 9, 56, 24]
print(interchange(list1))