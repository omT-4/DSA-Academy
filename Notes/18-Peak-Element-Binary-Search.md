# Lesson 18 — Peak Element Binary Search

## 1. What is a Peak Element?

A peak element is an element that is greater than its neighboring element(s).

Example:

numbers = [1, 3, 5, 4, 2]

Index:      0  1  2  3  4
Numbers:   [1, 3, 5, 4, 2]

5 is a peak because:

5 > 3
5 > 4

A problem may contain multiple peak elements, but if the requirement asks for a peak element, finding one valid peak is enough.

Example:

numbers = [1, 3, 2, 5, 4]

Peak elements:

3
5


---

# 2. Binary Search Without a Completely Sorted Array

Traditional Binary Search usually works on sorted data.

However, Binary Search can also work when the array is not completely sorted if information at the current position allows us to safely eliminate part of the search space.

In the Peak Element pattern, we compare:

numbers[mid]

with:

numbers[mid + 1]

This comparison tells us whether we are moving uphill or downhill.


---

# 3. Going Uphill

If:

numbers[mid] < numbers[mid + 1]

Example:

3 < 5

The array is moving uphill.

Therefore, a peak can be found on the RIGHT side.

Update:

left = mid + 1


Pattern:

numbers[mid] < numbers[mid + 1]

→ Going uphill
→ Search RIGHT
→ left = mid + 1


---

# 4. Going Downhill

If:

numbers[mid] > numbers[mid + 1]

Example:

5 > 4

The array is moving downhill.

A peak can exist at:

- mid itself
- somewhere to the LEFT

Therefore, we search LEFT while keeping mid inside the search space.

Update:

right = mid


We do NOT use:

right = mid - 1

because mid itself may be the peak.


Pattern:

numbers[mid] > numbers[mid + 1]

→ Going downhill
→ Peak can be at mid or LEFT
→ right = mid


---

# 5. Why Use while left < right?

The loop condition is:

while left < right

The search space keeps shrinking until only one possible index remains.

Eventually:

left == right

At this point, the remaining index represents a peak element.

Therefore, we stop the loop and return:

return left


---

# 6. Core Algorithm

def find_peak(numbers):
    left = 0
    right = len(numbers) - 1

    while left < right:
        mid = (left + right) // 2

        if numbers[mid] < numbers[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return left


---

# 7. Step-by-Step Logic

Start:

left = 0
right = len(numbers) - 1

While:

left < right

Calculate:

mid = (left + right) // 2

Compare:

numbers[mid]

with:

numbers[mid + 1]


If:

numbers[mid] < numbers[mid + 1]

Search RIGHT:

left = mid + 1


Otherwise:

Search LEFT including mid:

right = mid


When:

left == right

Return:

left


---

# 8. Example Dry Run

numbers = [1, 2, 4, 6, 5, 3]

Initial:

left = 0
right = 5


Iteration 1:

mid = (0 + 5) // 2
mid = 2

numbers[mid] = 4
numbers[mid + 1] = 6

4 < 6 → True

Action:

left = mid + 1

left = 3


Iteration 2:

left = 3
right = 5

mid = (3 + 5) // 2
mid = 4

numbers[mid] = 5
numbers[mid + 1] = 3

5 < 3 → False

Action:

right = mid

right = 4


Iteration 3:

left = 3
right = 4

mid = (3 + 4) // 2
mid = 3

numbers[mid] = 6
numbers[mid + 1] = 5

6 < 5 → False

Action:

right = mid

right = 3


Final State:

left = 3
right = 3

left == right

Return:

3


numbers[3] = 6

Therefore, the peak index is:

3


---

# 9. Pattern Recognition

Use Peak Element Binary Search when:

- The problem asks to find a peak element.
- The array may not be completely sorted.
- Comparing the current element with a neighboring element helps determine which half can be eliminated.
- We only need to find one valid peak.

Core pattern:

numbers[mid] < numbers[mid + 1]
→ Search RIGHT

numbers[mid] > numbers[mid + 1]
→ Search LEFT including mid


---

# 10. Important Difference from Traditional Binary Search

Traditional Binary Search:

- Usually requires sorted data.
- Compares numbers[mid] with a target.
- Eliminates a side based on whether the target is smaller or larger.

Peak Element Binary Search:

- Does not require the entire array to be sorted.
- Does not search for a specific target.
- Compares numbers[mid] with numbers[mid + 1].
- Eliminates a side based on whether the sequence is moving uphill or downhill.


---

# 11. Fundamental Binary Search Principle

Binary Search is not limited to sorted arrays.

Binary Search can work whenever information obtained at the current position allows us to safely eliminate part of the search space.

For Peak Element Binary Search:

Compare mid with mid + 1
↓
Determine uphill or downhill
↓
Determine which side can still contain a peak
↓
Eliminate the other side
↓
Continue until one index remains


---

# 12. Time and Space Complexity

Time Complexity:

O(log n)

Because the search space is approximately reduced by half during each iteration.

Space Complexity:

O(1)

Because only a constant number of variables are used.


---

# 13. Quick Revision

Peak Element:

An element greater than its neighboring element(s).


Going Uphill:

numbers[mid] < numbers[mid + 1]

→ left = mid + 1


Going Downhill:

numbers[mid] > numbers[mid + 1]

→ right = mid


Loop:

while left < right


Final State:

left == right


Return:

return left


Fundamental Idea:

Binary Search can work even without a completely sorted array if the information at the current position allows us to safely eliminate half of the search space.