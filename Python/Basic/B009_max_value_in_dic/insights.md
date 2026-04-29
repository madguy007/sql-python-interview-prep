- This problem uses a HashMap (dictionary) to count frequency of each character.
- Each character becomes a key, and its count becomes the value.

Example:
"hello"
{
'h':1,
'e':1,
'l':2,
'o':1
}

Core Counting Logic:
- char_count.get(char, 0)
- If character exists → returns current count
- If not → starts from 0
- Then +1 updates frequency

Important New Concept:
most_occuring_char = max(char_count, key=char_count.get)

How this works:
- By default, max(dictionary) checks only keys alphabetically
- Example:
  max({'a':5, 'z':1}) → 'z'

But:
- key=char_count.get tells max() to compare dictionary values instead of keys

So:
max(char_count, key=char_count.get)

Means:
- For each key, fetch its value
- Return the key with highest value

Example:
char_count = {'h':1, 'e':1, 'l':2, 'o':1}

Internally:
max compares:
h → 1
e → 1
l → 2
o → 1

Result:
'l'

Why powerful:
- Directly finds highest frequency key
- No manual loop required
- Very common in interviews

Time Complexity:
- Counting: O(n)
- max(): O(k)
- Total: O(n)

This is a standard frequency-count + dictionary optimization pattern.