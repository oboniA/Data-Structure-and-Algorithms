str1 = input("Enter the strings contained in the list: ")
print('The entry: ',str1)

list_words = str1.split()
print('Convert the entry to a list: ', list_words)

reverse_list = []

for i in list_words:
    reverse_list.append(i[::-1])
print(reverse_list)




