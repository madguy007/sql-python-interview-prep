- This problem uses the Sliding Window technique.
- Instead of recalculating sum for every subarray, we reuse the previous window sum.

How window works:
- Start with first window of size k:
  [4, 2, 1] → sum = 7
- Slide the window by 1 step:
  Remove left element, add next element
  [2, 1, 7] → 7 - 4 + 7 = 10
- Again slide:
  [1, 7, 8] → 10 - 2 + 8 = 16

Key Idea:
- window_sum = previous_sum + incoming_element - outgoing_element
- This avoids recomputing sum → improves efficiency

Why efficient:
- Brute force: O(n * k)
- Sliding window: O(n)

Important Mistake to Avoid:
- Use += and -= correctly
  window_sum += arr[i]
  window_sum -= arr[i-k]
- Writing =+ or =- resets value instead of updating

This pattern is heavily used in subarray problems in interviews.