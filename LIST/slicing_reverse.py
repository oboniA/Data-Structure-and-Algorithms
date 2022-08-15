x = [2, 4, 6, 7, 8]   #  list created
coords = [[1,2,3,4], [5,6,7,8]]  # 0th list; 1st list

print(x[-3])  # prints the third last count_element
print(x[1:-2])

print(coords[1][1:-1])  # from 1st list, prints between index1(inclusive) and index-1(exclusive)

x.reverse()
print(x)

coords.reverse()
print(coords)     # 0th becomes 1st; 1st becomes 0th