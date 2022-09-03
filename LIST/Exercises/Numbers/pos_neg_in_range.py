"""
Python program to print all positive and negative numbers in a range
"""

# ---------------INDIVIDUALLY--------------------------
start = -13
end = 16

print("positive numbers: ")
for i in range(start, end+1):
    if i >= 0:                   # positive numbers
        print(i, end=" ")

print("\nnegative numbers: ")
for j in range(start, end+1):
    if j < 0:                   # negative numbers
        print(j, end=" ")

# ---------------IN A LIST -------------------------------


s = -6
e = 14
pos_list = []
neg_list = []
for item in range(s, e+1):
    if item >= 0:                   # positive numbers
        pos_list.append(item)
    else:                           # negative numbers
        neg_list.append(item)

print("\nList of positive numbers: ", pos_list)
print("List of negative numbers: ", neg_list)
