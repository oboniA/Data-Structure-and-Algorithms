"""
Find The Largest Number In A List
"""

# --------------FOR-LOOP method----------------------

list1 = [3, 64, 72, 2, 4, 100, 5]

def largest_num(list1):
    max = 0              # max initiated; assigned to the 0th index of the list

    for i in list1:
        if i > max:      # INITIALLY, if item>0,
            max =  i     # set the max to item; now item is the new max
    return max

print('Largest number in List1 is: ',largest_num(list1))



# ----------------------------SORT---------------------------
my_list = [4, 65, 76, 2, 4, 100, 7]
my_list.sort()                         # sorted in increasing order
print(my_list)                         # largest at the end 
print("largest count_item: ", my_list[-1])



# ------------------------MIN-MAX--------------------------------
my_list2 = [4, 65, 76, 2, 4, 200, 7]
print("largest count_item: ", max(my_list2))
