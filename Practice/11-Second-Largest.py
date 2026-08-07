# Practice problems: Problem 1
# Write a program to find the second largest element in:
numbers = [12, 45, 30, 50, 20]
largest = numbers[0]
second_largest = float("-inf")
for num in numbers:
    if num > largest:
        second_largest = largest
        largest =  num

    elif num > second_largest and num != largest:
        second_largest = num
print(second_largest)

# Problem 2
# Find the second largest element in:
numbers = [-5, -10, -2, -20]
largest = numbers[0]
second_largest = float("-inf")
for num in numbers:
    if num > largest:
        second_largest = largest
        largest =  num
    elif num > second_largest and num != largest:
        second_largest = num
print(second_largest)

# Problem 3 ⭐ (Dry Run)
# Without running the code:
numbers = [15, 40, 25]
largest = numbers[0]
second_largest = float("-inf")
for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num
print(second_largest)
# Write the complete dry run using our academy format.

# Iteration 1 
# Current state
# largest = 15
# second_largest = -infinity 
# 15 > 15
# False 
# 15 > -infinty and 15 != 15
# True and False
# False 
# Nothing changes 

# Iteration 2
# Current state 
# largest = 15
# second_largest = -infinity 
# 40 > 15
# True
# second_largest = 15
# largest = 40


# Iteration 3
# Current state
# largest = 40
# second_largest = 15
# 25 > 40
# False
# 25 > 15 and 25 != 40
# True and True
# second_largest = 25

# Final output
# 25

# Problem 4 ⭐⭐ (Most Important)
# Explain in your own words:
# Why does the old largest become the second largest when a new largest element is found?
# As per the conditions used by us the old largest value becomes the second largest value because before finding the new largest value it was the largest value than every other value. 
# In terms of a real-world analogy suppose a teacher is checking question papers of students she/he finds that one student has scored more than 90 marks but he/she has yet to check all the paper so for now the current highest marks are of student 1. After checking all the papers he/she finds out that another student scored more than 95 marks. Now the highest marks title was given to student 2 while the second highest marks title was given to student 1. No further checking was done because student 1 already had 90 marks and was holding the highest makrs title initially. 

# Pattern Transfer
# Scenario A 
# Traversal + one best value 

# Scenario B
# Traversal + two best values (distinct) [multiple patterns combine]

# Scenario C
# Traversal + Accumulation pattern [multiple patterns combine]

# Scenario D
# I would probably extend today's reasoning 
# Because now I have a clear grasp and understanding of the algorithm. Also finding the third largest value follows the same procedure as that of the finding the second largest value 