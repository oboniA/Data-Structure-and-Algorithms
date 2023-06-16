rows = 4
columns = 2

# for loop append
mtx = []
for r in range(rows):
    row = []
    for c in range(columns):
        row.append("*")
    mtx.append(row)

print(mtx)


# list comprehension
matrix = [["*" for c in range(columns)] for r in range(rows)]
print(matrix)

matrix2 = [["*" for _ in range(columns)] for _ in range(rows)]
print(matrix2)
