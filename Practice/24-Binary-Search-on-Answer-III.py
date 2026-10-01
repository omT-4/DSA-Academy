# ============================================
# Lesson 24 Practice
# Binary Search on the Answer
# LeetCode 1011
# ============================================


# --------------------------------------------
# Part 1 — Recognize the Pattern
# --------------------------------------------

# Q1:
# What exactly are we searching for?
#
# Your Answer:
#


# Q2:
# Why is this a Binary Search on the Answer problem?
#
# Your Answer:
#


# Q3:
# If a capacity works, what happens to greater capacities?
#
# Your Answer:
#


# --------------------------------------------
# Part 2 — Search Boundaries
# --------------------------------------------

weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
days = 5

# Q4:
# What should left be?
#
# Your Answer:
#


# Q5:
# What should right be?
#
# Your Answer:
#


# Q6:
# Explain why left and right have those values.
#
# Your Answer:
#


# --------------------------------------------
# Part 3 — Feasibility Function
# --------------------------------------------

# Complete this function yourself.

# def can_ship(weights, days, capacity):

    # What should this start at?
    # weight_loaded = _____

    # What should this start at?
    # days_used = _____

    # for weight in weights:

        # Complete the condition.
        # if ______________________________:

            # Move to the next day.
            # days_used = __________________

            # Start the new day with the current package.
            # weight_loaded = _______________

        # else:

            # Add the package to the current day's load.
            # weight_loaded = _______________

    # Does this capacity work?
    # return ______________________________


# --------------------------------------------
# Part 4 — Binary Search
# --------------------------------------------

# def shipWithinDays(weights, days):

    # Search boundaries
    # left = __________________
    # right = _________________

    # while __________________:

        # mid = ______________________________

        # if can_ship(weights, days, mid):

            # right = __________________

        # else:

            # left = __________________
    # return __________________


# --------------------------------------------
# Part 5 — Manual Trace
# --------------------------------------------

# weights = [1,2,3,4,5,6,7,8,9,10]
# days = 5

# Initial:
# left =
# right =

# Iteration 1:
# mid =
# Does it work?
# New left =
# New right =

# Iteration 2:
# mid =
# Does it work?
# New left =
# New right =

# Iteration 3:
# mid =
# Does it work?
# New left =
# New right =

# Continue until:
# left == right


# --------------------------------------------
# Part 6 — Active Recall
# --------------------------------------------

# Q1:
# What are we binary searching?
#
# Answer:
#


# Q2:
# Why is left = max(weights)?
#
# Answer:
#


# Q3:
# Why is right = sum(weights)?
#
# Answer:
#


# Q4:
# What does can_ship() check?
#
# Answer:
#


# Q5:
# What does weight_loaded represent?
#
# Answer:
#


# Q6:
# Why do we use days_used = 1?
#
# Answer:
#


# Q7:
# Why do we use:
# weight_loaded + weight > capacity?
#
# Answer:
#


# Q8:
# Why do we use:
# right = mid
# when mid works?
#
# Answer:
#


# Q9:
# Why do we use:
# left = mid + 1
# when mid doesn't work?
#
# Answer:
#


# Q10:
# Why do we use while left < right?
#
# Answer:
#


# Q11:
# What does left == right mean?
#
# Answer:
#


# Q12:
# What is the time complexity?
#
# Answer:
#


# Q13:
# Why is the time complexity O(n log M)?
#
# Answer:
#


# Q14:
# What is the space complexity?
#
# Answer:
#


# Q15:
# Explain the difference between:
#
# Koko's feasibility check
#
# and
#
# Shipping's feasibility check.
#
# Answer:
#


# --------------------------------------------
# Part 7 — Coding Challenge
# --------------------------------------------

# Try solving LeetCode 1011 completely
# without looking at your notes.
#
# Target:
#
# def shipWithinDays(weights, days):
#     ...
#
# Then test:
#
# weights = [1,2,3,4,5,6,7,8,9,10]
# days = 5
#
# Expected Answer:
# 15