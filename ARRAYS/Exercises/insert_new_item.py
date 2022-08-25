"""
insert a new item at a given index position in an array that is created.
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



# Insert a new value at a desired index position
insert_value = int(input("Insert a new item: "))
insert_position = int(input("Where will the new item be inserted?: "))

a.insert(insert_position, insert_value)
print("New array after the insertion: ",a)