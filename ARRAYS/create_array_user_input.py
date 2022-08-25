from array import *

arr = array('i', [])
n = int(input("Enter the lenght of the array: "))

for i in range(n):
    array_element = int(input("Enter an element: "))
    arr.append(array_element)
print("The array and it's data type: ", arr)

