n = int(input('Length of the list: '))           # how many elememnt will be added to the list
list1 = []                                       # empty list, where elements will be recorded

for i in range(n):                               # elements within range of 0-n
    list_elements = input("input the count_item: ") # input the elements from user
    list1.append(list_elements)                  # add the user inputs to the empty list

print(list1)                                     # prints the list