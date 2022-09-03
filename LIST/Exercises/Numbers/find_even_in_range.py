
start = int(input("starting value: "))
end = int(input("ending value: "))

for i in range(start, end+1):
    if i % 2 == 0:
        print(i, end=" ")

