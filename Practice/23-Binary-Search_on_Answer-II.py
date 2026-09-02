# ============================================================
# LESSON 23 - BINARY SEARCH ON THE ANSWER
# LeetCode 875 - Koko Eating Bananas
# ============================================================


# ------------------------------------------------------------
# PART 1 - Ceiling Division Practice
# ------------------------------------------------------------

# Calculate how many groups are required.

# Example:
# 10 items
# 3 items per group
# Answer = 4


# TODO:
# Write the ceiling division formula here.


# ------------------------------------------------------------
# PART 2 - Feasibility Function
# ------------------------------------------------------------

def can_finish(piles, h, k):
    # TODO:
    # 1. Create a variable to store total hours.
    # 2. Loop through every pile.
    # 3. Calculate hours required for each pile.
    # 4. Add those hours to the total.
    # 5. Return whether total hours <= h.

    pass


# ------------------------------------------------------------
# PART 3 - Binary Search on the Answer
# ------------------------------------------------------------

def minEatingSpeed(piles, h):
    # TODO:
    # Set the search boundaries.

    # left = ?
    # right = ?

    # TODO:
    # Build Binary Search.

    pass


# ------------------------------------------------------------
# PART 4 - Test Cases
# ------------------------------------------------------------

# Expected: 4
print(minEatingSpeed([3, 6, 7, 11], 8))

# Expected: 30
print(minEatingSpeed([30, 11, 23, 4, 20], 5))

# Expected: 23
print(minEatingSpeed([30, 11, 23, 4, 20], 6))


# ------------------------------------------------------------
# PART 5 - Active Recall
# ------------------------------------------------------------

# 1. What exactly are we binary searching?

# 2. Why is max(piles) a safe upper boundary?

# 3. Why do we need ceiling division?

# 4. Explain:
#    (pile + k - 1) // k

# 5. Why is right = mid when mid works?

# 6. Why is left = mid + 1 when mid doesn't work?

# 7. Why do we use while left < right?

# 8. What does left == right mean?

# 9. Why is the complexity O(n log M) rather than O(log M)?