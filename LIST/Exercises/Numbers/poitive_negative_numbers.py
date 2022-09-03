# --------Gives in Lists---------------
list1 = [11, -21, 0, 45, 66, -93]
pos_list = []
neg_list = []

for i in list1:
    if i >= 0:
        pos_list.append(i)
    else:
        neg_list.append(i)

print("List of positive numbers: ", pos_list)
print("List of negative numbers: ", neg_list)


# ----------Individually-----------------
list2 = [11, -21, 0, 45, 66, -93]

print("+ve Numbers: ")
for num in list2:
    if num >= 0:
        print(num, end=" ")

print("\n-ve numbers: ")
for num2 in list2:
    if num2 < 0:
        print(num2, end=" ")

