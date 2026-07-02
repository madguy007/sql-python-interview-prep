- This is a classic matrix pattern-recognition problem.
- Main goal:
  Understand how movement works inside matrix.

==================================================
How To Think In Matrix Questions
==================================================

Instead of thinking:
- "How do I build diagonals?"

Think:
- "What relationship connects diagonal cells?"

This is the important interview mindset.

==================================================
Diagonal Movement Observation
==================================================

For top-left → bottom-right movement:

From:
(0,0) → (1,1)

row +1
col +1

Again:
(1,1) → (2,2)

row +1
col +1

Meaning:
- diagonal movement changes both row and column together

==================================================
Core Realization
==================================================

If current cell belongs to same diagonal,
then previous diagonal cell is:

(i-1, j-1)

So:
matrix[i][j]
must equal:
matrix[i-1][j-1]

This becomes the entire solution.

==================================================
Why This Checks Entire Diagonal
==================================================

Every cell checks:
"Am I equal to my upper-left diagonal neighbor?"

Example:
1 == 1
1 == 1

This creates a chain:
1 == 1 == 1

If every neighboring pair matches,
whole diagonal automatically matches.

==================================================
Why Loops Start From 1
==================================================

We use:
(i-1, j-1)

So first row and first column cannot move upward-left.

Thus:
for i in range(1, rows)
for j in range(1, cols)

==================================================
Most Important Interview Skill
==================================================

Matrix problems are usually:
Movement problems.

Always ask:
- How do I move?
- What is previous position?
- What stays constant?

==================================================
Very Important Matrix Patterns
==================================================

Main diagonal:
i == j

Anti-diagonal:
i + j == n-1

Same diagonal:
i - j constant

Same anti-diagonal:
i + j constant

==================================================
Why Interviewers Love This Question
==================================================

This problem tests:
- matrix traversal
- coordinate thinking
- pattern recognition
- reduction from global property to local check

Instead of checking entire diagonals manually,
we reduce problem into:
small neighbor comparisons.

That is advanced problem-solving thinking.

==================================================
Time Complexity
==================================================

O(m * n)

Efficient because every cell is visited once.

==================================================
Interview Pattern Type
==================================================

Matrix Traversal + Coordinate Pattern Recognition