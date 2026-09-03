# Lesson 24 — Binary Search on the Answer: Shipping Packages

## Problem

**LeetCode 1011 — Capacity To Ship Packages Within D Days**

---

# 1. Problem Understanding

We are given packages with different weights.

Example:

weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

We are also given the number of days available:

days = 5

The packages must be shipped **in the given order**.

We need to find:

> The minimum ship capacity that allows us to ship all packages within the given number of days.

---

# 2. What Are We Searching?

We are NOT searching for a particular package.

We are searching through possible **ship capacities**.

For the example:

weights = [1,2,3,4,5,6,7,8,9,10]

Possible capacities range from:

10 → 55

So our search space is:

10, 11, 12, 13, ..., 55

Each number represents a possible answer.

This is another example of:

> **Binary Search on the Answer**

---

# 3. Why Binary Search Works

The possible capacities have a monotonic pattern.

If a capacity works, every greater capacity will also work.

For example:

10 → ?
11 → ?
12 → ❌
13 → ❌
14 → ❌
15 → ✅
16 → ✅
17 → ✅
...
55 → ✅

The pattern looks like:

INVALID INVALID INVALID VALID VALID VALID

We are looking for:

> The minimum valid capacity.

---

# 4. Search Boundaries

We use:

left = max(weights)

right = sum(weights)

For:

weights = [1,2,3,4,5,6,7,8,9,10]

we get:

left = 10

right = 55

---

# 5. Why Is left = max(weights)?

The largest package weighs 10.

Therefore, the ship must have a capacity of at least 10.

If:

capacity = 9

then the package weighing 10 cannot be shipped.

Therefore:

left = max(weights)

Important:

left does NOT mean that this value is guaranteed to work.

It only means:

> This is the smallest possible capacity that could work.

---

# 6. Why Is right = sum(weights)?

If the ship can carry the weight of every package at once, then all packages can be shipped in one day.

For:

[1,2,3,4,5,6,7,8,9,10]

the total weight is:

55

Therefore:

right = sum(weights)

This is a safe maximum boundary.

---

# 7. Feasibility Check

Now we need to answer:

> Can we ship all packages within the given number of days if the ship has capacity `capacity`?

We create a helper function:

def can_ship(weights, days, capacity):

Its job is:

True → capacity works

False → capacity does not work

---

# 8. How Shipping Works

Suppose:

capacity = 15

weights = [1,2,3,4,5,6,7,8,9,10]

We load packages in order.

Day 1:

1 + 2 + 3 + 4 + 5 = 15

The ship is full.

Day 2:

6 + 7 = 13

We cannot add 8 because:

13 + 8 = 21 > 15

So Day 2 contains:

[6,7]

Day 3:

[8]

Day 4:

[9]

Day 5:

[10]

Total:

5 days

Therefore capacity 15 works if:

days = 5

---

# 9. weight_loaded

We use:

weight_loaded = 0

This keeps track of:

> How much weight is currently loaded onto the ship for the current day.

At the beginning of a new day, the ship is empty.

---

# 10. days_used

We use:

days_used = 1

Why not 0?

Because we are already starting to ship packages on Day 1.

---

# 11. Loop Through the Packages

We use:

for weight in weights:

We process every package in its original order.

We cannot rearrange the packages.

---

# 12. Checking Whether a Package Fits

We use:

if weight_loaded + weight > capacity:

This means:

> If the weight already loaded onto the ship plus the current package exceeds the capacity, the package cannot fit.

Example:

weight_loaded = 13

weight = 8

capacity = 15

13 + 8 = 21

21 > 15

Therefore, the package does not fit.

---

# 13. Starting a New Day

If the package does not fit:

days_used += 1

weight_loaded = weight

Why?

Because:

1. The current day is finished.
2. We move to the next day.
3. The current package must be loaded onto the new day's ship.

We do NOT skip the package.

---

# 14. If the Package Fits

If the package fits:

weight_loaded += weight

This adds the package to the current day's ship.

---

# 15. Complete Feasibility Function

def can_ship(weights, days, capacity):

    weight_loaded = 0
    days_used = 1

    for weight in weights:

        if weight_loaded + weight > capacity:
            days_used += 1
            weight_loaded = weight

        else:
            weight_loaded += weight

    return days_used <= days

---

# 16. Why days_used <= days?

We calculate the number of days actually required.

Then we compare it with the number of days allowed.

