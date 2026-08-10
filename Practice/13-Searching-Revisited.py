# Lesson 13 - Searching Revisited
# Practice problems: Problem 1
# Implement Linear Search for:
# numbers = [10, 20, 30, 40, 50]
# target = 40
# Print "Element Found" or "Element Not Found"
numbers = [10, 20, 30, 40, 50]
target = 40
found = False
for num in numbers:
    if num == target:
        found = True
        break
if found:
    print("Element Found")
else:
    print("Element Not Found")

# Problem 2
# Implement Linear Search for:
# numbers = [5, 15, 25, 35, 45]
# target = 100
# Print "Element Found" or "Element Not Found"
numbers = [5, 15, 25, 35, 45]
target =  100
for num in numbers:
    if num == target:
        found = True
        break
if found:
    print("Element Found")
else:
    print("Element Not Found")

# Problem 3
# Find the number of comparisons required to find:
# target = 50
# in:
# numbers = [10, 20, 30, 40, 50]
# Think about:
# How many elements does Linear Search check?

# target = 50
# 10 - comparison 1
# 20 - comparison 2
# 30 - comparison 3
# 40 - comparison 4
# 50 - comparison 5
# Total comparison = 5


# Problem 4
# Find the number of comparisons required to find:
# target = 10
# in:
# numbers = [10, 20, 30, 40, 50]
# Think about:
# What does this tell us about the best case?

# The number of iterations performed by the code is 1. The time complexity for this code is O(1)

# Problem 5
# The target is not present:
# numbers = [10, 20, 30, 40, 50]
# target = 35
# Think about:
# How many elements must Linear Search check?
# What is the worst-case time complexity?

# Linear search checks every element in the array.
# This is the worst case scenario because the code performs n number of iterations making the time complexity as O(n)
