# Lesson 19 - Search in Rotated Sorted Array

## Core Idea

A rotated sorted array is not completely sorted, but at least one half of the current search space is always sorted.

Binary Search can use this property to eliminate half of the search space.

---

## Main Logic

1. Find `mid`.
2. Check if `numbers[mid] == target`.
3. If not, determine which half is sorted.
4. Check whether the target lies inside the sorted half.
5. Search the appropriate half.
6. Return `-1` if the target is not found.

---

## Complete Algorithm

```python
def search(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left <= right:
        mid = (left + right) // 2

        if numbers[mid] == target:
            return mid

        elif numbers[left] <= numbers[mid]:

            if numbers[left] <= target < numbers[mid]:
                right = mid - 1
            else:
                left = mid + 1

        else:

            if numbers[mid] < target <= numbers[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1

Identifying the Sorted Half
Left Half Sorted
numbers[left] <= numbers[mid]
Target inside the left half:
numbers[left] <= target < numbers[mid]
- Inside → right = mid - 1
- Outside → left = mid + 1

Right Half Sorted
If the left half is not sorted, the right half is sorted.
Target inside the right half:
numbers[mid] < target <= numbers[right]
- Inside → left = mid + 1
- Outside → right = mid - 1

Important Rule
This approach works because the array is guaranteed to be a rotated version of a sorted array.
Therefore, during every iteration, at least one half of the current search space is sorted.

Complexity
- Time: O(log n)
- Space: O(1)