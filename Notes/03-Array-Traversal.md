# Array Traversal

## What is Traversal?

Traversal means visiting every element of a data structure exactly once in a systematic order.

For arrays, traversal means accessing each element from the first index to the last index.

Example:

```
10 → 20 → 30 → 40 → 50
```

The computer visits every element one by one.

---

# Why Do We Need Traversal?

Traversal is required whenever we need to process every element in an array.

Common examples:

- Print all elements
- Find the largest element
- Find the smallest element
- Calculate the sum
- Count even/odd numbers
- Search for an element

Most array algorithms begin with traversal.

---

# Method 1 - Value Traversal

Use this method when you only need the values stored inside the array.

```python
numbers = [10, 20, 30, 40]

for num in numbers:
    print(num)
```

### Explanation

- `num` stores the current element.
- Python automatically moves to the next element after each iteration.
- The same variable (`num`) is updated every iteration.

Output:

```
10
20
30
40
```

---

# Dry Run - Value Traversal

Initial State

```
numbers = [10,20,30,40]

num = ?
```

Iteration 1

```
num = 10

Output

10
```

Iteration 2

```
num = 20

Output

20
```

Iteration 3

```
num = 30

Output

30
```

Iteration 4

```
num = 40

Output

40
```

Loop Ends.

---

# Memory Model

Memory during execution:

```
numbers
↓

[10,20,30,40]

num
↓

10
```

Next iteration:

```
numbers
↓

[10,20,30,40]

num
↓

20
```

Python does **not** create another variable.

It simply updates the existing variable.

---

# Method 2 - Index Traversal

Use this method when you need the index (position) of each element.

```python
numbers = [10,20,30,40]

for i in range(len(numbers)):
    print(i, numbers[i])
```

Output

```
0 10
1 20
2 30
3 40
```

---

# How Index Traversal Works

```
len(numbers)

↓

4

range(4)

↓

0
1
2
3
```

Iteration 1

```
i = 0

numbers[0]

↓

10
```

Iteration 2

```
i = 1

numbers[1]

↓

20
```

The process continues until the last index.

---

# When to Use Each Method

## Use Value Traversal

```python
for num in numbers:
```

Examples:

- Print elements
- Find largest element
- Find smallest element
- Calculate sum
- Count elements

---

## Use Index Traversal

```python
for i in range(len(numbers)):
```

Examples:

- Print index and value
- Modify elements
- Compare neighbouring elements
- Two Sum (Brute Force)
- Access multiple indices

---

# Time Complexity

Traversal visits every element exactly once.

If the array has:

```
5 elements

↓

5 iterations
```

```
100 elements

↓

100 iterations
```

Therefore,

```
Time Complexity = O(n)
```

Reason:

The number of operations grows linearly with the input size.

---

# Space Complexity

Extra variables:

```
num

or

i
```

Python updates the same variable every iteration.

No new variable is created.

Therefore,

```
Space Complexity = O(1)
```

Reason:

Only a fixed amount of additional memory is used.

---

# Common Beginner Mistakes

❌ Confusing index with value.

❌ Thinking Python creates a new loop variable every iteration.

❌ Thinking loops increase Space Complexity.

❌ Using index traversal when only values are needed.

---

# Interview Tip

If an interviewer asks:

> Why do we use `range(len(array))` instead of `for element in array`?

Do not answer:

> Because Python works that way.

Instead answer:

> We use index traversal when the algorithm requires the position of each element, not just the value.

---

# Concept Connection

```
Array
    │
    ▼
Contiguous Memory
    │
    ▼
Random Access
    │
    ▼
Traversal
   / \
  /   \
 ▼     ▼
Value  Index
Traversal Traversal
```

---

# Key Takeaways

- Traversal means visiting every element once.
- Use value traversal when only values are needed.
- Use index traversal when the index is required.
- Traversal takes O(n) time.
- Traversal uses O(1) extra space.
- Python updates the same loop variable during each iteration.