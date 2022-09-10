list1 = [105, 'sD', 200, 139, 'Queen', 620, 400, 3]
print('Original list: ', list1)

reversed_list = []

for i in range(1, len(list1)+1):
    reversed_list.append(list1[-i])

print(reversed_list)


