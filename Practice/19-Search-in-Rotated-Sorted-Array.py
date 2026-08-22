def search(numbers, target):
    left = 0
    right = len(numbers) - 1
    while left <= right:
        mid = (left + right) // 2
        if numbers[mid] == target:
            return mid
        elif numbers[left] <= numbers[mid]:
            if numbers[left] <= target <  numbers[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if numbers[mid] < target <= numbers[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1

print(search([4, 5, 6, 7, 0, 1, 2], 0))
print(search([4, 5, 6, 7, 0, 1, 2], 6))
print(search([4, 5, 6, 7, 0, 1, 2], 3))
print(search([1], 1))
print(search([1], 0))