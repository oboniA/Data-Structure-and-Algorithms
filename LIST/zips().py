names = ['Oboni', 'Shabnam', 'Aneeza']
age = [24, 24, 21]

# comprehensions
zipped = list(zip(names, age))
print(zipped)

zipped_dict = dict(zip(names, age))
print(zipped_dict)



# for loops
zipd = zip(names, age)

for (a,b) in zipd:
    print(a,b)