"""
all the arrays to be concatenated as to have same data types
"""

import array as arr1

# a = function.module('',[])
a = arr1.array('i', [1, 3, 67, 89, 10, 2])  # elements stored in a;
                                           # 'i' = integer
b = arr1.array('i', [1, 5, 64, 82, 13, 3])

c = a+b    # concatenated; both arrays made into single 1D array
print(c)
