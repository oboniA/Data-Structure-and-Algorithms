list1 = [5, 20, 15, 20, 25, 50, 20]

def removes(lst):

    while 20 in lst:
        lst.remove(20)
    return lst

print(removes(list1))
