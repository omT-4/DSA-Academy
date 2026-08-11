# Binary Search — Implementation, Complexity & Boundaries

## Topic

Binary Search implementation, complexity, edge cases, and Boundary Binary Search.

## Core Idea

Binary Search uses an ordered search space to repeatedly eliminate approximately half of the remaining possibilities.

Exact Binary Search finds a specific target. Boundary Binary Search finds the first or last position satisfying a condition.

---

## Exact Binary Search

```text
middle == target
→ Found → return middle

middle < target
→ Search RIGHT
→ left = mid + 1

middle > target
→ Search LEFT
→ right = mid - 1

Standard Implementation
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
Search Space
left → beginning of current search space
right → end of current search space
mid → middle of current search space
mid = (left + right) // 2

The search continues while:

left <= right

When:

left > right

the search space is empty.

Why mid + 1 and mid - 1?

The middle element has already been checked.

Therefore:

left = mid + 1

excludes the middle element when searching right.

And:

right = mid - 1

excludes the middle element when searching left.

Complexity
Time Complexity
O(log n)

Reason: The search space is approximately halved after every comparison.

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
↓
1

Approximately:

2^20 ≈ 1,000,000

Therefore:

log₂(1,000,000) ≈ 20
Space Complexity
O(1)

The iterative implementation only uses a few variables:

left
right
mid

No additional array is created.

Edge Cases
Empty Array
numbers = []

Then:

left = 0
right = -1

Since:

0 <= -1

is false, the loop does not execute.

Single Element
numbers = [50]

Then:

left = 0
right = 0

Since:

0 <= 0

is true, the single element is checked normally.

Boundary Binary Search

Boundary Binary Search is used when we need to find the first or last position satisfying a condition.

Example:

Find the first number greater than 7.

[2, 4, 6, 8, 10, 12, 14, 16]

 F  F  F  T   T   T   T   T
          ↑
       First True

The deeper idea is:

Find the boundary where the condition changes from False to True.

Boundary Search Rules
Condition is False
→ Current element is not a valid candidate
→ Search RIGHT
→ left = mid + 1
Condition is True
→ Current element is a valid candidate
→ Save candidate
→ Search LEFT
→ right = mid - 1

The candidate is saved because there may be an earlier valid element.

Why Not Return Immediately?

Suppose:

[2, 4, 6, 8, 10, 12, 14]

Find the first number greater than 5.

If Binary Search encounters:

10 > 5

then 10 is a valid candidate.

However, there may be a smaller valid element to its left:

8 > 5
6 > 5

Therefore:

Save 10
→ Search LEFT
→ Look for an earlier valid candidate

The correct answer is:

6
First Greater Element
def first_greater(numbers, target):
    left = 0
    right = len(numbers) - 1
    answer = -1

    while left <= right:
        mid = (left + right) // 2

        if numbers[mid] > target:
            answer = numbers[mid]
            right = mid - 1

        else:
            left = mid + 1

    return answer
First Greater Than or Equal To

The same Boundary Binary Search pattern can be used to find the first element greater than or equal to a target.

Change:

numbers[mid] > target

to:

numbers[mid] >= target

Example:

[1, 3, 5, 7, 9, 11]

target = 6

 F  F  F  T  T  T
          ↑
          7

Answer:

7
Pattern Recognition
Situation	Pattern
Sorted + exact target	Exact Binary Search
Sorted + first/last valid position	Boundary Binary Search
Unsorted + exact target	Linear Search
Common Mistakes
Using Binary Search on unsorted data.
Using left = mid instead of left = mid + 1.
Using right = mid instead of right = mid - 1.
Forgetting that mid has already been checked.
Returning immediately when a Boundary Search candidate is found.
Hardcoding the target instead of using the function parameter.
Confusing print() with return.
Interview Tips
Why is Binary Search O(log n)?

Because each comparison eliminates approximately half of the remaining search space, so the number of operations grows logarithmically with the input size.

Why does Binary Search require sorted data?

Sorting gives Binary Search an ordering that allows it to determine which half of the search space cannot contain the answer.

Why use mid + 1 and mid - 1?

Because the middle element has already been checked and is known not to be the target.

Why don't we immediately return a valid candidate in Boundary Binary Search?

Because there may be a smaller valid element to its left, so we save the candidate and continue searching for an earlier valid element.

Concept Connection
Ordered Search Space
        ↓
Find Middle
        ↓
Check Condition
        ↓
Eliminate Impossible Half
        ↓
Smaller Search Space
        ↓
Repeat
Exact Binary Search
Valid → Return
Boundary Binary Search
Valid → Save → Continue Searching
Key Takeaways
Binary Search requires an ordered search space.
Exact Binary Search searches for a specific target.
Boundary Binary Search searches for a position satisfying a condition.
left and right define the current search space.
mid identifies the element being evaluated.
left = mid + 1 searches right.
right = mid - 1 searches left.
Exact Search returns when the target is found.
Boundary Search saves a valid candidate and continues searching.
Time Complexity: O(log n).
Space Complexity: O(1) for iterative Binary Search.