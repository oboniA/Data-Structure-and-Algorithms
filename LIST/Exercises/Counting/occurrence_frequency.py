"""
Frequency of a single count_item in the list
How many times it occurs in the list
"""
print('Frequency of a given count_item in the list')
list1 = [10,10,10,10,20,20,20,20,40,40,50,50,30]
count = 0
count_element = 30

for i in list1:                                         # for elements in the list
    if count_element == i:                              # if the count_item is same as the element:i
        count += 1                                      # add 1 to the number of counts (increments)

if count == 0:                                          # if counts 0 times,
   print(f"{count_element} do not occur in this list")
else:                                                   # counts once or more
   print(f"{count_element} repeats {count} times")



""" 
--------------Frequency of all the elements in a list
              As a dictionary-------------------------
"""
print('Frequency of all the elements in a list')
list2 = [10,10,10,10,20,20,20,20,40,40,50,50,30]
count2 = {}                       # empty dictionary created

for j in list2:                   # for elements in the list
    if j in count2:               # if the count_item is already in the count list,
        count2[j] += 1            # add 1 to the number of counts (increments)
    else:
        count2[j] = 1             # otherwise, keep the count to 1 (because occurs only once)
print(count2)                     # prints count result


# ---------COLLECTION METHOD--------------
import collections
my_list = [10,10,10,10,20,20,20,20,40,40,50,50,30]
print("Original List : ",my_list)
ctr = collections.Counter(my_list)
print("Frequency of the elements in the List : ",ctr)