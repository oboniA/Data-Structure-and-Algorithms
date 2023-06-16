list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_list = ["h", "i", "j"]

# understand indexing
# Sqr_list[2] = ['c', ['d', 'e', ['f', 'g'], 'k'], 'l']
# Sqr_list[2][1] = ['d', 'e', ['f', 'g'], 'k']
# Sqr_list[2][1][2] = ['f', 'g']

list1[2][1][2].extend(sub_list)
print(list1)