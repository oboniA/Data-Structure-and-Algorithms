"""
Concatenate two lists in the following order

['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
"""

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

concat_list = [(x+y)
               for x in list1
                 for y in list2]
print(concat_list)