"""
Write a Python program to
count the number of strings
where the string length is 2 OR more
AND the first and last character are same
from a given list of strings.
"""

str_list1 = ['abc', '123', 'bt34', 'blolpb', '1ookf1', '11']
count = 0

for element in str_list1:
    if len(element) >= 2 and element[0] == element[-1]:
        print(element)
        count = count + 1
print(count)










