Idea Behind the Pattern

The pattern size is determined by:

2*num - 1

If num = 5

Size becomes

9 × 9


User Solution Logic

The pattern is built row by row.

1. Start with a full row of the largest number.

Example

555555555

2. For each next row:

- Increase the number of characters kept from the start.
- Decrease the middle section.
- Keep the ending part same.

So each row becomes:

start + middle + end

Example transformation

555555555
544444445
543333345
543222345
543212345


Upper and Lower Parts

The pattern has two halves.

Upper half:
- middle length decreases
- count increases

Lower half:
- middle length increases
- count decreases


Mathematical Solution Logic

Instead of modifying strings repeatedly, we can calculate the value of each cell directly.

For each position (i, j) we compute its distance from the nearest border.

distance = min(i, j, n-1-i, n-1-j)

Then the value becomes:

num - distance

Example (center of 9×9 pattern)

distance = 4  
value = 5 - 4 = 1

So the center becomes 1.


Why the Mathematical Approach is Better

- No string slicing
- No tracking of pattern updates
- No extra variables like count and t
- Works directly using index math
- Easier to generalize for larger patterns


Time Complexity

Both approaches print n² cells.

Time Complexity

O(n²)