# Insights

1. **Using a Function**
Creating the function `word_dict()` avoids writing the same logic twice for both strings.  
This keeps the code cleaner and reduces duplication.

2. **Main Idea**
The approach checks whether both strings follow the same **frequency pattern** of characters.

Example  
egg → e(1), g(2) → [1,2]  
add → a(1), d(2) → [1,2]

Since the patterns match, the strings are considered isomorphic in this approach.

3. **Steps**
- Count occurrences of each character using a dictionary.
- Convert counts to a list.
- Compare both lists.
- If equal → print `True`, otherwise `False`.