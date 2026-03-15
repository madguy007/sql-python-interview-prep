```python
def count_substrings(s):
    # Base case
    if len(s) == 0:
        return 0

    # Count substrings starting from index 0
    count = 0
    for j in range(len(s)):
        if s[0] == s[j]:
            count += 1

    # Recursive call on the remaining string
    return count + count_substrings(s[1:])


s = input().strip()
print(count_substrings(s))
```

---