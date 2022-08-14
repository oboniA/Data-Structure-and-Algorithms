"""
Write a Python program to
sum all the items in a list.
"""

'''
nList1 = int(input("How many numbers in the list?: "))
list1 = []

for e in range(nList1):
    list1.append(int(input()))
print(list1)
'''

list1 = [4 , 7, 12, 32]
sum_list = 0  # initiated the initial variable

for element in list1:
    sum_list = sum_list + element

print("the sum of the given list is: " , sum_list)








'''
def sum_list(items):
    sum_numbers = 0
    for x in items:
        sum_numbers += x
    return sum_numbers
print(sum_list([1,2,-8]))
'''