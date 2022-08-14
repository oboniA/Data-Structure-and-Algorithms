def generate_list(n):       # of n numbers
    list1 = []              # generated an empty list

    for i in range(1, n):   # for values between 0 and n
        list1.append(i**2)  # add the square of each value in the range
    return list1[5:]        # returns only after first 5 recorded values

print(generate_list(30))
