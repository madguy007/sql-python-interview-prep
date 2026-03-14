### Core Idea

Roman numerals normally follow the rule:

larger value comes before smaller value.

Example  
VI = 5 + 1 = 6

But sometimes a smaller value appears before a larger value, which means subtraction.

Example  
IV = 5 − 1 = 4  
IX = 10 − 1 = 9


### Key Logic Used in the Algorithm

We iterate through the string from left to right.

For each character we compare its value with the next character.

Two cases occur:

**Case 1 — Normal addition**

If the current value is greater than or equal to the next value, we simply add it.

Example

XVI

X (10) ≥ V (5) → add  
V (5) ≥ I (1) → add  
I (1) → add

Result  
10 + 5 + 1 = 16


**Case 2 — Subtraction case**

If the current value is smaller than the next value, it means subtraction is needed.

Example

IV

I (1) < V (5)

So instead of adding 1, we subtract it.


### Why `abs(ans - value)` works

When a subtraction case happens, we remove the smaller value from the total.

Example

IV

Step 1  
ans = 0

Step 2  
I < V → subtraction case

ans = abs(0 − 1) = 1

Step 3  
V → add 5

ans = 4


### Example Walkthrough

Input

MCMXCIV

Values

M = 1000  
C = 100  
M = 1000  
X = 10  
C = 100  
I = 1  
V = 5

Process

M → add → 1000  
C < M → subtract 100  
M → add 1000  
X < C → subtract 10  
C → add 100  
I < V → subtract 1  
V → add 5

Final result

1994


### Time Complexity

O(n)

We scan the string once.


### Space Complexity

O(1)

Only a dictionary and a few variables are used.