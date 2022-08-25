"""
append a new item at the end of an array that is created.
"""

from array import *

# -----------USER INPUT----------------------------------
a = array('i', [])
n = int(input("Input the number of elements: "))

for i in range(n):
    array_elements = int(input("type an element:"))
    a.append(array_elements)
print("The array and it's data type: ", a)
# --------------------------------------------------------


# Append a new value to the array
append_value = int(input("Enter an item to append to the array:"))
a.append(append_value)
print("The new array after appending: ", a)


