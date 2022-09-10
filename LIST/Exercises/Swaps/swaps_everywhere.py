list1 = ['Best', 'Ball', 'Egg', 'bEn', 'bEntly', 'eBay']
print('The original list: ', list1)

swap_list = [sub.replace('B', '-').replace('e', 'B').replace('-', 'e') for sub in list1]
print('After swapping: ', swap_list)
