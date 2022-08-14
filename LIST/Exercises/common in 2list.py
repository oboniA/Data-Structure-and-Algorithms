"""
Write a function
that takes two lists
and returns True if they have at least one common member
"""


list1 = [ 1, 3, 5]
list2 = [2, 4, 6]

for x in list1:
  for y in list2:
     if x==y:
     print("True")



'''def common(list1, list2):
 result = False

 for x in list1:
   for y in list2:
      if (x==y) :
        result = True
        return result
      else:
        return result

print(common([1,2,3,4], [1,7,8,9]))
'''

