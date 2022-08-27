"""
are used for creating new lists from other iterables like tuples, strings, arrays, lists, etc
list comprehension consists of brackets containing the expression, which is executed for each count_item along with the for loop to iterate over each count_item.

newList = [ expression(count_item) for count_item in iterable( ]
"""

list1 = [i*i for i in range(5)]
print(list1)
