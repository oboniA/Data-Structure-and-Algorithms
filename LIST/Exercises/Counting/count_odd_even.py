list1 = [10, 21, 4, 45, 66, 93, 1]

odd_count, even_count = 0, 0

for i in list1:
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Total even numbers: ", even_count)
print("Total odd numbers: ", odd_count)

