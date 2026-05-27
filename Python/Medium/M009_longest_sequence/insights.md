- The main idea:
  First sort the array so consecutive numbers become neighbors.

Example:
Original:
[100, 4, 200, 1, 3, 2]

After sorting:
[1, 2, 3, 4, 100, 200]

Now consecutive sequence becomes easy to detect.

==================================================
Core Sequence Logic
==================================================

Check:
new_nums[i] + 1 == new_nums[i+1]

Meaning:
- next number is exactly one greater
- sequence continues

Example:
1 → 2
2 → 3
3 → 4

count keeps increasing.

==================================================
Most Important Concept:
Tracking Maximum Subsequence
==================================================

This is the important interview pattern:

We use TWO variables:

1. count
- current running sequence length

2. longest
- best sequence found so far

==================================================
Why longest Variable Is Powerful
==================================================

While traversing:
- current sequence can grow
- but later sequence may become even larger

So:
we continuously save the maximum.

Example:

Sequence 1:
[1,2]
count = 2

Sequence breaks.

Store:
longest = max(2, longest)

Later:

Sequence 2:
[10,11,12,13]
count = 4

Again:
longest = max(4, 2)

Final:
4

==================================================
Mental Model
==================================================

count:
"Current streak"

longest:
"Best streak ever seen"

Very common interview strategy.

==================================================
Why We Reset count
==================================================

When sequence breaks:

Example:
4 → 100

Not consecutive.

So:
- old sequence ended
- start fresh sequence

Thus:
count = 1

==================================================
Duplicate Handling
==================================================

If:
new_nums[i] == new_nums[i+1]

We skip duplicates.

Because:
duplicates should not break sequence
and should not increase count.

==================================================
Important Final Update
==================================================

After loop:
longest = max(longest, count)

Needed because:
largest sequence may end at final element.

Without this,
last sequence might never be stored.

==================================================
Key Interview Pattern
==================================================

Whenever problem asks:
- longest streak
- maximum subarray
- longest chain
- best sequence

Think:
- current tracker variable
- global maximum variable

This pattern appears everywhere.

==================================================
Time Complexity
==================================================

Sorting:
O(n log n)

Traversal:
O(n)

Total:
O(n log n)

==================================================
Pattern Type
==================================================

Sorting + Consecutive Sequence Tracking