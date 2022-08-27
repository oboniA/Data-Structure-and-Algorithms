"""
Sort a given list of items in Ascending order
  -- replace > with < for descending order
"""

list1 = [5, 7, 9, 4, 3, 6]
print("Unsorted original list:",list1)

i = 0                                      # initialized to zero; the first i is 0th index; that means first i+1 is 1st index
for i in range(len(list1)):                # for all the items in the list
    for j in range(i+1, len(list1)):       # for item between the next and last in the list
        if list1[i] > list1[j]:            # if the present item is greater than the next one
            t = list1[i]                   # t takes the value of the i
            list1[i] = list1[j]            # i takes the value of the j
            list1[j] = t                   # j takes the value of t

print("Sorted in ascending order:",list1)
