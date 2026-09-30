# Lesson 23 - Binary Search on the Answer

## Overview

In the previous lessons, we used Binary Search to search through an existing data structure.

In this lesson, we learn a different application of Binary Search:

> Instead of searching for an existing value, we search through a range of possible answers.

This pattern is called:

**Binary Search on the Answer**

We will learn this pattern using:

**LeetCode 875 - Koko Eating Bananas**

---

# 1. Problem Understanding

Koko has several piles of bananas.

Example:

piles = [3, 6, 7, 11]

She has:

h = 8 hours

Koko chooses an eating speed `k`.

If:

k = 4

Then:

3 bananas  -> 1 hour
6 bananas  -> 2 hours
7 bananas  -> 2 hours
11 bananas -> 3 hours

Total:

1 + 2 + 2 + 3 = 8 hours

Therefore, speed 4 works.

The goal is:

> Find the minimum eating speed that allows Koko to finish all bananas within `h` hours.

---

# 2. What Are We Searching?

This is the biggest difference from our previous Binary Search problems.

We are NOT searching through:

[3, 6, 7, 11]

Instead, we are searching through possible speed values:

1, 2, 3, 4, 5, 6, 7, ... 11

For example:

1  2  3  4  5  6  7  8  9  10  11
X  X  X  ✓  ✓  ✓  ✓  ✓  ✓  ✓   ✓
         ^
    minimum valid speed

This is suitable for Binary Search because the answers follow a monotonic pattern.

---

# 3. Monotonic Property

The important property is:

> If a particular speed works, every greater speed will also work.

For example:

If speed 4 works:

4 -> works
5 -> works
6 -> works
7 -> works
...

But if speed 4 does NOT work:

1 -> does not work
2 -> does not work
3 -> does not work
4 -> does not work

Therefore, the possible answers look like:

INVALID INVALID INVALID VALID VALID VALID VALID

This allows us to eliminate half of the possible answers using Binary Search.

---

# 4. Search Boundaries

We start with:

left = 1
right = max(piles)

For:

piles = [3, 6, 7, 11]

we get:

left = 1
right = 11

## Why is left = 1?

Speed 0 means Koko eats zero bananas per hour.

She would never finish.

Therefore, the smallest possible positive speed is:

1

Important:

`left = 1` does NOT mean speed 1 is guaranteed to work.

It only means 1 is the smallest possible speed we need to consider.

---

# 5. Why Is max(piles) the Upper Boundary?

Suppose:

piles = [3, 6, 7, 11]

The largest pile is 11.

If:

k = 11

then:

3  -> 1 hour
6  -> 1 hour
7  -> 1 hour
11 -> 1 hour

So every pile can be completed in at most one hour.

Therefore, `max(piles)` is a safe upper boundary.

In general:

left = 1
right = max(piles)

---

# 6. Checking Whether a Speed Works

Binary Search gives us a possible speed `k`.

We then need to answer:

> Can Koko finish all the bananas within `h` hours at speed `k`?

We create a helper function:

