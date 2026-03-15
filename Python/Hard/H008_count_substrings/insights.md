# Recursion Thinking Process

This problem becomes simple once we break it into **two logical steps**.

---

## Step 1 — Focus on One Starting Index

For string

```
abcab
```

First consider substrings starting at index `0`

```
a
ab
abc
abca
abcab
```

A substring is valid if

```
s[0] == s[j]
```

Matches occur at:

```
j = 0, 3
```

Valid substrings

```
a
abca
```

Count = **2**

---

## Step 2 — Reduce the Problem

After processing index `0`, move to the **next starting index**.

```
abcab
bcab
cab
ab
b
""
```

Each recursive call processes substrings starting at the **new first character**.

---

## Step 3 — Recursive Formula

```
count_substrings(s)
=
(count of substrings starting at s[0])
+
count_substrings(s[1:])
```

---

## Step 4 — Base Case

When the string becomes empty:

```
""
```

there are **no substrings left**, so recursion stops.

```
return 0
```

---

## Step 5 — Recursion Flow Example

```
count_substrings("abcab")

= 2 + count_substrings("bcab")
= 2 + (2 + count_substrings("cab"))
= 2 + 2 + (1 + count_substrings("ab"))
= 2 + 2 + 1 + (1 + count_substrings("b"))
= 2 + 2 + 1 + 1 + (1 + count_substrings(""))
```

Final result

```
7
```

---

## Key Recursion Idea

Every recursion problem should answer three questions:

1. **What is the smaller problem?**

```
s[1:]
```

2. **What work does the current call perform?**

Count matches of

```
s[0] == s[j]
```

3. **How are results combined?**

```
current_count + recursive_result
```

---

## Time Complexity

```
O(n²)
```

Each recursive call scans the remaining string.