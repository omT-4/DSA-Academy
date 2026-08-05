# Practice problems: Problem 1
# Reverse the array:
numbers = [10, 20, 30, 40]
# using the Two Pointers approach.
left_pointer = 0
right_pointer = len(numbers)-1

while left_pointer <  right_pointer:
    temp = numbers[left_pointer]
    numbers[left_pointer] = numbers[right_pointer]
    numbers[right_pointer] = temp

    left_pointer+=1
    right_pointer-=1

print(numbers)

# Problem 2
# Reverse:
numbers = [7, 3, 9, 2, 8, 1]
left_pointer = 0
right_pointer = len(numbers)-1

while left_pointer <  right_pointer:
    temp = numbers[left_pointer]
    numbers[left_pointer] = numbers[right_pointer]
    numbers[right_pointer] = temp

    left_pointer+=1
    right_pointer-=1

print(numbers)

# Problem 3 ⭐ (Dry Run)
# Without running the code:
numbers = [2, 4, 6, 8]
left = 0
right = len(numbers) - 1
while left < right:
    temp = numbers[left]
    numbers[left] = numbers[right]
    numbers[right] = temp
    left += 1
    right -= 1
print(numbers)
# Write the complete dry run.

# Iteration 1
# 0 < 3
# True
# swap 2 <--> 8
# Increment left by 1
# Current state of left = 1
# Decrement right by 1
# Current state of right = 2

# Iteration 2
# 1 < 2
# True
# Swap 4 <--> 6
# Increment left by 1
# Current state of left = 2
# Decrement right by 1
# Current state of right = 1

# Iteration 3
# 2 < 1
# False
# print array
# [8, 6, 4, 2]

# Problem 4 ⭐⭐ (Most Important)
# In your own words, explain:
# Why do the left and right pointers stop when left == right instead of continuing?

# They stop because the condition on which they were performing operations turned from True to False. And when the condition is not satisfied the loop breaks. The condition was is left less than right. So when left == right is does not satisfies the given condition resulting in loop termination 