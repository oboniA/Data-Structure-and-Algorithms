"""
same for append, insert, extend
"""

import array as arr1

# APPENDS
# a = function.module('',[])
a = arr1.array('i',[1, 3, 67, 89, 10, 2])  # elements stored in a; i' = integer
print("ARRAY before appending: ")
for i in range(0, len(a)):
    print(a[i], end=" ")
print()

a.append(5)  # adds 5 at the end of the array
print("ARRAY after appending: ")
for i in (a):
    print(i, end=" ")
print()


''''
a.extend([8, 9, 11, 12])  # added at the end of the array
print(a)


a.insert(3, 121)      # 121 is added at index3
                      # previous index3 is shifted; is index4 now
print(a)
'''

# EXTENDS
a1 = arr1.array('d',[2, 3, 63, 80, 14, 21])
print("ARRAY before extending: ")
for i in range(0,len(a1)):
    print(a1[i], end=" ")
print()

a1.extend([8, 9, 11, 12])
print("ARRAY after extending: ")
for i in (a1):
    print(i, end=" ")
print()