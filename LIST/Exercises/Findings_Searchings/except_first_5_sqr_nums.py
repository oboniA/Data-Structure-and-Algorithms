"""
Write a Python program to generate and print a list except for the first 5 elements, where the values are square of numbers between 1 and 30 (both included).

returns the square of the values in the list, but deletes the first 5
"""

def generate_list(n):       # of n numbers
    list1 = []              # generated an empty list

    for i in range(1, n):   # for values between 0 and n
        list1.append(i**2)  # add the square of each value in the range
    return list1[5:]        # returns only after first 5 recorded values

print(generate_list(30))
