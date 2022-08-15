coords = [[1,2,3,4], [5,6,7,8]]  # 0th list: 0 1 2 3 index, 1st list: 0 1 2 3 index
print(coords)
print(coords[1][2])   # give the value from 1st Row and 2nd column
                      # OR, gives, the index2 from 1st list


# FLATTEN a SHALLOW LIST
import itertools
list1 = [[2,4,3],[1,5,6], [9], [7,9,0]]
new_list = list(itertools.chain(*list1))
print(new_list)
print(list1[3][1])