# string: append do not work
x = 'computer'
x.append('xyz')
print(x)


# list: APPENDS
y = ['keyboard', 'mouse', 'speaker', 'monitor']
y.append('fruit')
print(y)

# tuple: DO NOT ACCEPT append; once created, it cannot be modified
z = ('keyboard', 'mouse', 'speaker', 'monitor')
z.append('fruit')
print(z)