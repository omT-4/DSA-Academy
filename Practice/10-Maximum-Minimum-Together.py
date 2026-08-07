# Practice problems: Problem 1
# Write a program to find both the maximum and minimum element in:
numbers = [8, 15, 3, 20, 11]
largest = numbers[0]
smallest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

    if num < smallest:
        smallest = num

print(f"Largest element is {largest}")
print(f"Smalllest element is {smallest}")

# Problem 2
# Find the maximum and minimum in:
numbers = [-10, -25, -3, -40]
largest = numbers[0]
smallest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

    if num < smallest:
        smallest = num

print(f"Largest element is {largest}")
print(f"Smalllest element is {smallest}")

# Problem 3 ⭐ (Dry Run)
# Without running the code:
numbers = [12, 7, 18, 5]
largest = numbers[0]
smallest = numbers[0]

for num in numbers:

    if num > largest:
        largest = num

    if num < smallest:
        smallest = num

print(largest)
print(smallest)
# Write the complete dry run using our academy format.
# Iteration 1
# Question 1
# 12 > 12
# Question 2
# 12 < 12
# Action
# Nothing changes
# Current State
# largest = 12
# smallest = 12

# Iteration 2 
# Question 1
# 7 > 12
# Question 2
# 7 < 12
# Action
# Update smallest
# Current state 
# largest = 12
# smallest = 7

# Iteration 3
# Question 1
# 18 > 12
# Question 2
# 18 < 7
# Action
# Update largest
# Current state
# largest = 18
# smallest = 7

# Iteration 4
# Question 1
# 5 > 18
# Question 2
#  5 < 7
# Action
# Update smallest
# Current state 
# largest = 18
# smallest = 5

# Final output:
# 18
# 5

# Problem 4 ⭐⭐ (Most Important)
# Explain in your own words:
# Why are largest and smallest both initialized with numbers[0] instead of 0?

# Because the guarantee to work as a valid input for positive, negative and mixed elements. Also it is the principle to use a value from the input rather than inventing one 

# Pattern Transfer
# Scenario A
# Find the highest and lowest temperature recorded in a week.
# Which pattern would you use?

# Traversal

# Scenario B
# Count how many students scored above 90 marks.
# Which pattern would you use?

# Traversal + running counter

# Scenario C
# Check if a sentence is a palindrome (ignore spaces for now).
# Which pattern would you use?

# Traversal + two pointers

# Scenario D ⭐

# You need to find:
# the largest element,
# the smallest element,
# and the total sum
# while visiting the array only once.
# Question: Which previously learned patterns would you combine?

# Traversal + accumulation pattern