# numbers = [2, 4, 4, 4, 4, 6, 8]
# target = 4
# Initial:
# left = 0
# right = 6
# answer = -1

# Iteration 1
# Current State
# left = 0
# right = 6
# answer = -1

# mid = (left+right)//2
# mid = (0+6)//2
# mid = 3
# numbers[mid] = 4

# Question
# numbers[mid] == target
# 4 == 4
# True

# Action
# Save mid
# right = mid - 1

# Updated State
# left = 0
# right = 2
# answer = 3

# Iteration 1
# Current State
# left = 0
# right = 2
# answer = 3

# mid = (left+right)//2
# mid = (0+2)//2
# mid = 1
# numbers[mid] = 4

# Question
# numbers[mid] == target
# 4 == 4
# True

# Action
# Save mid
# right = mid - 1

# Updated State
# left = 0
# right = 0
# answer = 1

# Iteration 3
# Current State
# left = 0
# right = 0
# answer = 1

# mid = (left+right)//2
# mid = (0+0)//2
# mid = 0
# numbers[mid] = 2

# Question
# numbers[mid] == target
# 2 == 4
# False

# numbers[mid] < target
# True

# Action
# left = mid + 1

# Updated State
# left = 1
# right = 0
# answer = 1

# Iteration 4 
# Current State
# left = 1
# right = 0
# answer = 1

# Question
# left <= right

# Action
# return answer

# numbers = [2, 4, 4, 4, 4, 6, 8]
# target = 4
# Initial:
# left = 0
# right = 6
# answer = -1

# Iteration 1
# Current State
# left = 0
# right = 6
# answer = -1

# mid = (left+right)//2
# mid = (0+6)//2
# mid = 3
# numbers[mid] = 4

# Question
# numbers[mid] == target    
# 4 == 4
# True

# Action
# Save mid
# left =  mid + 1

# Updated State
# left = 4
# right = 6
# answer = 3

# Iteration 2
# Current State 
# left = 4
# right = 6
# answer = 3

# mid = (left+right)//2
# mid = (4+6)//2
# mid = 5
# numbers[mid] = 6

# Question
# numbers[mid] == target
# 6 == 4
# False

# numbers[mid] < target
# 6 < 4
# False

# right = mid - 1

# Updated State
# left = 4
# right = 5
# answer = 3

# Iteration 3
# Current State
# left = 4
# right = 5
# answer = 3

# mid = (left+right)//2
# mid = (4+5)//2
# mid = 4
# numbers[mid] = 4

# Question
# numbers[mid] == target
# 4 == 4
# True

# Action
# Save mid
# left = mid + 1

# Updated State
# left = 5
# right = 5
# answer = 4

# Iteration 4
# Current State
# left = 5
# right = 5
# answer = 4

# mid = (left+right)//2
# mid = (5+5)//2
# mid = 5
# numbers[mid] = 6

# Question 
# numbers[mid] == target
# 6 == 4
# False

# numbers[mid] < target
# 6 < 4
# False

# Action
# right = mid - 1

# Updated State
# left = 5
# right = 4
# answer = 4

# Iteration 5
# Current State
# left = 5
# right = 4
# answer = 4

# Question 
# left <= right
# 5 <= 4
# False

# Action
# Return answer

# numbers = [5, 7, 7, 8, 8, 10]
# target = 8


def first_occurrence(numbers, target):
    left = 0
    right = len(numbers) - 1
    answer = -1

    while left <= right:
        mid = (left+right)//2
        if numbers[mid] == target:
            answer = mid
            right = mid - 1
        elif numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    # print(answer)
    return answer

# first_occurrence([5, 7, 7, 8, 8, 10], 8)

def last_occurrence(nums, target):
    left = 0
    right = len(nums) - 1
    answer = -1
    
    while left <= right:
        mid = (left+right)//2
        if nums[mid] == target:
            answer = mid
            left = mid + 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return answer

# last_occurrence([5, 7, 7, 8, 8, 10], 8)


def search_range(numbers, target):
    first = first_occurrence(numbers, target)
    last = last_occurrence(numbers, target)
    
    return [first, last]

