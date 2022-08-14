"""
Find The Largest Number In A List
"""

'''---------------user input -------------------'''
nList1 = int(input("how many numbers?: "))
list1 = []

for n in range(nList1):
    list1.append(int(input()))
print(nList1)

'''---------------main code--------------------'''
larg_num = list1[0]  # assigned the largest number to the first index

for n in list1:
    if n > larg_num:
        larg_num =  n
print(larg_num)



'''
def max_num_in_list( list ):
    max = list[ 0 ]
    for a in list:
        if a > max:
            max = a
    return max
print(max_num_in_list([1, 2, -8, 0]))
'''

