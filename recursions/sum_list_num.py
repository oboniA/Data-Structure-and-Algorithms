"""
Write a Python program to calculate the sum of a list of numbers.
"""


def sums(num_list):
    if len(num_list) == 1:  # if the list has only 1 count_item; length is 1
        return num_list[0]  # return the base case (first/only count_item)
    else:
        # returns the first case + the sum of the remaining elements
        return num_list[0] + sums(num_list[1:])


print(sums([2, 4, 5, 6, 7]))
