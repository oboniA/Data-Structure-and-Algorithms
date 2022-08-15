# ----------------APPENDS------------------------------
x = [2, 4, 6, 7, 8]   #  list created
x.append(11)          #  11 is added to the end of the list
print(x)

xx = [2, 4, 6, 7, 8]
xx.append((12, 13))   # this tuple is added to the list
print(xx)

list1 = [1, 2, 3, 0]
list2 = ['R', 'G', 'B']
merge_list = list1 + list2
print(merge_list)


# --------------------EXTENDS----------------------------
x1 = [2, 4, 6, 7, 8]
y1 = [90, 67]
x1.extend(y1)
print(x1)


# --------------------INSERTS-------------------------------
z = [2, 4, 6, 7, 8]
z.insert(3, -4)       # adds -4 to index3
print(z)

z1 = [2, 4, 6, 7, 8]
z1.insert(4, ['e', 'f']) # add the elements to index4
print(z1)                # list inside list

