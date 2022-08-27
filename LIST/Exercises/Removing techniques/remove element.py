"""
Write a program to
print a specified list
after removing the 0th, 4th and 5th elements
"""

list1 = ['Red', 'Green',  'White', 'Black', 'Pink', 'Yellow']  # list created

def remove_elements(list1):
  new_list = []                      # empty list where the remaining values will be stored

  for i in range(len(list1)):        # for elements within the list range,
     if i not in (0, 4, 5):          # if the count_item is not index0,4,5
        new_list.append(list1[i])    # add the count_item to the empty list
  return new_list                    # the new list will be returned


print(remove_elements(list1))