Example:

days_used = 4
days = 5

4 <= 5

True

The capacity works.

Example:

days_used = 6
days = 5

6 <= 5

False

The capacity does not work.

---

# 17. Binary Search

Now we search for the minimum valid capacity.

Initial boundaries:

left = max(weights)

right = sum(weights)

Then:

while left < right:

    mid = (left + right) // 2

---

# 18. If mid Works

If:

can_ship(weights, days, mid)

returns True:

The capacity works.

But we are looking for the minimum capacity.

Therefore, we try smaller capacities.

We use:

right = mid

Why not:

right = mid - 1?

Because `mid` itself may be the minimum valid capacity.

---

# 19. If mid Does Not Work

If:

can_ship(weights, days, mid)

returns False:

The capacity is too small.

Because of the monotonic property, every capacity smaller than `mid` will also fail.

Therefore:

left = mid + 1

We use `mid + 1` because `mid` has already been proven invalid.

---

# 20. Why while left < right?

We are not searching for a specific target.

We are narrowing the search space until only one possible answer remains.

Eventually:

left == right

At this point there is only one possible answer remaining.

Therefore:

return left

We could also return right because:

left == right

when the loop ends.

---

# 21. Complete Solution

def shipWithinDays(weights, days):

    def can_ship(weights, days, capacity):

        weight_loaded = 0
        days_used = 1

        for weight in weights:

            if weight_loaded + weight > capacity:
                days_used += 1
                weight_loaded = weight

            else:
                weight_loaded += weight

        return days_used <= days

    left = max(weights)
    right = sum(weights)

    while left < right:

        mid = (left + right) // 2

        if can_ship(weights, days, mid):
            right = mid

        else:
            left = mid + 1

    return left

---

# 22. Complete Example

weights = [1,2,3,4,5,6,7,8,9,10]

days = 5

Initial:

left = 10
right = 55

---

## Iteration 1

mid = (10 + 55) // 2

mid = 32

Capacity 32 works.

Therefore:

right = 32

New search space:

10 → 32

---

## Iteration 2

mid = (10 + 32) // 2

mid = 21

Capacity 21 works.

Therefore:

right = 21

New search space:

10 → 21

---

## Iteration 3

mid = (10 + 21) // 2

mid = 15

Capacity 15 works.

Therefore:

right = 15

New search space:

10 → 15

---

## Iteration 4

mid = (10 + 15) // 2

mid = 12

Capacity 12 requires 6 days.

But only 5 days are available.

Therefore:

12 does not work.

So:

left = 12 + 1

left = 13

New search space:

13 → 15

---

## Iteration 5

mid = (13 + 15) // 2

mid = 14

Capacity 14 requires 6 days.

Therefore it does not work.

So:

left = 14 + 1

left = 15

Now:

left = 15
right = 15

The loop stops.

Answer:

15

Therefore:

> The minimum ship capacity is 15.

---

# 23. Lesson 23 vs Lesson 24

Both problems use:

> Binary Search on the Answer

The Binary Search framework is almost identical.

The difference is the **feasibility check**.

---

## Lesson 23 — Koko Eating Bananas

We guess:

> Eating speed

Then calculate:

> Hours required

Conceptually:

speed → calculate hours → check hours <= h

The important calculation is:

(pile + k - 1) // k

This calculates the number of whole hours required for a pile.

We use ceiling division because if there are leftover bananas, Koko needs another complete hour.

Example:

11 bananas

4 bananas per hour

11 / 4 = 2.75

Koko needs 3 hours.

---

## Lesson 24 — Shipping Packages

We guess:

> Ship capacity

Then calculate:

> Days required

Conceptually:

capacity → simulate loading → calculate days → check days_used <= days

We keep adding packages until adding another package would exceed capacity.

If the next package does not fit:

days_used += 1

weight_loaded = weight

Then we continue on the next day.

---

# 24. The Simplest Difference

Imagine two toys.

### Koko 🍌

We give Koko a speed.

She says:

> "How many hours do I need?"

So:

SPEED → HOURS

We mainly use division.

---

### Shipping 🚚

We give the truck a capacity.

The truck says:

> "How many days do I need?"

So:

CAPACITY → DAYS

We keep adding package weights until the truck becomes full.

---

# 25. One-Year-Old Explanation 👶

### Koko

Give her a speed:

4 bananas per hour.

She eats:

🍌🍌🍌🍌

