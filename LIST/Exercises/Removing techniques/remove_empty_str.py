list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
new_list = []

# remove None from list1 and convert result into list
res = list(filter(None, list1))
print(res)
