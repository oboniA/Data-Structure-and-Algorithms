import array as arr1

# a = function.module('',[])
a = arr1.array('i',[1, 3, 67, 89, 10, 2])  # elements stored in a;
                                           # 'i' = integer

a.append(5)  # adds 5 at the end of the array
print(a)


a.extend([8, 9, 11, 12])  # added at the end of the array
print(a)


a.insert(3, 121)      # 121 is added at index3
                      # previous index3 is shifted; is index4 now
print(a)