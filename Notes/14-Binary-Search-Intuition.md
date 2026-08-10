# Binary Search Intuition

## What is Binary Search?

Binary Search is a searching algorithm that works on **sorted data** by repeatedly checking the middle element and eliminating half of the current search space.

---

## Core Idea

Instead of checking elements one by one like Linear Search:

```text
Check → Check → Check → Check

Binary Search:

Find Middle
    ↓
Compare
    ↓
Eliminate Half
    ↓
Smaller Search Space
    ↓
Repeat
Requirement

Binary Search requires the data to be sorted.

Example:

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]

Because the data is sorted, we can determine which half cannot contain the target.

Search Space

The search space is the portion of the array that can still contain the target.

We represent it using two variables:

left = 0
right = len(numbers) - 1
left → first possible index
right → last possible index
mid → middle index
Finding the Middle
mid = (left + right) // 2

mid gives the index of the middle element in the current search space.

Comparison Rules
Target equals middle
middle == target
        ↓
      Found
Target is greater than middle
middle < target
        ↓
  Search RIGHT
        ↓
left = mid + 1
Target is smaller than middle
middle > target
        ↓
   Search LEFT
        ↓
right = mid - 1
Why mid + 1 and mid - 1?

The middle element has already been checked.

If:

numbers[mid] < target

the middle cannot be the target, so we exclude it:

left = mid + 1

If:

numbers[mid] > target

the middle cannot be the target, so we exclude it:

right = mid - 1
Search Space Example
[10, 20, 30, 40, 50, 60, 70, 80, 90]
                  ↑
                 mid

Target:

70

Since:

50 < 70

search the right side.

New search space:

[60, 70, 80, 90]

The process continues until the target is found or the search space becomes empty.

Complete Algorithm
1. Define the search space.
2. Find the middle element.
3. Compare the middle element with the target.
4. If equal → target found.
5. If middle < target → search right.
6. If middle > target → search left.
7. Repeat while a valid search space exists.
8. If left > right → target not found.
Python Implementation
def binary_search(numbers, target):

    left = 0
    right = len(numbers) - 1

    while left <= right:

        mid = (left + right) // 2

        if numbers[mid] == target:
            return mid

        elif numbers[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1

Example:

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]

result = binary_search(numbers, 70)

print(result)

Output:

6
Found vs Not Found
Target Found
numbers[mid] == target
        ↓
return mid

The returned value is the index of the target.

Target Not Found

If:

left > right

the search space is empty.

Therefore:

return -1

-1 indicates that no valid index was found.

Why Does left > right Mean Not Found?

left represents the beginning of the search space.

right represents the end.

When:

left > right

the boundaries have crossed.

Therefore, no valid index remains between them.

left > right
    ↓
Empty Search Space
    ↓
Target Not Found
Complete Dry Run

Given:

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
target = 25

Initial:

left = 0
right = 8
Iteration 1
mid = (0 + 8) // 2
mid = 4

numbers[mid] = 50

Comparison:

25 < 50

Search left:

right = mid - 1
right = 3

New state:

left = 0
right = 3
Iteration 2
mid = (0 + 3) // 2
mid = 1

numbers[mid] = 20

Comparison:

25 > 20

Search right:

left = mid + 1
left = 2

New state:

left = 2
right = 3
Iteration 3
mid = (2 + 3) // 2
mid = 2

numbers[mid] = 30

Comparison:

25 < 30

Search left:

right = mid - 1
right = 1

New state:

left = 2
right = 1

Now:

left > right

Therefore:

Target Not Found
Time Complexity
O(log n)

Reason:

The search space is approximately halved after every comparison.

Example:

1,000,000
    ↓
500,000
    ↓
250,000
    ↓
125,000
    ↓
...

The number of remaining elements decreases exponentially rather than one element at a time.

Space Complexity
O(1)

The iterative implementation only uses a few variables:

left
right
mid

No additional array is created.

Linear Search vs Binary Search
Feature	Linear Search	Binary Search
Data requirement	Sorted or unsorted	Must be sorted
Approach	Check one by one	Eliminate half
Best Case	O(1)	O(1)
Worst Case	O(n)	O(log n)
Main idea	Sequential traversal	Divide search space
Real-World Analogy

Searching for a word in a physical dictionary resembles Binary Search.

Words arranged alphabetically
        ↓
Open near the middle
        ↓
Compare the word
        ↓
Choose left or right
        ↓
Repeat

The alphabetical ordering allows half of the dictionary to be eliminated after each comparison.

Common Mistakes
Using Binary Search on unsorted data.
Using left = mid instead of left = mid + 1.
Using right = mid instead of right = mid - 1.
Forgetting that mid has already been checked.
Using the wrong comparison direction.
Forgetting the left <= right loop condition.
Forgetting to handle the target-not-found case.
Pattern Recognition
Sorted Data
    ↓
Search Space
    ↓
Find Middle
    ↓
Compare
    ↓
Eliminate Half
    ↓
Smaller Search Space
    ↓
Repeat
    ↓
Found / Not Found
Key Takeaways
Binary Search works on sorted data.
left and right define the current search space.
mid identifies the element to compare.
middle < target → search right.
middle > target → search left.
middle == target → found.
left > right → target not found.
mid is excluded after it has been checked.
Time Complexity: O(log n)
Space Complexity: O(1) for the iterative implementation.