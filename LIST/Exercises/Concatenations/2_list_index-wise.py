"""
add two lists index-wise.
Create a new list that contains the 0th index item from both the list,
then the 1st index item,
and so on till the last element.
any leftover items will get added at the end of the new list.

(values) = [(expression) for (value) in (condition)
"""

list1 = ["M", "na", "i", "Ob"]
list2 = ["y", "me", "s", "oni"]

list_concat = [(i + j) for i, j in zip(list1, list2)]
print(list_concat)   # NOTICE: between i[0] and j[0] (and so on), there is no space