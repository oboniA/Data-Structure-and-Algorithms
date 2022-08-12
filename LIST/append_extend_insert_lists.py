x = [2, 4, 6, 7, 8]   #  list created
x.append(11)          #  11 is added to the end of the list
print(x)

x1 = [2, 4, 6, 7, 8]
y1 = [90, 67]
x1.extend(y1)
print(x1)


z = [2, 4, 6, 7, 8]
z.insert(3, -4)       # adds -4 to index3
print(z)

z1 = [2, 4, 6, 7, 8]
z1.insert(4, ['e', 'f']) # add the elements to index4
print(z1)                # list inside list