```python
def can_finish(piles, h, k):
    ...
Its job is simply to return:
True  -> speed works
False -> speed does not work
7. Calculating Hours for One Pile
Suppose:
pile = 11
k = 4
Normal division:
11 / 4 = 2.75
But Koko cannot finish the pile in 2.75 hours.
After 2 hours:
4 + 4 = 8 bananas
There are still:
11 - 8 = 3 bananas
remaining.
Therefore, she needs a third hour.
So:
ceil(11 / 4) = 3 hours
We need to round the division UP.
8. Ceiling Division
For positive integers:
ceil(a / b) = (a + b - 1) // b
Therefore:
(pile + k - 1) // k
calculates the number of whole hours required for one pile.
Example:
(11 + 4 - 1) // 4
= 14 // 4
= 3
Therefore:
hours_for_pile = (pile + k - 1) // k
9. Why Do We Need Ceiling Division?
Whenever we divide a quantity into fixed-size groups, we need to ask:
If there is a remainder, do I need one additional complete unit?

If the answer is YES, we need ceiling division.
Examples:
10 items
3 items per box
10 / 3 = 3.33
We cannot use 3 boxes.
We need:
4 boxes
Similarly:
11 bananas
4 bananas/hour
11 / 4 = 2.75
We need:
3 hours
So this pattern appears in problems involving:
- bananas -> hours
- items -> boxes
- people -> buses
- work -> batches
- files -> storage blocks
10. Calculating Total Hours
We need the total hours required for ALL piles.
We start with:
hours = 0
Then loop through every pile:
for pile in piles:
For each pile:
hours += (pile + k - 1) // k
This means:
Calculate the hours required for the current pile and add them to the running total.

Example:
piles = [3, 6, 7, 11]
k = 4
3  -> 1 hour
6  -> 2 hours
7  -> 2 hours
11 -> 3 hours
Total:
hours = 1 + 2 + 2 + 3
hours = 8
11. Checking the Time Limit
We have:
hours = total hours required
h = maximum hours available
The speed is valid if:
hours <= h
Why?
Because Koko is allowed to finish:
- exactly at the deadline
- before the deadline
Examples:
8 <= 8 -> True
7 <= 8 -> True
9 <= 8 -> False
Therefore:
if hours <= h:
    return True
else:
    return False
The shorter version is:
return hours <= h
12. Binary Search on the Answer
Now we have everything needed for Binary Search.
Initial boundaries:
left = 1
right = max(piles)
Loop:
while left < right:
Calculate:
mid = (left + right) // 2
Then check:
if can_finish(piles, h, mid):
13. If mid Works
Suppose:
can_finish(piles, h, mid) == True
This means:
Speed mid is fast enough.

But we want the MINIMUM valid speed.
Therefore, there may be a smaller valid speed.
So we search the left side:
right = mid
Important:
We use:
right = mid
NOT:
right = mid - 1
because mid itself may be the minimum valid answer.
14. If mid Does Not Work
Suppose:
can_finish(piles, h, mid) == False
This means:
Speed mid is too slow.

Because of the monotonic property, every speed smaller than mid is also too slow.
Therefore, we can eliminate:
mid and everything to its left.
So:
left = mid + 1
We use mid + 1 instead of mid because mid has already been proven invalid.
15. Complete Binary Search Pattern
                mid
                 |
        ----------|----------
        |                   |
     WORKS              DOESN'T WORK
        |                   |
        v                   v
  mid could be          mid is too slow
   the answer               |
        |                   |
right = mid          left = mid + 1
The goal is always:
Find the first/minimum value that is valid.

16. Why while left < right?
We use:
while left < right:
because we are narrowing the search space until only one possible answer remains.
Eventually:
left == right
At this point, there is only one candidate remaining.
Because of how we updated the boundaries, this remaining candidate is the minimum valid speed.
Therefore:
return left
We could also return:
return right
because when the loop ends:
left == right
Both contain the same value.
17. Complete Solution
class Solution(object):
    def minEatingSpeed(self, piles, h):

        def can_finish(piles, h, k):
            hours = 0

            for pile in piles:
                hours += (pile + k - 1) // k

            return hours <= h

        left = 1
        right = max(piles)

        while left < right:
            mid = (left + right) // 2

            if can_finish(piles, h, mid):
                right = mid
            else:
                left = mid + 1

        return left
18. Example Walkthrough
Given:
piles = [3, 6, 7, 11]
h = 8
Initial:
left = 1
right = 11
Iteration 1
mid = 6
Speed 6 requires:
1 + 1 + 2 + 2 = 6 hours
6 <= 8
Valid.
Therefore:
right = 6
Iteration 2
left = 1
right = 6

mid = 3
Speed 3 requires:
1 + 2 + 3 + 4 = 10 hours
10 > 8
Invalid.
Therefore:
left = 4
Iteration 3
left = 4
right = 6

mid = 5
Speed 5 requires:
1 + 2 + 2 + 3 = 8 hours
Valid.
Therefore:
right = 5
Iteration 4
left = 4
right = 5

mid = 4
Speed 4 requires:
1 + 2 + 2 + 3 = 8 hours
Valid.
Therefore:
right = 4
Now:
left = 4
right = 4
Loop ends.
Answer:
4
19. Complexity
Let:
n = number of piles
M = maximum pile size
Binary Search performs:
O(log M)
iterations.
For every iteration, we loop through all n piles:
O(n)
Therefore:
Time Complexity:
O(n log M)
Space Complexity:
O(1)
20. Key Pattern to Remember
Binary Search on the Answer follows this structure:
1. Define possible answers
        ↓
2. Find minimum and maximum possible answer
        ↓
3. Pick mid
        ↓
4. Check whether mid works
        ↓
     /       \
   YES        NO
    |          |
search       search
left         right
    |          |
right=mid   left=mid+1
        ↓
left == right
        ↓
return answer24