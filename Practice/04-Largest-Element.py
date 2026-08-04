# Practice Problems: Problem 1
# Write a program to find the largest element in:
numbers = [5, 10, 15, 20, 25]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num

print(largest)

# Problem 2
# Find the largest element in:
numbers = [-10, -5, -25, -1]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num

print(largest)

# Problem 3
# Without running the code, tell me the output.
numbers = [8, 3, 15, 7]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print(largest)
# Iteration 1
# 8 > 8
# False
# largest = 8

# Iteration 2
# 3 > 8
# False
# largest = 8

# Iteration 3
# 15 > 8
# True
# Update largest
# largest = 15

# Iteration 4
# 7 > 15
# False
# largest = 15

# Final output = 15

# Problem 4 (Interview Thinking ⭐)
# Why is this initialization correct?
# largest = numbers[0]
# instead of
# largest = 0
# Explain the reasoning, not just the answer.

# Because when comparing it is better to choose a value from the input rather than inventing a new value as per the principle. 
# Since when using largest = numbers[0] we are able to compare known values from the array whereas when using largest = 0 we are creating a new value also every positive value is greater than 0 which will result in the largest variable to not be updated it will work only when the array contains negative values 

# We initialize with numbers[0] because it is guaranteed to be a valid element in the array. This makes the algorithm work correctly for positive, negative, mixed, and single-element arrays.