"""
Add new item to list after a specified item
add 8000 after 6000
"""

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

# understand indexing
# Sqr_list[0] = 10
# Sqr_list[1] = 20
# Sqr_list[2] = [300, 400, [5000, 6000], 500]
# Sqr_list[2][2] = [5000, 6000]
# Sqr_list[2][2][1] = 6000

list1[2][2].append(8000)
print(list1)
