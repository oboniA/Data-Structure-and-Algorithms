"""
Write a Python program to reverse the order of the items in the array.
"""

from array import *

a = array('i', [3, 6, 8, 10, 21, 34, 54])
print("Array before reversing: ",a)

a.reverse()
print("array after reversing: ", a)
