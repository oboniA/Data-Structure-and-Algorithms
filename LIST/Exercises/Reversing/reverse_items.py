list1 = ['My','Name','is', 'something']
print('original list: ', list1)

item_reversed = lambda i : i[::-1]
reversed = list(map(item_reversed, list1))
print('after reversing: ', reversed)
