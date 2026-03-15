# Count Substrings Starting and Ending With Same Character

## Problem

We are given a string **S**.
Write a **recursive Python program** to count all **contiguous substrings** that **start and end with the same character**.

A substring must be continuous in the string.

---

## Example

Input

```
abcab
```

All substrings

```
a, ab, abc, abca, abcab
b, bc, bca, bcab
c, ca, cab
a, ab
b
```

Valid substrings (start and end with same character)

```
a
abca
b
bcab
c
a
b
```

Output

```
7
```

---

## Goal

Design a recursive function that:

1. Counts substrings starting from the **current first character**
2. Recursively processes the **remaining string**

---