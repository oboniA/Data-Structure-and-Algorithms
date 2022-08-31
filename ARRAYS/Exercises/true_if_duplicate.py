"""
Write a Python program to find
whether a given array of integers contains any duplicate element.
Return true if any value appears at least twice in the array
and return false if every element is distinct.
"""

array_data = [2, 1, 3, 5, 3, 7, 9, 3]

def duplicate_presence(arr1):
    arr1.sort()                         # sorted the list, so duplicate can be checked in pairs
    print(arr1)

    for i in range(len(arr1)):
        if arr1[i] == arr1[i-1]:        # if the current item is same as the previous,
            return True                 # return True
    return False                        # else, return false by default

print(duplicate_presence(array_data))

