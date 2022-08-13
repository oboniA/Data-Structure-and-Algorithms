import  array as arr

list1 = [2, 4, 6, 78, 90, 11, 3, 14, 37]
array1 = arr.array('i', list1)
for i in (array1):
    print(i, end=" ")
print()

print(array1[2:5])           # gives in un-organised form

sliced_array = array1[2:5]
print(sliced_array)          # again gives in un-organised form
for i in (sliced_array):     # now gives in array form
    print(i, end=" ")
print()

