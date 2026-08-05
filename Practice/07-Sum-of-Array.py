# Practice Problems: Problem 1
# Write a program to find the sum of:
numbers = [5, 10, 15, 20]
total = 0
for num in numbers:
    total = total + num
print(total)

# Problem 2
# Find the sum of:
numbers = [-5, 10, -15, 20]
total = 0
for num in numbers:
    total = total + num
print(total)

# Problem 3 ⭐ (Dry Run)
# Without running the code:
numbers = [4, 6, 3]
total = 0
for num in numbers:
    total = total + num
print(total)
# Write the complete dry run.
# Iteration 1 
# 0 = 0 + 4
# Update total
# total = 4

# Iteration 2
# 4 = 4 + 6
# Update total
# total = 10

# Iteration 3
# 10 = 10 + 3
# Update total
# total = 13

# Final Output = 13

# Problem 4 ⭐⭐ (Most Important)
# In your own words, explain:
# Why do we initialize total = 0, but initialize largest = numbers[0]?
# This is one of the most common interview questions because it checks whether you understand the difference between accumulation and comparison. Don't just state the answer—explain the reasoning behind it.

# Because we are performing addition and zero is the identity element of addition whereas we initialize largest = numbers[0] because it guarantees a valid element in the input making the algorithm work correctly with positive, negative, mixed and single element array 