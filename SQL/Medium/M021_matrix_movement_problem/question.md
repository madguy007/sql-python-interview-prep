Given an m x n matrix, determine whether every diagonal from top-left to bottom-right contains the same value.

Return True if all diagonal stripes are identical, otherwise return False.

Example 1:

Input:
matrix = [
 [42, 7, 13, 99],
 [6, 42, 7, 13],
 [1, 6, 42, 7]
]

Output:
True

Explanation:
Diagonals:
[1]
[6, 6]
[42, 42, 42]
[7, 7, 7]
[13, 13]
[99]

All diagonals contain identical values.

Example 2:

Input:
matrix = [
 [8, 23],
 [69, 1]
]

Output:
False