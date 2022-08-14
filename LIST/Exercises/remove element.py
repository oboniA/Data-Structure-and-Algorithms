"""
Write a program to
print a specified list
after removing the 0th, 4th and 5th elements
"""

list1 = ['blue', 'pink', 'red', 'green', 'black', 'white']


for e in list1:
    if e not in (0,4,5):
        print(e, end=" ")
