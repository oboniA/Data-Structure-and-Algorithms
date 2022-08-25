"""
Write a Python program to get the number of occurrences of a specified element in an array.
"""

from array import *

array_num = array('i', [1, 3, 3, 5, 3, 7, 9, 3])

arr1 = array_num
print(arr1)

count = 0
count_item = 3

for i in arr1:                                          # for elements in the list
    if count_item == i:                                 # if the count_item is same as the element:i
        count += 1                                      # add 1 to the number of counts (increments)

if count == 0:                                          # if counts 0 times,
   print(f"{count_item} do not occur in this list")
else:                                                   # counts once or more
   print(f"{count_item} repeats {count} times")