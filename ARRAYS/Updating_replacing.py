import array as arr

a = arr.array('i', [1, 2, 3, 1, 2, 5])
print("Array before updating : ", end="")
for i in range(0, len(a)):
    print(a[i], end=" ")
print()

a[2] = 6        # replacing the index2 value with 6
print("Array after updation : ", end ="")
for i in range (0, len(a)):
    print(a[i], end =" ")
print()

