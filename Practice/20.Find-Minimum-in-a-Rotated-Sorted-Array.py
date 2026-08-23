def find_min(numbers):
    left = 0
    right = len(numbers) - 1

    while left < right:
        mid = (left + right) // 2

        if numbers[mid] > numbers[right]:
            left = mid + 1
        else:
            right = mid

    return numbers[left]

print(find_min([4, 5, 6, 7, 0, 1, 2]))  # Expected: 0

print(find_min([3, 4, 5, 1, 2]))        # Expected: 1

print(find_min([5, 1, 2, 3, 4]))        # Expected: 1

print(find_min([2, 3, 4, 5, 1]))        # Expected: 1

print(find_min([1, 2, 3, 4, 5]))        # Expected: 1

print(find_min([1]))                    # Expected: 1