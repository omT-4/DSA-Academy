# Boundary Binary Search — First & Last Occurrence

## Topic

Finding the first occurrence, last occurrence, and complete range of a target in a sorted array containing duplicates.

## Core Idea

Ordinary Binary Search returns immediately when the target is found.

Boundary Binary Search continues searching after finding the target because we need a specific occurrence.

- First Occurrence → continue LEFT
- Last Occurrence → continue RIGHT

---

## First Occurrence

When:

```python
numbers[mid] == target
do:

answer = mid
right = mid - 1

Why?

There may be another occurrence of the target to the LEFT.

Pattern
Target found
→ Save candidate
→ Search LEFT
Last Occurrence

When:

numbers[mid] == target

do:

answer = mid
left = mid + 1

Why?

There may be another occurrence of the target to the RIGHT.

Pattern
Target found
→ Save candidate
→ Search RIGHT
Other Conditions

If:

numbers[mid] < target

search RIGHT:

left = mid + 1

If:

numbers[mid] > target

search LEFT:

right = mid - 1
First Occurrence Implementation
def first_occurrence(numbers, target):
    left = 0
    right = len(numbers) - 1
    answer = -1

    while left <= right:
        mid = (left + right) // 2

        if numbers[mid] == target:
            answer = mid
            right = mid - 1

        elif numbers[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return answer
Last Occurrence Implementation
def last_occurrence(numbers, target):
    left = 0
    right = len(numbers) - 1
    answer = -1

    while left <= right:
        mid = (left + right) // 2

        if numbers[mid] == target:
            answer = mid
            left = mid + 1

        elif numbers[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return answer
Finding the Complete Range

The range can be found by combining the two patterns:

def search_range(numbers, target):
    first = first_occurrence(numbers, target)
    last = last_occurrence(numbers, target)

    return [first, last]

Example:

numbers = [5, 7, 7, 8, 8, 10]
target = 8

first = 3
last = 4

result = [3, 4]
Target Not Found

If the target does not exist:

first = -1
last = -1

Therefore:

[-1, -1]

Example:

numbers = [5, 7, 7, 8, 8, 10]
target = 6

result = [-1, -1]
Single Occurrence

If the target occurs only once:

numbers = [1, 2, 3, 4, 5]
target = 3

Then:

first = 2
last = 2

result = [2, 2]
All Elements Are the Target
numbers = [5, 5, 5, 5, 5]
target = 5

Then:

first = 0
last = 4

result = [0, 4]
Complexity

First Occurrence:

O(log n)

Last Occurrence:

O(log n)

Combined:

O(log n) + O(log n)
= O(log n)

Space Complexity:

O(1)

for the iterative implementation.

Why Do We Save the Candidate?

Finding the target does not necessarily mean we found the required boundary.

For First Occurrence:

Target found
→ Save candidate
→ Search LEFT

For Last Occurrence:

Target found
→ Save candidate
→ Search RIGHT

The candidate is updated if a better boundary is discovered.

Exact vs Boundary Binary Search
Exact Binary Search
Target found
→ Return
First Occurrence
Target found
→ Save
→ Search LEFT
Last Occurrence
Target found
→ Save
→ Search RIGHT
Complete Range
First Occurrence
+
Last Occurrence
↓
[Starting Index, Ending Index]
Pattern Recognition
Problem	Pattern
Sorted + exact target	Exact Binary Search
Sorted + first occurrence	First-Occurrence Binary Search
Sorted + last occurrence	Last-Occurrence Binary Search
Sorted + complete target range	First + Last Binary Search
Unsorted + exact target	Linear Search
Common Mistakes
Returning immediately after finding the target.
Searching the wrong direction after finding the target.
Forgetting to save mid as the candidate.
Saving numbers[mid] instead of mid when the question asks for the index.
Forgetting [-1, -1] when the target does not exist.
Confusing first occurrence with last occurrence.
Using Binary Search on unsorted data.
Interview Tip
Why don't we return immediately when the target is found?

Because finding the target only proves that it is a valid occurrence.

For the first occurrence, there may be another target to the LEFT.

For the last occurrence, there may be another target to the RIGHT.

Therefore, save the candidate and continue searching.

Concept Connection
Ordered Search Space
        ↓
Find Middle
        ↓
Compare
        ↓
Eliminate Impossible Half
        ↓
Smaller Search Space
        ↓
Repeat

For boundaries:

First → Save → Search LEFT
Last  → Save → Search RIGHT

For a range:

First Occurrence
        +
Last Occurrence
        ↓
[Starting Index, Ending Index]
Key Takeaway

Find → Save → Continue searching in the required direction.

First Occurrence → LEFT

Last Occurrence → RIGHT