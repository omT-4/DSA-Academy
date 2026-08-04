# Problem 1
# Write a program to find the smallest element in:
numbers = [25, 10, 35, 5, 18]
smallest = numbers[0]
for num in numbers:
    if num < smallest:
        smallest = num

print(smallest)

# Problem 2
# Find the smallest element in:
numbers = [-3, -15, -7, -1]
smallest = numbers[0]
for num in numbers:
    if num < smallest:
        smallest = num

print(smallest)

# Problem 3
# Without running the code, tell me the output.
numbers = [9, 4, 12, 2]

smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num

print(smallest)

# Write the complete dry run.
# Iteration 1 
# 9 < 9
# False
# smallest = 9

# Iteration 2
# 4 < 9
# True
# Update smallest
# smallest = 4

# Iteration 3
# 12 < 4
# False
# smallest = 4

# Iteration 4
# 2 < 4
# True
# Update smallest
# smallest = 2

# Final output = 2

# Problem 4 (Pattern Recognition ⭐)
# In your own words, explain:
# Why do you think Largest Element and Smallest Element are considered the same algorithmic pattern instead of two different algorithms?
# This last question is the most important one because it checks whether you've understood the idea of reusing patterns, not just changing code.

# Because the overall process to execute both the problems is the same i.e. they are the same comparison pattern. Solutions of both the problems do not require any major change i.e. they only require a change in sign and a different variable. Excluding these two changes the overall process is the same 

# Same traversal ✅
# Same comparison pattern ✅
# Only comparison operator changes ✅
# Variable name changes ✅
# This is called algorithm abstraction.