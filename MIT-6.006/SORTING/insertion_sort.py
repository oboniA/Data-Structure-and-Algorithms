def insert_sort(list_a):
    for i in range(1, len(list_a)):                              # for every value(i) within that length of given list
        while list_a[i] < list_a[i-1] and i>0 :                  # when current value is smaller than the previous value (and value is greater than 0)
            list_a[i], list_a[i-1] = list_a[i-1], list_a[i]      # swap the value, LHS with RHS
            i -= 1                                               # continues the comparison and swap with all the elements

    return list_a

print(insert_sort([7, 5, 1, 3, 9, 10, 2]))



"""
Source: https://www.youtube.com/watch?v=byHi41L9vTM&t=30s
"""
