"""
Given a two Python list.
Write a program to iterate both lists simultaneously
and display items from list1 in original order
and items from list2 in reverse order.
"""

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

zipped_list = zip(list1, list2[::-1])  # list2[::-1] (reverse list using list slicing)

for x,y in zipped_list:
    print(x,y)