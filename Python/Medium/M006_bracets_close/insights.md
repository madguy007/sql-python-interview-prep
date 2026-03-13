1. Core idea: Stack
Balanced parentheses problems are usually solved using a stack.

A stack follows LIFO (Last In First Out).

Whenever we see an opening bracket "(", we push it into the stack.  
Whenever we see a closing bracket ")", we remove (pop) the last opening bracket.


2. Logic of the algorithm

Step 1: Traverse the string character by character.

Step 2:
If the character is "("  
→ push it into the stack.

Step 3:
If the character is ")"  
→ check if the stack is empty.

If the stack is empty  
→ it means ")" appeared before "(", which makes the string invalid.

If the stack is not empty  
→ pop the top element (match the pair).


3. Final condition

After processing the entire string:

If the stack is empty  
→ all parentheses were matched → balanced.

If the stack still has elements  
→ some "(" were not closed → not balanced.


4. Example walkthrough

Input:
"(())()"

Process:

( → push → stack = [(]  
( → push → stack = [(,(]  
) → pop → stack = [(]  
) → pop → stack = []  
( → push → stack = [(]  
) → pop → stack = []

Stack becomes empty → Balanced → True