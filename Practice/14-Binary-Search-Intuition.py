# Practice problems: problem 1
# Write a program to search for:
# target = 70
# in:
# numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# Requirements:
# Use left
# Use right
# Use while
# Calculate mid
# Return/print the index when found
# Handle the case where the target isn't found

def binary_search(numbers, target):
    left = 0
    right = len(numbers) - 1
    while left <= right:
        mid = (left + right) // 2
        if numbers[mid] == target:
            print(f"Target found at index {mid}")
            return mid
        elif numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
binary_search([10, 20, 30, 40, 50, 60, 70, 80, 90], 70)

# Problem 2 — Target Not Found
# Search for:
# target = 25
# in:
# numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# Write the Binary Search code.
# Expected behavior:
# Target Not Found
def binary_search(numbers, target):
    left = 0
    right = len(numbers) - 1
    while left <= right:
        mid = (left + right) // 2
        if numbers[mid] == target:
            print(f"Target found at index {mid}")
            return mid
        elif numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    print("Target Not Found")
    # return -1
binary_search([10, 20, 30, 40, 50, 60, 70, 80, 90], 25)

# Problem 3 — Dry Run
# Without running the code:
numbers = [5, 10, 15, 20, 25, 30, 35]
target = 30
left = 0
right = len(numbers) - 1
while left <= right:
    mid = (left + right) // 2
    if numbers[mid] == target:
        print("Found")
        break
    elif numbers[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
# Perform the complete dry run using our academy format.
# Track:
# Current State
# left
# right
# mid
# Middle Value
# Question
# Action
# Updated State
# Continue until the target is found.

# Iteration 1 
# Current State
# left = 0
# right = 6
# Find Middle
# mod = (0+6)//2
# mid = 3
# Therefore 
# numbers[mid] = 20
# Question 1
# 20 == 30
# False
# 20 < 30
# True
# Action 
# Target is greater than the middle 
# Search RIGHT
# Eliminate LEFT
# Update
# left = mid + 1
# left = 3 + 1
# left =  4
# updated state
# left = 4
# right = 6
# Search Space
# 25, 30, 35

# Iteration 2
# Current State
# left = 4
# right = 6
# FInd Middle
# mid = (4+6)//2
# mid = 5
# Therefore 
# numbers[mid] = 30
# Question 1
# 30 == 30
# True
# Action
# Print Found
# End loop
# Code executed successfully

# Problem 4 — Most Important
# Explain in your own words:
# Why do we use mid + 1 when searching right and mid - 1 when searching left instead of simply using mid?
# Think carefully about what happened to the middle element after we compared it.

# Because everytime when the target is greater than the middle element the left side of the array is eliminated and when the target is smaller than the left element the right side of the array is eliminated. In other words the search space is shortened and due to this the mid is added or subtracted from based on the situation because if we don't do that then the code will always use a value that is not included in the shortened search space. Making the comparisons not accurate enough. As the principle says always use a value from the input rather than inventing here. The same rule applies here think of the shortened search space of the new input according to the particular iteration and use that middle element. 

# Pattern Transfer
# Scenario A
# You have an unsorted array and need to find a target.
# Which search algorithm would you choose and why?
# I would use linear search as it follows a sequential order and better suits the requirements as binary search only works on sorted data. 

# Scenario B
# You have a sorted array containing 1 million elements and need to repeatedly search for targets.
# Which search algorithm would you choose and why?
# For this siutation I would use binary search as it works perfectly with sorted data and reduces the need for extra work. It is an optimal choice for the problem here and it better suits the requirements.

# Scenario C ⭐
# You are searching for a word in a physical dictionary.
# Which algorithmic idea does this resemble?
# Explain the connection.
# In a dictionary words are arranged in an alphabetical order. Its like a sorted data structure but with alphabets. Ss this follows the algorithmic idea of binary search as the data is sorted. Binary search only works on sorted data and the words in the dictionary are sorted so that's the main connection between the algorithm and the physical dictionary

# Scenario D ⭐
# Suppose you have:
# [10, 20, 30, 40, 50, 60, 70]
# and target:
# 65
# You perform Binary Search.
# Eventually the search space becomes:
# [60, 70]
# What happens next?
# Don't write code. Explain the state changes.
# The code returns either nothing or returns -1 based on the code. 
# Here once again the middle element is selected in this case 70 is chosen to be the middle element and on comparison the target is found to be smaller than the middle element leading to the elimination of the right side elements. In this case the only right side element is 70 so it is eliminated.
# Now only 60 remains it again carries out the comparison now with 60 being the middle element. On comparison the target is found to be greater than the middle element so the left side elements are eliminated. For now that would be 60 so after 60 has been eliminated the array is empty and does not perform any more operations.

# Final Concept Question
# This is the most important question of Lesson 14:
# In one sentence, what is the fundamental idea behind Binary Search?
# sorted data traversed optimally 

Binary Search uses the sorted order of data to repeatedly eliminate half of the search space until the target is found or the search space becomes empty.