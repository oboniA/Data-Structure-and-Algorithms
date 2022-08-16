list1 = [7,8, 120, 25, 44, 20, 27]

def remove_even(list1):
    new_list = []

    for i in list1:
        if i % 2 != 0:
            new_list.append(i)
    return new_list

print(remove_even(list1))