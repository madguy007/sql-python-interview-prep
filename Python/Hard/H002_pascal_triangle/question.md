# Pascal Triangle

## Problem

Write a Python program to generate Pascal's Triangle for a given number of rows.

Pascal's Triangle is a triangular array of numbers where:

- The first and last numbers of each row are always **1**.
- Every other number is the **sum of the two numbers directly above it** from the previous row.

## Example

Input

5

```
Output

[
 [1],
 [1, 1],
 [1, 2, 1],
 [1, 3, 3, 1],
 [1, 4, 6, 4, 1]
]
```

## Rule

If the current element is not on the edge:

value = previous_row[j-1] + previous_row[j]
