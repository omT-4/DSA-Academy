# Practice Problems: Problem 1
# Write a program to count the even and odd numbers in:
numbers = [2, 5, 8, 11, 14]
even_count = 0
odd_count = 0
for num in numbers:
    if num % 2 == 0:
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1
print(f"Even count is {even_count}")
print(f"Odd count is {odd_count}")

# Problem 2
# Count the even and odd numbers in:
numbers = [1, 3, 5, 7]
even_count = 0
odd_count = 0
for num in numbers:
    if num % 2 == 0:
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1
print(f"Even count is {even_count}")
print(f"Odd count is {odd_count}")

# # Problem 3 ⭐ (Dry Run)
# Without running the code:
numbers = [6, 9, 12]
even_count = 0
odd_count = 0
for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print(even_count)
print(odd_count)
# Write the complete dry run.

# Iteration 1
# 6 % 2 == 0
# True
# Increase even_count by 1
# Initial even_count = 1

# Iteration 2
# 9 % 2 == 0
# False
# Increase odd_count by 1
# Initial odd_count = 1

# Iteration 3
# 12 % 2 == 0
# True
# Increase even_count by 1
# Initial even_count = 2

# Final output: 
# 2
# 1

# Problem 4 ⭐⭐ (Most Important)
# In your own words, explain:
# Why is counting even and odd numbers considered an extension of the Accumulation Pattern instead of a completely new pattern?

# Because here it follows the same traversal concept every element is visited at least once and and the count is increased when and even or odd number is encountered both it follows both the traversal as well as accumulation pattern. Hence it is considered as an extension of the Accumulation Pattern 