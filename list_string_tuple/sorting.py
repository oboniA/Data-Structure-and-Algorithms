"""
 * takes a string, returns it as list of elements in ascending order
 * returns a list in ascending order
 * returns a tuple in ascending order
"""

#string
x = 'computer'
print(sorted(x))

# list
y = ['keyboard', 'mouse', 'speaker', 'monitor']
print(sorted(y))

# tuple
z = ('keyboard', 'mouse', 'speaker', 'monitor')
print(sorted(z))

# can be sorted at specific position, in this case, the 3rd letter
z2 = ('keyboard', 'mouse', 'speaker', 'monitor')
print(sorted(z, key=lambda k: k[2]))
