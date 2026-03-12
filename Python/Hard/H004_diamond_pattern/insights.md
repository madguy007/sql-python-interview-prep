Key Observation About Pattern Problems

When a pattern has an increasing upper half and a decreasing lower half,
the internal printing logic usually remains exactly the same.

Only the range of the outer loop changes.

Template:

for i in range(1, n+1):
    pattern_logic(i)

for i in range(n-1, 0, -1):
    pattern_logic(i)

Important detail:
We start the second loop from (n-1) so the middle row does not print twice.



Another Insight

Many pattern problems do not require complex position tracking
variables like:

l, r, gap

Instead we can construct rows using simple string operations.


Spaces can be created using:

" " * k


Numbers can be created using:

"".join(str(i) for i in range(...))


Then combine them:

spaces + numbers + spaces


Practical Thinking Rule

Break every row into three parts:

left spaces + pattern content + right spaces


For this problem:

spaces = n - row
numbers = 2*row - 1


So each row becomes:

spaces + numbers + spaces


This simple mental model works for most pyramid,
diamond and centered pattern questions.