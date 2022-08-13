"""
are used for creating new lists from other iterables like tuples, strings, arrays, lists, etc
list comprehension consists of brackets containing the expression, which is executed for each element along with the for loop to iterate over each element.

newList = [ expression(element) for element in oldList if condition ]
"""

list1 = [i*i for i in range(5)]
print(list1)