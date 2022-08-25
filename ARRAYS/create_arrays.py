""" importing array data type
    array(data_type, value_list)
"""

import array as arr1

# a = function.module('',[])
a = arr1.array('i',[1, 3, 67, 89, 10, 2])  # elements stored in a;
                                           # 'i' = integer; 'd' = float
print("The array and it's data type is: ", a)
print("the third index of the array is: ",a[3])

# now print the array in array/list form
print("The array: ")
for i in range(0, len(a)):
    print(a[i], end=" ")
print()


# ALSO can be created like:
list1 = [1, 3, 67, 89, 10, 2]
aa = arr1.array('d', list1)
print(aa)
