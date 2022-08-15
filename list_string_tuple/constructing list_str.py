# GIVEN METHOD
list_char = ['a', 'b', 'c', 'd']
list_to_str = ' '.join(list_char)

print(list_to_str)



# USER INPUT
n = int(input('Length of the list: '))           # how many elememnt will be added to the list
list1 = []                                       # empty list, where elements will be recorded

for i in range(n):                               # elements within range of 0-n
    list_elements = input("input the element: ") # input the elements from user
    list1.append(list_elements)                  # add the user inputs to the empty list
print(list1)                                     # prints the list

list1_to_str = ' '.join(list1)
print(list1_to_str)