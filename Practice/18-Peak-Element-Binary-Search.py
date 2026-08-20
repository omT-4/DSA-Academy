# The problem

# Given:

# numbers = [1, 3, 5, 4, 2]

# Return the index of a peak element.

# Expected result:

# 2

# Because:

# numbers[2] = 5
# Your task

# Write the function:

# def find_peak(numbers):

# Use this structure:

# 1. Initialize left = 0
# 2. Initialize right = len(numbers) - 1
# 3. Use while left < right
# 4. Calculate mid
# 5. Compare numbers[mid] with numbers[mid + 1]


# If numbers[mid] < numbers[mid + 1]:
#     Search RIGHT


# Otherwise:
#     Search LEFT including mid


# 6. Return left

def find_peak(numbers):
    left = 0
    right = len(numbers) - 1

    while left < right:
        mid = (left + right) // 2

        if numbers[mid] <  numbers[mid + 1]:
            left = mid + 1
        else:
            right = mid
    print(left)
    return left

find_peak([1,3,5,4,2])

# Question 4 — Dry Run

# Perform the complete dry run for:

# numbers = [1, 2, 4, 6, 5, 3]

# Use:

# left = 0
# right = len(numbers) - 1


# while left < right:
#     mid = (left + right) // 2

# Show:

# left
# right
# mid
# numbers[mid]
# numbers[mid + 1]
# condition result
# action
# updated pointers
# Continue until the loop ends.

# Initial State
# left = 0
# right = 5

# Iteration 1
# Current State
# left = 0
# right = 5
# mid = 2
# numbers[mid] = 4
# numbers[mid + 1] = 6

# Question
# numbers[mid] <  numbers[mid + 1]
# 4 < 6
# True

# Action
# left = mid + 1 

# Updated State
# left = 3
# right = 5

# Iteration 2
# Current State
# left = 3
# right = 5
# mid = 4
# numbers[mid] = 5
# numbers[mid + 1] = 3 

# Question
# numbers[mid] <  numbers[mid + 1]
# 5 < 3
# False

# Action
# right = mid

# Updated State
# left = 3
# right = 4

# Iteration 3
# Current State
# left = 3
# right = 4
# mid = 3
# numbers[mid] = 6 
# numbers[mid + 1] = 5

# Question
# numbers[mid] <  numbers[mid + 1]
# 6 < 5
# False

# Action
# right = mid

# Updated State
# left = 3
# right = 3

# Iteration 4
# left = 3
# right = 3

# Question
# left < right
# 3 < 3
# False

# Action
# return left

# Final answer = 3

# Lesson 18 - Peak Element Binary Search


def find_peak(numbers):
    left = 0
    right = len(numbers) - 1

    while left < right:
        mid = (left + right) // 2

        if numbers[mid] < numbers[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return left


# Practice 1
numbers = [1, 3, 5, 4, 2]

peak_index = find_peak(numbers)

print("Peak Index:", peak_index)
print("Peak Element:", numbers[peak_index])


# Practice 2
numbers = [1, 2, 4, 6, 5, 3]

peak_index = find_peak(numbers)

print("Peak Index:", peak_index)
print("Peak Element:", numbers[peak_index])


# Practice 3
numbers = [1, 3, 2, 5, 4]

peak_index = find_peak(numbers)

print("Peak Index:", peak_index)
print("Peak Element:", numbers[peak_index])