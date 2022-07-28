import array as arr1

# a = function.module('',[])
a = arr1.array('i',[1, 3, 67, 89, 10, 2, 67, 10])  # elements stored in a;
                                           # 'i' = integer

a.pop()   # takes out the last index
print(a)

a.pop(-3) # takes out the (current) third last index
print(a)

# run this seperately
a.remove(10)    # removes the first presence of 10
print(a)

