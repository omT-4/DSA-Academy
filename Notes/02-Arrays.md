# Arrays

## What is an Array?

An array is a collection of elements stored in contiguous memory locations and accessed using an index.

---

## Why Do We Use Arrays?

Instead of creating hundreds of separate variables, arrays allow us to store and manage related data together.

Example:

```python
marks = [89, 76, 91, 85]
```

---

## Contiguous Memory

Array elements are stored next to each other in memory.

Example:

```
Address      Value

1000         12
1004         45
1008          8
1012         31
1016         19
```

This allows the computer to calculate the address of any element directly.

---

## Indexing

Arrays start from index **0**.

Example:

```python
numbers = [12, 45, 8, 31, 19]
```

| Index | Value |
|-------:|------:|
| 0 | 12 |
| 1 | 45 |
| 2 | 8 |
| 3 | 31 |
| 4 | 19 |

---

## Why Does Indexing Start at 0?

The first element is **0 positions away** from the base address.

The computer calculates:

```
Address = Base Address + (Index × Size of One Element)
```

Example:

```
Base Address = 1000

numbers[3]

1000 + (3 × 4)

= 1012
```

The computer directly reaches the correct memory location.

---

## Random Access

Arrays provide **Random Access**.

The computer directly calculates the address of an element instead of searching every element.

Time Complexity:

```
O(1)
```

Space Complexity:

```
O(1)
```

---

## Advantages

- Fast random access
- Easy traversal
- Simple to use
- Efficient for storing related data

---

## Disadvantages

- Fixed size in many languages
- Insertion and deletion in the middle are expensive

---

## Interview Tip

If asked why array access is O(1):

Do not say:

> Arrays are fast.

Instead say:

> Arrays are stored in contiguous memory, allowing the computer to calculate the memory address directly using the index instead of searching.

---

## Concept Connection

```
Array
    │
    ▼
Contiguous Memory
    │
    ▼
Address Calculation
    │
    ▼
Random Access
    │
    ▼
O(1) Access Time
```