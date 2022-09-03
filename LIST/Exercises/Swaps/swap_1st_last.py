"""
Python program to interchange first and last elements in a list
"""

def interchange(a):
    i = 0
    j = len(a)-1

    t = a[i]
    a[i] = a[j]
    a[j] = t

    return a


list1 = [12, 35, 9, 56, 24]
print(interchange(list1))