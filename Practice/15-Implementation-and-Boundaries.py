# Problem 1
# Write a Binary Search function for:
# numbers = [5, 10, 15, 20, 25, 30, 35]
# target = 25
# It should return the index.
# Expected:
# 4
def binary_search(numbers, target):
    left = 0
    right = len(numbers)-1

    while left <= right:
        mid = (left+right)//2

        if numbers[mid] == target:
            print(f"{mid}")
            return mid
        elif numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    print("Element Not Found")

binary_search([5, 10, 15, 20, 25, 30, 35], 25)

# Problem 2
# Write a Binary Search function for:
# numbers = [5, 10, 15, 20, 25, 30, 35]
# target = 100
# Expected:
# -1
def binary_search(numbers, target):
    left = 0
    right = len(numbers)-1
    while left <= right:
        mid = (left+right)//2
        if numbers[mid] == target:
            print(f"{mid}")
            return mid
        elif numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    print(-1)
binary_search([5, 10, 15, 20, 25, 30, 35], 100)

# Problem 3 — Edge Case
# What happens here?
# numbers = []
# target = 10
# Without running the code, tell me:
# left = 0
# right = -1
# while condition = False 0 > -1
# result = Nothing shows up on the console 

# Problem 4 — Complexity
# Suppose an array contains:
# 1,000,000 elements
# Approximately how many times can Binary Search divide the search space by 2 before reaching around one element?
# Don't calculate using code.
# Think:
# 2^? ≈ 1,000,000
# You don't need the exact answer; an approximate answer is enough.
# 20

# Problem 5 — Interview Thinking
# Explain in your own words:
# Why does Binary Search require sorted data while Linear Search does not?
# Don't simply say:
# "Binary Search needs sorted data."
# Explain what information sorting gives Binary Search that allows it to eliminate half the search space.
# Once you complete these, we'll review them and then move to your first LeetCode problem.
# Binary search works on the basis of sorted data by eliminating half of the data based on the condition. Sorting provides information that allows binary search to make less comparisons increasing speed and optimizes the working capacity. Sorting oorganizes the data in ascending order this helps binary search to make comparisons on the basis of the middle element. If the target element is less than the middle element eliminate right half of the data structure because binary search now knows that the data on the right side is greater than the target element and no longer serves any purpose. Same goes when the target element is greater than the middle element. 

numbers = [2, 4, 6, 8, 10, 12, 14, 16]
left = 0
right = len(numbers) - 1
answer = -1

# Iteration 1
# Current State
# left = 0
# right = 7
# answer = -1

# mid = (left+right)//2
# mid = 3
# numbers[mid] = 8

# Question 
#  8 > 7
# True

# Action 
# record Candidate
# Search LEFT
# Eliminate RIGHT half

# New search space
# [2, 4, 6]

# Updated state
# left = 0
# right = 2
# answer = 8

# Iteration 2
# Current State
# left = 0
# right = 2
# answer = 8

# mid = (left+right)//2
# mid = 1
# numbers[mid] = 4

# Question 
#  4 > 7
# False

# Action 
# record Candidate
# Search RIGHT
# Eliminate LEFT half

# New search space
# [6]

# Updated state
# left = 2
# right = 2
# answer = 8

# Iteration 3
# Current State
# left = 2
# right = 2
# answer = 8

# mid = (left+right)//2
# mid = 2
# numbers[mid] = 6

# Question 
#  6 > 7
# False

# Action 
# record Candidate
# Search RIGHT
# Eliminate LEFT half

# New search space
# []

# Updated state
# left = 3
# right = 2
# answer = 8

# Iteration 4
# Current State
# # left = 3
# right = 2
# answer = 8

# left <= right
# False
# return answer  

# Boundary binary search pattern 
# Practice problems: problem 1
# Write the function yourself.
# Don't look back at the exact code above while writing it.
# Use:
# def first_greater(numbers, target):
#     your code
# For:
# numbers = [2, 4, 6, 8, 10, 12, 14, 16]
# target = 7
# Expected:
# 8
# Your function should:
# Initialize left
# Initialize right
# Initialize answer
# Use while left <= right
# Calculate mid
# Check whether numbers[mid] > target
# If true → save candidate and search left
# If false → search right
# Return answer

def first_greater(numbers, target):
    left = 0
    right = len(numbers) - 1
    answer = -1
    while left <= right:
        mid = (left+right)//2
        if numbers[mid] > 7:
            answer = numbers[mid]
            right = mid - 1
        else:
            left =  mid + 1
    print(answer)
    return answer
first_greater([2, 4, 6, 8, 10, 12, 14, 16], 7)

# Problem 2 — No Valid Element
# Now consider:
# numbers = [2, 4, 6, 8]
# target = 10
# We're looking for:
# First number greater than 10.
# There isn't one.
# What should your function return?
# Think about why we initialized:
# answer = -1
def first_number_greaterthan10(numbers, target):
    left = 0
    right = len(numbers)-1
    answer = -1
    while left<= right:
        mid = (left+right)//2
        if numbers[mid] > 10:
            answer = numbers[mid]
            right = mid - 1
        else:
            left = mid + 1
    print(answer)
    return answer
first_number_greaterthan10([2, 4, 6, 8], 10)

# Problem 3 — First >= Target
# Now we're slightly changing the condition.
# Given:
# numbers = [1, 3, 5, 7, 9, 11]
# target = 6
# Find:
# The first number greater than or equal to 6.
# Expected:
# 7
# The only conceptual change is:
# > target
# becomes:
# >= target
# Everything else follows the same boundary-search pattern.

def first_greaterthan_orequalto_6(numbers, target):
    left = 0
    right = len(numbers) - 1
    answer = -1
    while left <=right:
        mid = (left+right)//2
        if numbers[mid] >= 6:
            answer = numbers[mid]
            right = mid - 1
        else:
            left = mid + 1
    print(answer)
    return answer

first_greaterthan_orequalto_6([1, 3, 5, 7, 9, 11] , 6)

# Problem 4 — Pattern Recognition
# Identify the appropriate approach:
# A
# [10, 20, 30, 40, 50]
# Find 40.
# B
# [10, 20, 30, 40, 50]
# Find the first element greater than 25.
# C
# [50, 10, 30, 20, 40]
# Find 30.
# D
# [1, 2, 4, 8, 16, 32]
# Find the first element greater than or equal to 7.
# For each, tell me whether you'd use:
# Linear Search
# Exact Binary Search
# Boundary Binary Search
# and why.

# For A I would use linear seach because the size of the data is less and we only need to find the target. Although We can also use exact binary search because the data is sorted and is a more optimal choice. But in terms of code complexity linear search is much easier to code than exact binary search. My final answer would be exact binary search since the data is sorted it is the most optimal choice

# For B I would use boundary binary search because the requirements are not to find a target but to find the first element greater than 25 and boundary binary search meets the requirements

# For C Here, I would go with linear search because the data is unsorted. And linear search is the optimal choice for unsorted data rather than exact/boundary binary search

# For D I will choose boundary binary search because the algorithm better fits the requirements 

# Problem 5 — Interview Question
# Explain this in your own words:
# Why can't we immediately return when we find a valid candidate in Boundary Binary Search?
# Use this example:
# [2, 4, 6, 8, 10, 12, 14]
# Find the first number greater than 5.
# Suppose Binary Search encounters 10.
# Why can't we simply say:
# return 10
# ?

# Because there is always a possibility to find other element that is greater than 5. This is the reason why we cannot return a valid candidate in boundary binary search when we encounter one
