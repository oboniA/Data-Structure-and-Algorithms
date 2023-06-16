"""
wherever there is a B(case-sensitive), swap with e(case-sensitive)
and vice versa
for all the items
"""

list1 = ['Best', 'Ball', 'Egg', 'bEn', 'bEntly', 'eBay']
print('The original list: ', list1)


# joins all the items with a $
# swaps
# splits at every $ to get back the list
joint_list = " $ ".join(list1)
print(joint_list)
swap_list = joint_list.replace("B", "_").replace("e", "B").replace("_", "e").split(' $ ')
print('After swapping: ', swap_list)
