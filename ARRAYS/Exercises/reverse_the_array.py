"""
Write a Python program to reverse the order of the items in the array.
"""

# Create Function using Algorithm
'''
     - i = 0th index; j = last index
     - take temporary variable t
     - swapping between i and j 
       --via t
     - Condition: i<j; 
       -- NOT i>=j
'''


arr = [4, 2, 6, 5, 21, 10]
print("The Array before reversing: ",arr)


def reversing(a):       # a is the array
    i = 0
    j = len(a)-1

    while i < j:        # ONLY while i is less than i
        t = a[i]        # t takes the value of the i of array a
        a[i] = a[j]     # i of array a takes the value of the j of array a
        a[j] = t        # j of array a takes the value of t

        i += 1          # increment, i goes forward
        j -= 1          # decrement, j goes backwards

reversing(arr)
print("The Array after reversing", arr)