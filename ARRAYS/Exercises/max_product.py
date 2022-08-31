"""
Write a Python program
to find a pair with the highest product
from a given array of integers.

   - Sort input array in increasing order.
   - If all elements are positive, then return the product of the last two numbers.
   - Else return a maximum of products of the first two and last two numbers.
"""

data = [1, 4, 3, 6, 7, 0]
data2 = [9, 6, 10, -14, -16, 3]


# Time Complexity: O(nlog n)
def max_prod(arr):
    arr.sort()
    print(arr)
    num1 = num2 = 0                              # both nums initiated
    sum1 = arr[0] * arr[1]                       # Calculate product of first 2 items (smallest)
    sum2 = arr[len(arr)-1] * arr[len(arr)-2]     # Calculate product of last 2 items  (largest)

    if sum1 > sum2:                              # if sum1 is greater
        num1 = arr[0]
        num2 = arr[1]
    else:                                        # if sum2 is greater
        num1 = arr[len(arr)-2]
        num2 = arr[len(arr)-1]

    return f"max product pair is {num1},{num2}"


print(max_prod(data))
print(max_prod(data2))
