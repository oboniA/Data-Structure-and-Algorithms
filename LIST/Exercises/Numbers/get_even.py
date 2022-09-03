"""
GEt the even numbers only in the list
"""

list1 = [70, 70, 11, 4, 20, 4, 100]
even_list = []

for i in list1:
    if i % 2 == 0:
        even_list.append(i)
print("List of even numbers: ",even_list)        # gives in a list

# ---------------------------------------------------------

list2 = [70, 70, 11, 4, 20, 4, 100]

# iterating each number in list
print("individually: ")
for num in list2:
    # checking condition
    if num % 2 == 0:
        print(num, end=" ")     # gives only the numbers
