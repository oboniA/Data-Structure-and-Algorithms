'''FIND SECOND LARGEST'''

'''--------------------------SORT METHOD-----------------------------------'''
my_list = [3, 5, 78, 98, 35, 26, 8]
my_list.sort()
print('The given list is: ', my_list)
print('Second largest number in the list: ', my_list[-2])



'''------------------------------SET METHOD--------------------------------------------------------------'''
my_list1 = [3, 5, 78, 98, 35, 26, 8]

new_my_list1 = set(my_list1)
new_my_list1.remove(max(new_my_list1))
print(new_my_list1)                        # gives the set of data without the original max value
print(max(new_my_list1))



'''-----------------------------------------------------FOR-LOOP METHOD-----------------------------------------------------------------------------'''
def second_largest(list1):
    unique_list = []                                   # this list is created, so if a value repeats, the repeat will be discarded

    # ---------------------------- creating the unique list first, before checking for second max-------------------------------------------------
    for i in list1:                                    # for elements in list1,
        if i not in unique_list:                       # if element is not in the unique list,
            unique_list.append(i)                      # add it to the list
    print(unique_list)

    # ------------ will search for  max now -------------------------------------------------------------------------------------------------------
    max_val = unique_list[0]                           # initial max_value is assigned to the 0th index of the unique list

    for i in unique_list:                              # for the elements in the unique list,
        if i > max_val:                                # if the current item is greater than the current max
            max_val = i                                # make the current item the new max value

    # ------------- will search for  second max now -----------------------------------------------------------------------------------------------
    second_max_val = unique_list[0]                    # initial second_max_value is assigned to the 0th index of the unique list

    for i in unique_list:
        if (i > second_max_val) and (i != max_val):    # if the current item is greater than the current second max AND not equal to the max value
            second_max_val = i                         # make the current item the new max value
    return  second_max_val

print('The Second largest value is: ', second_largest([4, 6, 7, 90, 12, 7, 4, 90, 101]))

