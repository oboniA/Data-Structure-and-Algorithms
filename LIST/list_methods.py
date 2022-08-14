nums = [3, 5, 7, 1, 9, 4, 5]  # List of numbers
nums2 = nums.copy()  # makes a copy of the original

print(nums)
print(nums2)

nums.append(-3)  # adds new number to the list
nums.insert(2, -5)  # adds -5 to the 0th index
nums.remove(9)  # removes 9
nums.pop()  #removes the last

print(nums.index(7))  # gives the index of the first occurrence
print(52 in nums)  # tells if 50 exists in the nums list. (ans true/false)
print(nums.count(5))  #how many times has 5 occurred

nums.sort()  # sorts
nums.reverse()  # reverses the sort
print(nums)  # sorted/reversed the list

nums.clear()  # prints empty list