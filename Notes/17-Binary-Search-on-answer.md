# Lesson 17 — Binary Search on Answer

## 1. Core Idea

Binary Search on Answer searches through a range of possible answers rather than directly searching for an element inside an array.

It works when:

- We can define a search space of possible answers.
- We can test a candidate answer.
- The test produces a `True` or `False` result.
- The condition follows a monotonic pattern.
- The result allows us to eliminate half of the search space.

---

## 2. Fundamental Idea

The fundamental idea behind Binary Search is:

> Use an ordered or monotonic search space to eliminate half of the possibilities at every iteration.

Normal Binary Search applies this idea to a sorted array.

Binary Search on Answer applies the same idea to a range of possible answer values.

Instead of asking:

> Is this the target element?

We ask:

> Does this candidate answer satisfy the required condition?

---

## 3. Monotonic Condition

A condition is monotonic when, once it changes in one direction, it does not switch back.

Example:

```text
F F F F F T T T T

Once the condition becomes True, it remains True.

Another example:

T T T T T F F F F

Once the condition becomes False, it remains False.

This monotonic behavior allows Binary Search to eliminate half of the search space.

4. Search Space

Binary Search on Answer searches possible answer values.

left  = smallest possible answer
right = largest possible answer

The values of left and right depend on the problem.

Example:

left = 1
right = 10

Possible answers:

1 2 3 4 5 6 7 8 9 10

Sometimes the search space must be derived from the problem.

Example: Package Capacity

left = max(weights)
right = sum(weights)
5. Minimum Valid Answer

Use this pattern when the goal is:

Find the smallest value that satisfies a condition.

Monotonic pattern:

F F F F F T T T T
          ↑
      First True

If the condition is True:

Save mid
Search LEFT

If the condition is False:

Search RIGHT

Template:

left = ...
right = ...
answer = -1


while left <= right:
    mid = (left + right) // 2


    if condition(mid):
        answer = mid
        right = mid - 1
    else:
        left = mid + 1


return answer

Master rule:

TRUE  → SAVE + LEFT
FALSE → RIGHT

Example:

Find the minimum x such that x * 6 >= 35.

Condition:

mid * 6 >= 35
6. Maximum Valid Answer

Use this pattern when the goal is:

Find the largest value that satisfies a condition.

Monotonic pattern:

T T T T T F F F F
        ↑
    Last True

If the condition is True:

Save mid
Search RIGHT

If the condition is False:

Search LEFT

Template:

left = ...
right = ...
answer = -1


while left <= right:
    mid = (left + right) // 2


    if condition(mid):
        answer = mid
        left = mid + 1
    else:
        right = mid - 1


return answer

Master rule:

TRUE  → SAVE + RIGHT
FALSE → LEFT

Example:

Find the maximum x such that x * 7 <= 50.

Condition:

mid * 7 <= 50
7. Candidate Answer

In Binary Search on Answer:

mid

represents the current candidate answer being tested.

We do not immediately assume that mid is the final answer.

We ask:

Does this candidate satisfy the condition?

If:

True

then mid is a valid candidate.

If:

False

then mid is an invalid candidate.

Depending on whether we need the minimum or maximum valid answer, we continue searching for a better candidate.

8. Simple Conditions

If the condition is simple, it can be written directly inside the Binary Search.

Example:

def minimum_hours(items_per_hour, target_items):
    left = 1
    right = 10
    answer = -1


    while left <= right:
        mid = (left + right) // 2


        if mid * items_per_hour >= target_items:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1


    return answer

Condition:

mid * items_per_hour >= target_items

This is a Minimum-Valid Binary Search on Answer.

9. Maximum Valid Example
def maximum_hours(items_per_hour, max_items):
    left = 1
    right = 10
    answer = -1


    while left <= right:
        mid = (left + right) // 2


        if mid * items_per_hour <= max_items:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1


    return answer

Condition:

mid * items_per_hour <= max_items

This is a Maximum-Valid Binary Search on Answer.

10. Condition Functions

Sometimes checking whether a candidate is valid is simple.

Example:

mid * 6 >= 35

Sometimes checking whether a candidate works requires multiple operations.

In that case, create a helper function.

Example:

can_process(weights, days, capacity)

The helper function answers:

Can this candidate capacity successfully complete the task?

Binary Search chooses the candidate:

mid

The helper function determines:

True  → candidate works
False → candidate does not work
11. Package Capacity Problem

Given:

weights = [3, 2, 2, 4, 1, 4]
days = 3

Goal:

Find the minimum truck capacity required to ship all packages within the allowed number of days.

Packages must be shipped in order.

12. Package Capacity Search Space
left = max(weights)
right = sum(weights)
Why left = max(weights)?

The truck must at least be able to carry the heaviest package.

If:

weights = [3, 2, 2, 4, 1, 4]

then:

max(weights) = 4

A capacity smaller than 4 can never work because the package weighing 4 cannot fit.

Therefore:

left = 4
Why right = sum(weights)?

If the truck capacity equals the total weight:

3 + 2 + 2 + 4 + 1 + 4 = 16

then all packages can be carried in one day.

Therefore:

right = 16

The search space is:

4 to 16
13. can_process() Logic

The helper function checks whether a given capacity can ship all packages within the allowed number of days.

def can_process(weights, days, capacity):
    current_load = 0
    days_used = 1


    for weight in weights:
        if current_load + weight <= capacity:
            current_load += weight
        else:
            days_used += 1
            current_load = weight


            if days_used > days:
                return False


    return True
14. Understanding can_process()
current_load
current_load = 0

Represents the total weight currently loaded for the current day.

If another package fits:

current_load += weight

If it does not fit:

days_used += 1
current_load = weight

This means a new day starts and the current package becomes the first package for that day.

days_used
days_used = 1

Represents how many days have been used.

Whenever the current package does not fit in the remaining capacity:

days_used += 1

If:

days_used > days

the capacity is invalid.

Return:

False

If all packages are processed within the allowed number of days:

return True
15. Complete Package Capacity Solution
def can_process(weights, days, capacity):
    current_load = 0
    days_used = 1


    for weight in weights:
        if current_load + weight <= capacity:
            current_load += weight
        else:
            days_used += 1
            current_load = weight


            if days_used > days:
                return False


    return True




def minimum_capacity(weights, days):
    left = max(weights)
    right = sum(weights)
    answer = -1


    while left <= right:
        mid = (left + right) // 2


        if can_process(weights, days, mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1


    return answer




print(minimum_capacity([3, 2, 2, 4, 1, 4], 3))

Output:

6
16. How Binary Search and can_process() Work Together

The flow is:

minimum_capacity()
        ↓
Choose mid
        ↓
mid = candidate capacity
        ↓
can_process(weights, days, mid)
        ↓
Does this capacity work?
        ↓
TRUE / FALSE
        ↓
Binary Search chooses direction

For this problem, we need the minimum valid capacity:

TRUE  → SAVE + LEFT
FALSE → RIGHT
17. Connection to Other Binary Search Patterns
Exact Binary Search

Goal:

Find an exact target.

target found → return immediately
First Occurrence

Goal:

Find the first occurrence of a target.

target found
→ save mid
→ search LEFT
Last Occurrence

Goal:

Find the last occurrence of a target.

target found
→ save mid
→ search RIGHT
Binary Search on Answer

Goal:

Find the first or last value that satisfies a condition.

Minimum valid:

TRUE → SAVE + LEFT
FALSE → RIGHT

Maximum valid:

TRUE → SAVE + RIGHT
FALSE → LEFT
18. Pattern Recognition
Sorted array + exact target
→ Exact Binary Search
Sorted array + duplicates + first occurrence
→ First-Occurrence Binary Search
Sorted array + duplicates + last occurrence
→ Last-Occurrence Binary Search
Unsorted array + find target
→ Linear Search
Possible answers + minimum value satisfying a condition
→ Minimum-Valid Binary Search on Answer
Possible answers + maximum value satisfying a condition
→ Maximum-Valid Binary Search on Answer
19. Decision Process

When you see a problem, ask:

1. Am I searching inside an existing array?


YES
→ Is the array sorted?


    YES
    → Exact / First / Last Binary Search


    NO
    → Usually Linear Search

If you are not searching directly for an element:

2. Am I searching for a possible answer value?

Then ask:

3. Can I test whether a candidate answer works?

Then:

4. Is the result monotonic?

If yes:

→ Binary Search on Answer may be applicable.

Finally:

5. Do I need the minimum valid answer?
or
6. Do I need the maximum valid answer?
20. Master Rules
Minimum Valid
F F F F T T T T


TRUE  → SAVE + LEFT
FALSE → RIGHT

Goal:

Find the first TRUE.
Maximum Valid
T T T T F F F F


TRUE  → SAVE + RIGHT
FALSE → LEFT

Goal:

Find the last TRUE.
21. Final Definition

Binary Search on Answer works when we can define a search space of possible answers and test a candidate answer using a monotonic True/False condition, allowing us to eliminate half of the search space at each iteration.

22. Fundamental Takeaway

Binary Search is not only about:

Finding a target inside a sorted array.

The deeper idea is:

Use an ordered or monotonic search space and a condition to determine which half of the possibilities can be safely eliminated.

Binary Search on Answer applies this same principle to possible answer values instead of array elements.



This version includes the **complete Lesson 17 concept, simple examples, both templates, the package problem, `can_process()`, search-space reasoning, pattern recognition, decision process, and the fundamental/deeper takeaway**.


Your commit message can remain:


```text
Complete Lesson 17 - Binary Search on Answer