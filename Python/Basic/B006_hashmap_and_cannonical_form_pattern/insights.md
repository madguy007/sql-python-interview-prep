- The core idea is to group words that have the same character composition.
- Since anagrams contain the same letters, sorting each word gives a common key.
  Example:
  "eat", "tea", "ate" → sorted → "aet"
- This sorted string acts as a hash key in the dictionary.
- Words with the same sorted key are grouped together.

Important Concept:
- Python strings do NOT have an in-built sorting method.
- So we use:
  sorted(word) → returns a list of characters
  "".join(...) → converts list back to string
- This conversion is necessary because dictionary keys must be hashable (strings, not lists).

Why this works:
- Dictionary provides O(1) average lookup
- Overall complexity:
  Time: O(n * k log k)
  (n = number of words, k = length of each word)

This is a standard HashMap + canonical form pattern used in interviews.