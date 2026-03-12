1. Why recursion is needed here:
The list can contain other lists inside it (nested lists).  
A normal loop cannot directly handle unlimited nesting depth.  
Recursion allows the function to solve the same problem again when it encounters another list.

Example:
[1, 2, [3,4], [5,6]]

The outer list contains numbers and two inner lists.  
When we reach an inner list, we call the same function again to compute its sum.


2. Recursive logic step-by-step:

Step 1: Start iterating through the list.

Step 2: For each element check:
- If the element is a list → call the same function again on that list.
- If the element is a number → add it to total.

Step 3: Each recursive call returns the sum of that inner list.

Step 4: Add that returned value to the current total.

Example flow:

list_sum([1,2,[3,4],[5,6]])

1 → add → total = 1  
2 → add → total = 3  
[3,4] → recursive call → returns 7 → total = 10  
[5,6] → recursive call → returns 11 → total = 21  


3. Key idea of recursion:
The function solves a small part of the problem and delegates the same task to itself for smaller sub-problems (nested lists).  
Finally all results combine to produce the total sum.