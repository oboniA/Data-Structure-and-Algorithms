"""
ou have given a Python list.
Write a program to find value 20 in the list,
and if it is present, replace it with 200.
only replace the first occurrence
"""

list1 = [5, 10, 15, 20, 25, 50, 20]

# get the first occurrence index
index = list1.index(20)
print(index)

# update item present at location
list1[index] = 200
print(list1)