This problem is about detecting a pattern across consecutive rows.

At first it may look complex because SQL tables do not naturally allow us to compare a row with its neighboring rows. However, there are two common strategies to solve such problems.

First approach: Self Join

A self join means joining a table with itself. In this solution the Logs table is referenced three times as l1, l2, and l3. Each alias represents a shifted version of the same table.

The conditions

l1.id = l2.id - 1  
l2.id = l3.id - 1

align three consecutive rows together. Conceptually the query creates a sliding window like:

row i   → l1  
row i+1 → l2  
row i+2 → l3  

Once the rows are aligned, we simply check whether all three numbers are equal using

l1.num = l2.num  
l2.num = l3.num

If the condition is true, that number appeared three times consecutively.

Second approach: Window Functions

Modern SQL provides window functions that allow direct access to neighboring rows. The LAG() function retrieves values from previous rows.

LAG(num,1) gives the previous number.  
LAG(num,2) gives the number two rows before.

This creates a temporary view where each row knows the values of the previous two rows. We then check:

num = prev1 AND num = prev2

If this condition holds, the current row completes a sequence of three identical numbers.

Key Takeaway

Many SQL problems that involve patterns across rows can be solved in two ways:
1. Self joins to manually align rows.
2. Window functions to directly access neighboring rows.

Window functions are usually cleaner and more efficient, while self joins help understand the underlying row alignment logic.