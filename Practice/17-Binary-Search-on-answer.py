# Initial State
# left = 1
# right = 10
# answer = -1

# Iteration 1
# Current State
# left = 1
# right = 10
# answer = -1

# mid = (left+right)//2
# mid = 5

# Question 
# 5 * 5 >=30
# 25 >= 30
# False

# Action
# left = mid + 1
# left = 6

# Updated State
# left = 6
# right = 10
# answer = -1

# Iteration 2
# Current State
# left = 6
# right = 10
# answer = -1

# mid = (left+right)//2
# mid = 8

# Question 
# 8 * 8 >= 30
# 64 >= 30
# True

# Action
# answer = mid
# right = mid - 1
# right = 7

# Updated State
# left = 6
# right = 7
# answer = 8

# Iteration 3
# Current State
# left = 6
# right = 7
# answer = 8

# mid = (left+right)//2
# mid = 6

# Question 
# 6 * 6 >= 30
# 36 >= 30
# True

# Action
# answer = mid
# right = mid - 1
# right = 5

# Updated State
# left = 6
# right = 5
# answer = 6

# Iteration 4
# Current State
# left = 6
# right = 5
# answer = 6

# Question
# 6 <= 5
# False

# Action 
# return answer

# weights = [3, 2, 2, 4, 1, 4]
# days = 3
# capacity = 5

# Initial:
# current_load = 0
# days_used = 1

# Package = 3
# Action = 
# current_load = 3 

# Package = 2
# Action =
# current_load =

# Package = 2
# Action =
# current_load =
# days_used =

# def can_process(weights, days, capacity):
#     current_load = 0
#     days_used = 1

#     for weight in weights:
#         if current_load + weight <= capacity:
#             current_load += weight
#         else:
#             days_used += 1
#             current_load = weight

#             if days_used > days:
#                 return False

#     return True
# can_process([3, 2, 2, 4, 1, 4], 3, 5)
# left = max(weights)
# right = sum(weights)
# answer = -1

# while left <= right:

#     mid = (left + right) // 2

#     if can_process(weights, days, mid):
#         answer = mid
#         right = mid - 1

#     else:
#         left = mid + 1

# return answer

# Find the maximum x such that x × 4 <= 30.
# Initial State
# left = 1
# right = 10
# answer = -1

# Iteration 1
# Current State
# left = 1
# right = 10
# answer = -1

# mid = 5

# Question
# mid * 4 <=30
# 20 <= 30
# True

# Action 
# Save mid
# Search right 
# left = 6

# Updated State
# left = 6
# right = 10
# answer = 5

# Iteration 2
# Current State
# left = 6
# right = 10
# answer = 5

# mid = 8

# Question 
# mid * 4 <= 30
# 32 <= 30
# False

# Action
# Search LEFT
# right = 7

# Updated State
# left = 6
# right = 7
# answer= 5

# Iteration 3
# left = 6
# right = 7
# answer= 5

# mid = 6

# Question
# mid * 4 <= 30
# 24 <= 30
# True

# Action
# Save mid
# Search RIGHT
# left = 7

# Updated State
# left = 7
# right = 7
# answer = 6

# Iteration 4
# Current State
# left = 7
# right = 7
# answer = 6

# mid = 7

# Question 
# mid * 4 <= 30
# 28 <= 30
# True

# Action
# Save mid
# Search RIGHT 
# left = 8

# Updated State
# left = 8
# right = 7
# answer = 7

# Iteration 5
# Current State
# left = 8
# right = 7
# answer = 7

# mid = 7

# Question 
# 8 <= 7
# False

# Action
# Return answer

# Final answer = 7

# Problem 1 — Minimum Hours

# A machine processes 6 items per hour.

# You need to process at least 35 items.

# Write a function that finds the minimum number of hours required.

# Given
# items_per_hour = 6
# target_items = 35

# Expected answer:

# 6
# Your function should follow this structure
# def minimum_hours(items_per_hour, target_items):
#     # your code
# Requirements

# Use:

# left
# right
# answer
# while left <= right
# mid
# A condition checking whether mid hours are sufficient
# Minimum-valid pattern

# Remember:

# TRUE  → save answer → search LEFT
# FALSE → search RIGHT
# One important thing

# For this problem, don't use can_process().

# The condition is simple enough to write directly:

# mid × items_per_hour >= target_items

# So the flow is:

#         mid
#          ↓
# mid × 6 >= 35?
#      ↙       ↘
#   FALSE      TRUE
#     ↓          ↓
#   RIGHT     SAVE + LEFT
# def minimum_hours(items_per_hour, target_items):
#     left = 1
#     right = 10
#     answer = -1

#     while left <= right:
#         mid = (left + right)//2

#         if mid * items_per_hour >= target_items:
#             answer = mid 
#             right = mid - 1
#         else:
#             left = mid + 1
#     return answer

# minimum_hours(6, 35)

# def maximum_hours(items_per_hour, max_items):
#     left = 1
#     right = 10
#     answer = -1
#     while left <= right:
#         mid = (left + right)//2

#         if mid * items_per_hour <= max_items:
#             answer = mid
#             left = mid + 1
#         else:
#             right = mid - 1
#     return answer
# maximum_hours(7, 50)

def can_process(weights, days, capacity):
    current_load = 0
    days_used = 1
    for weight in weights:
        if current_load + weight <= capacity:
            current_load += weight
        else:
            days_used += 1
            current_load = weight

            if days_used > days:
                return False

    return True
def minimum_capacity(weights, days):
    left = max(weights)
    right = sum(weights)
    answer = -1

    while left <= right:

        mid = (left + right) // 2

        if can_process(weights, days, mid):
            answer = mid
            right = mid - 1

        else:
            left = mid + 1
    print(answer)
    return answer

minimum_capacity([3, 2, 2, 4, 1, 4], 3)