# Practice problems: Problem 1
# Write a program to search for:
# target = 20
# in:
# numbers = [5, 10, 15, 20, 25]
# Print:
# Element Found
# or
# Element Not Found

numbers = [5, 10, 15, 20, 25]
target = 20
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
# Search for:
# target = 100
# in:
# numbers = [5, 10, 15, 20, 25]
# What will the output be?
# Write the code.
numbers = [5, 10, 15, 20, 25]
target = 100
found = False
for num in numbers:
    if num == target:
        found = True
        break

if found:
    print("Element Found")
else:
    print("Element Not Found")

# Problem 3 ⭐ (Dry Run)
# Without running the code:
numbers = [12, 18, 25, 30]
target = 25
found = False
for num in numbers:
    if num == target:
        found = True
        break
if found:
    print("Found")
else:
    print("Not Found")
# Write the complete dry run and clearly indicate where the loop stops.

# Iteration 1
# 12 == 25
# False

# Iteration 2
# 18 == 25
# False

# Iteration 3
# 25 == 25
# True
# found = True
# loop exits
# No further traversal
# Final output:- Found

# Problem 4 ⭐⭐ (Most Important)
# Answer in your own words:
# Why is break not useful in the Largest Element algorithm but very useful in the Linear Search algorithm?
# Don't just say "because we found the element."
# Explain the reasoning behind it.

# The major different between these two algorithm is that in Largest Element Algorithm we need to visit every element and using break is not useful and does not serve any purpose whereas for Linear Search Algorithm we only need to visit the elements until the target element is not found. When the target element is found the loop terminates saving resources, time and extra work. 