print(search_range([5, 7, 7, 8, 8, 10], 8))

numbers = [1, 3, 3, 3, 5, 7]
target = 3

left = 0
right = len(numbers) - 1
answer = -1

while left <= right:

    mid = (left + right) // 2

    if numbers[mid] == target:
        answer = mid
        right = mid - 1

    elif numbers[mid] < target:
        left = mid + 1

    else:
        right = mid - 1

print(answer)

# Problem 1 - First Occurrence 

# The first occurrence index would be 1. We don't stop when we find 2 because there is a chance of a previous occurrence of the target element. Hence we don't stop when we find 2.. Similarly the requirement for the question is last occurrence of the index

# Problem 2 - Last Occurrence 

# The last occurrence index is 3. We don't stop when we find 2 because there is a chance of a next occurrence of the target element. Hence we don't stop when we find 2. Also the question specifically asks to find the last occurrence index.

# Problem 3 - 
#Initial State

# left = 0

# right = 5

# answer = -1

# Iteration 1

# Current State

# left = 0

# right = 5

# answer = -1

# mid = 2

# numbers[mid] = 3

# Question 1

# 3 == 3

# True

# Action

# Save mid

# right = mid - 1

# Updated State

# left = 0

# right = 4

# answer = 2

# Iteration 2

# Current State

# left = 0

# right = 4

# answer = 2

# mid = 2

# numbers[mid] = 3

# Question

# 3 == 3

# True

# Action

# save mid

# right = mid - 1

# Updated State

# left = 0

# right = 1

# answer = 2

# Iteration 3

# Current State

# left = 0

# right = 1

# answer = 2

# mid = 0

# numbers[mid] = 1

# Question

# 1 == 3

# False

# 1 < 3

# True

# Action

# left = mid + 1

# Updated State

# left = 1

# right = 1

# answer = 2

# Iteration 4

# Current State

# left = 1

# right = 1

# answer = 2

# mid = 1

# numbers[mid] = 3

# Question

# 3 == 3

# True

# Action

# Save mid

# right = mid - 1

# Updated State

# left = 1

# right = 0

# answer = 1

# Iteration 5

# Current State

# left = 1

# right = 0

# answer = 1

# Question

# 1 <= 0

# False

# Action

# return answer

# Problem 4 - Pattern Recognition

# A - Exact Binary Search

# B - First-Occurrence Binary Search

# C - Last-Boundary Binary Search 

# D - Combined First + Last Binary Search

# E - Linear Search 

# Problem 5 - Most Important 
# A allows us to immediately return because it only asks for the target rather than asking if we specifically have to return anything either at the start or ending index. Whereas B specifically asks us to find the first 4 i.e. first occurrence of the element 4. 
#Initial State
# left = 0
# right = 5
# answer = -1

# Iteration 1
# Current State
# left = 0
# right = 5
# answer = -1

# mid = 2
# numbers[mid] = 3

# Question 1
# 3 == 3
# True

# Action
# Save mid
# right = mid - 1

# Updated State
# left = 0
# right = 4
# answer = 2

# Iteration 2
# Current State
# left = 0
# right = 4
# answer = 2

# mid = 2
# numbers[mid] = 3

# Question
# 3 == 3
# True

# Action
# save mid
# right = mid - 1

# Updated State
# left = 0
# right = 1
# answer = 2

# Iteration 3
# Current State
# left = 0
# right = 1
# answer = 2

# mid = 0
# numbers[mid] = 1

# Question
# 1 == 3
# False

# 1 < 3
# True

# Action
# left = mid + 1

# Updated State
# left = 1
# right = 1
# answer = 2

# Iteration 4
# Current State
# left = 1
# right = 1
# answer = 2

# mid = 1
# numbers[mid] = 3

# Question
# 3 == 3
# True

# Action
# Save mid
# right = mid - 1

# Updated State
# left = 1
# right = 0
# answer = 1

# Iteration 5
# Current State
# left = 1
# right = 0
# answer = 1

# Question
# 1 <= 0
# False

# Action
# return answer