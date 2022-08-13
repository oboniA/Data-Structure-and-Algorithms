"""
are used for creating new lists from other iterables like tuples, strings, arrays, lists, etc
list comprehension consists of brackets containing the expression, which is executed for each element along with the for loop to iterate over each element.

newList = [ expression(element) for element in oldList if condition ]
"""

list1 = []
for i in range(5):       # outs total 5 times
    list1.append(i*i)    # current index times current index
print(list1)             # prints the multiple of the current index with itself, for 5 times


