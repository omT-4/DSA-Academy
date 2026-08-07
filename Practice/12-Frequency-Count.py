# Practice problems: Problem 1
# Write a program to count the frequency of:
numbers = [3, 7, 3, 2, 7, 3]
# Expected output
# 3 → 3
# 7 → 2
# 2 → 1
frequency = {}
for num in numbers:
    if num in frequency:
        frequency[num]+=1
    else:
        frequency[num]=1
print(frequency)

# Problem 2
# Find the frequency of:
numbers = [5, 5, 5, 5]
frequency = {}
for num in numbers:
    if num in frequency:
        frequency[num]+=1
    else:
        frequency[num]=1
print(frequency)

# Problem 3 ⭐ (Dry Run)
# Without running the code:
numbers = [1,2,1]
frequency = {}
for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1
print(frequency)
# Write the complete dry run using our academy format.

# Current state
# frequency = {}

# Iteration 1
# Current number 
# 1
# Question
# Does 1 exist?
# No
# Action
# Create
# 1 -> 1
# Memory
# {
#     1 -> 1
# }

# Iteration 2
# Current number 
# 2
# Question
# Does 2 exist?
# No
# Action
# Create
# 2 -> 1
# Memory
# {
#     1 -> 1
#     2 -> 1
# }

# Iteration 3
# Current number 
# 1
# Question
# Does 1 exist?
# Yes
# Action
# Increase count
# Memory
# {
#     1 -> 2
#     2 -> 1
# }

# Problem 4 ⭐⭐ (Most Important)
# Explain in your own words:
# Why can't we solve frequency counting efficiently using only a few variables like largest, smallest, or count? Why do we need a dictionary?

# Because using such variables comes with its limitation. Dictionary serves a different purpose. 

# Pattern Transfer
# Scenario A
# Frequency counting
# Scenario B
# Frequency counting
# Scenario C
# Traversal + frequency counting
# Scenario D
# I would reuse today's algorithm because the question itself mentions the count of frequency