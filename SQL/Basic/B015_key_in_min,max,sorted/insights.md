- The goal is to find which number has the smallest absolute difference from K.
- For each number:
  abs(k - num)
- Smaller difference means closer number.

Example:
K = 6
5 → |6-5| = 1
9 → |6-9| = 3
3 → |6-3| = 3

Minimum difference = 1
Answer = 5

Core Logic:
- Store:
  number → distance from K
- Then find minimum distance

Important New Concept:
return min(diff, key=diff.get)

How this works:
- Normally min(dictionary) compares keys
- key=diff.get tells min() to compare based on dictionary values

Example:
diff = {
9: 3,
11: 5,
5: 1,
3: 3
}

min(diff, key=diff.get)
→ Returns key with smallest value
→ 5

==================================================
key= Quick Revision
==================================================

Used in:
- min()
- max()
- sorted()
- list.sort()

Purpose:
- Custom comparison rule

Syntax:
min(data, key=function)

Formula:
Original item → key function → comparison value

Example:
min(lst, key=lambda x: abs(x-K))

Meaning:
- Each element is checked based on closeness to K
- Returns original value with minimum transformed result

Common Uses:

Shortest string:
min(words, key=len)

Largest absolute value:
max(nums, key=abs)

Sort by second element:
sorted(lst, key=lambda x: x[1])

Dictionary minimum value:
min(dic, key=dic.get)

Golden Rule:
key = "compare using this logic"

Alternative Simpler Solution:
return min(lst, key=lambda x: abs(x-k))

This avoids extra dictionary creation.

Time Complexity:
- O(n)

Interview Pattern:
- Closest value
- Custom sorting
- key parameter mastery

This is an important Python interview optimization concept.