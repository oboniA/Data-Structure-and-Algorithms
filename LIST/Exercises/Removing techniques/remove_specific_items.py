list1 = [5, 20, 15, 20, 25, 50, 20]

def removes(lst):
    new_list = []

    for i in lst:
        if i != 20:
            new_list.append(i)
    return new_list

print(removes(list1))
