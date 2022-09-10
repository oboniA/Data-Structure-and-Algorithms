list1 = [105, 'sD', 200, 139, 'Queen', 620, 400, 3]
print('Original list: ', list1)

def reverse_list(l):
    i = 0                # first item
    j = len(l) - 1       # last item

    while i < j:
        t = l[i]
        l[i] = l[j]
        l[j] = t

        i += 1
        j -= 1

reverse_list(list1)
print('After reversing', list1)