Then:

🍌🍌🍌🍌

Then:

🍌🍌

She counts:

⏰ ⏰ ⏰

So:

> Koko's check = "How many hours?"

---

### Truck

Give the truck a capacity:

15 kg.

Put things inside:

📦 1
📦 2
📦 3
📦 4
📦 5

Truck is full.

Next day:

📦 6
📦 7

Then next day...

So:

> Shipping's check = "How many days?"

---

# 26. What Is Common?

Both problems do:

1. Guess an answer.
2. Check whether the answer works.
3. If it works, try a smaller answer.
4. If it doesn't work, try a larger answer.
5. Continue until one answer remains.

Pattern:

INVALID INVALID INVALID VALID VALID VALID

We want the:

> **First valid answer**

---

# 27. Important Mental Model

Do NOT memorize the feasibility code.

Instead ask:

> "What am I guessing?"

Then:

> "If I guess this value, what do I need to calculate to know whether it works?"

For Koko:

Guess → speed

Calculate → hours

Check → hours <= h

For Shipping:

Guess → capacity

Calculate → days

Check → days_used <= days

This is the most important skill from these two lessons.

---

# 28. Complexity

Let:

n = number of packages

M = size of the numeric capacity search range

Binary Search requires:

O(log M)

iterations.

However, every Binary Search iteration calls:

can_ship()

And `can_ship()` loops through all `n` packages:

O(n)

Therefore:

Time Complexity:

O(n log M)

Why?

Binary Search:

O(log M)

Feasibility check:

O(n)

Together:

O(n log M)

---

## Space Complexity

We only use a few variables:

left
right
mid
weight_loaded
days_used

We do not create another data structure that grows with the input.

Therefore:

Space Complexity:

O(1)

---

# 29. How To Recognize Binary Search on the Answer

Ask these questions:

### Question 1

Am I looking for a minimum or maximum value?

Examples:

- minimum speed
- minimum capacity
- minimum time
- maximum distance

### Question 2

Can I define a range of possible answers?

Example:

10 → 55

### Question 3

Can I check whether one candidate answer works?

Example:

can_ship(...)

### Question 4

Does the result have a monotonic pattern?

Example:

INVALID INVALID INVALID VALID VALID VALID

If the answer to these questions is YES, Binary Search on the Answer may be appropriate.

---

# 30. Key Takeaways

1. Binary Search can search through possible answers, not just array values.

2. `left` and `right` represent the smallest and largest possible answers.

3. The feasibility function checks whether a candidate answer works.

4. If `mid` works and we want the minimum:

right = mid

5. If `mid` doesn't work:

left = mid + 1

6. `while left < right` is used when we want to narrow the search space to one remaining answer.

7. `left == right` means only one candidate remains.

8. The feasibility function is different for every problem.

9. Koko:
   
   speed → hours → check hours <= h

10. Shipping:
   
   capacity → days → check days_used <= days

11. The Binary Search framework remains the same.

12. The important skill is learning how to design the feasibility check.

---

# 31. Active Recall — Lesson 24

### Q1
What exactly are we binary searching in LeetCode 1011?

### Q2
Why is `left = max(weights)`?

### Q3
Why is `right = sum(weights)`?

### Q4
What is the purpose of `can_ship()`?

### Q5
What does `weight_loaded + weight > capacity` mean?

### Q6
If the package does not fit, why do we increase `days_used`?

### Q7
Why do we set `weight_loaded = weight` after starting a new day?

### Q8
Why does `days_used` start at 1?

### Q9
What does `days_used <= days` tell us?

### Q10
Why do we use `right = mid` when `mid` works?

### Q11
Why do we use `left = mid + 1` when `mid` doesn't work?

### Q12
Why do we use `while left < right`?

### Q13
What does `left == right` mean?

### Q14
What is the time complexity and why?

### Q15
What is the space complexity and why?

### Q16
What is the difference between Koko's feasibility check and Shipping's feasibility check?

### Q17
What remains the same between both problems?

### Q18
How can you recognize a Binary Search on the Answer problem?

---

# 32. Final Pattern

Remember:

POSSIBLE ANSWERS

        ↓

     choose mid

        ↓

  "Does mid work?"

      /       \
    YES        NO
     |          |
     ↓          ↓
try smaller   try bigger
     |          |
right = mid   left = mid + 1

        ↓

left == right

        ↓

return answer