- This is a classic Sliding Window problem on strings.
- Instead of checking every substring separately, we maintain a running count of vowels.

How window works:
- First window: "abc" → vowels = 1
- Slide:
  Remove left char, add right char
  "bci" → count updates dynamically
- Continue sliding until end

Key Idea:
- When window moves:
  Add effect of new character (s[i])
  Remove effect of old character (s[i-k])
- This keeps computation constant per step

Why efficient:
- Brute force: O(n * k)
- Sliding window: O(n)

Important Concepts:
- Set lookup (s[i] in vowels) is O(1)
- Maintain count instead of recomputing
- Works for any fixed-size substring problems

This pattern generalizes to:
- max sum
- max frequency
- count of valid elements in window