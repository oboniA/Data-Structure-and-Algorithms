'''---------------user input -------------------'''
nList1 = int(input("how manu numbers to multiply?: "))
list1 = []
for n in range(nList1):
    list1.append(int(input()))
print(list1)

mult_count = 1  # not 0 initiated because 0 will give multiple of zeros
for elements in list1:
    mult_count = mult_count * elements
print(mult_count)

