"""
how many times an item appears and their indexes
"""

x = 'computer'
print(x.count('o'))
print(x.index('o'))


# list
y = ['keyboard', 'mouse', 'speaker', 'monitor', 'mouse']
print(y.count('mouse'))
print(y.count('horse'))
print(y.count('monitor'))

print(y.index('mouse'))    # will give the first occurance


# tuple
z = ('keyboard', 'mouse', 'speaker', 'monitor')
print(z.count('mouse'))
print(z.count('horse'))
print(z.count('monitor'))

print(z.index('mouse'))