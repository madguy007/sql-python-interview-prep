# Insights

When counting digits using division (`num = num // 10`), the loop stops only when the number becomes **0**. This works correctly for **positive numbers**.

Example: `123 → 12 → 1 → 0`

But negative numbers behave differently because Python uses **floor division** (`//`), which rounds down toward negative infinity.

Example: `-123 // 10 = -13 → -13 // 10 = -2 → -2 // 10 = -1 → -1 // 10 = -1`

At this point the value keeps repeating `-1` and **never becomes 0**, which causes the loop to run forever (infinite loop).

To prevent this issue we convert the number to a positive value using:

`num = abs(num)`

Example: `abs(-123) = 123 → 123 → 12 → 1 → 0`

Now the number eventually becomes **0**, so the loop stops correctly and digit counting works.

Another edge case is when the number is **0**. Since the loop would not run at all, we return **1 digit** manually.

**Key takeaway:**  
Whenever counting digits using repeated division, convert the number using `abs(num)` so the algorithm works correctly for both **positive and negative integers**.
