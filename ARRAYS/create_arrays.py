""" importing array data type
    array(data_type, value_list)
"""

import array as arr1

# a = function.module('',[])
a = arr1.array('i',[1, 3, 67, 89, 10, 2])  # elements stored in a;
                                           # 'i' = integer; 'd' = float
print(a)
print(a[3])

# now print the array in array/list form
for i in range(0, 6):
    print(a[i], end=" ")
print()