"""
Write a Python program to find
whether a given array of integers contains any duplicate element.
Return true if any value appears at least twice in the array
and return false if every element is distinct.
"""

array_data = [2, 1, 3, 5, 3, 7, 9, 3]

def duplicate_presence(arr1):

    for i in range(len(arr1)):
        for j in range(i):
            if arr1[i] == arr1[j]:
                return True             # return True
    return False                        # else, return false by default

print(duplicate_presence(array_data))

