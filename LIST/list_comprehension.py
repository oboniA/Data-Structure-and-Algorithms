"""
are used for creating new lists from other iterables like tuples, strings, arrays, lists, etc
list comprehension consists of brackets containing the expression, which is executed for each count_item along with the for loop to iterate over each count_item.

newList = [ expression(count_item) for count_item in iterable(if/for) ]
"""



'''
(values) = [ (expression) for (value) in (collection) ]

alues = []
for (value) in (collection):
     values.append(expression)    
'''

# For loop
sqr_list1 = []
for i in range(5):
    sqr_list1.append( i * i )
print(sqr_list1)

# List Comprehension
sqr_list2 = [i * i for i in range(5)]    # gives square numbers from 0-4
print(sqr_list2)



# ------------------------------------------------------------------------------
'''
(values) = [ (expression) for (value) in (collection) if (condition) ]

values = []
for (value) in (collection):
      if (condition):
          values.append(expression)     
'''

# For loop
even_sqrs = []
for x in range(10):
    if x % 2 == 0:
        even_sqrs.append( x * x )
print(even_sqrs)

# List Comprehension
evn_sqr = [(x * x) for x in range(10) if (x % 2 == 0)]
print(evn_sqr)

evnsqr = [(x * x)
          for x in range(10)
          if (x % 2 == 0)]        # Good practice
print(evnsqr)



# ------------------------------------------------

num = [4, 52, 6, 17, 8, 92, 130, 11, 2, 13, 4]

dd = []
for i in num:
    if i < 100 and i >= 20:
        dd.append(i)
print(dd)


ddd = list(filter(lambda i: i < 100 and i >= 20, num))
print(ddd)


dddd = [i for i in num if (i < 100 and i >= 20)]
print(dddd)
