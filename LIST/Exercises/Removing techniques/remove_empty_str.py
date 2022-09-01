list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
new_list = []

for i in list1:
    if len(i) >= 1:
        new_list.append(i)
print(new_list)
