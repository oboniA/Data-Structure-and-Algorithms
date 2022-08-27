"""
reversing a sorted/unsorted array
"""
arr = [4, 2, 6, 5, 21, 10]
print("The Array 1 before reversing: ",arr)

arr2 = [3, 5, 6, 8, 9]
print("The Array 2 before reversing: ",arr2)


def reversing(a):       # a is the array
    i = 0               # initialized; first i=index0
    j = len(a)-1        # initialized; first j=LASTindex

    while i < j:        # ONLY while i is less than j
        t = a[i]        # t takes the value of the i of array a
        a[i] = a[j]     # i of array a takes the value of the j of array a
        a[j] = t        # j of array a takes the value of t

        i += 1          # increment, i goes forward
        j -= 1          # decrement, j goes backwards

reversing(arr)
print("The Array 1  after reversing", arr)

reversing(arr2)
print("The Array 2 after reversing", arr2)