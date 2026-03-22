1. Step-by-step Logic (Approach 1):
   - First, group all employees by their email using a dictionary.
   - Each email maps to a list of employees having that email.
   - Then, check which emails have more than one employee (duplicates).
   - For each duplicate group, find the employee with the maximum employee_id using max().
   - Collect those employees as the final result.

2. Why this works:
   - Grouping ensures we isolate duplicate emails.
   - Using max() directly gives the required employee efficiently.
   - This mimics SQL's GROUP BY + HAVING + MAX() logic.

3. Step-by-step Logic (Approach 2):
   - Sort employees by email and descending employee_id.
   - This ensures highest employee_id appears first within each email group.
   - Traverse the list and identify groups of same email.
   - If group size > 1, take the first element (max employee_id).

4. Time and Space Complexity:
   - Approach 1:
     Time Complexity: O(n)
     Space Complexity: O(n)
   - Approach 2:
     Time Complexity: O(n log n) (due to sorting)
     Space Complexity: O(1) extra (ignoring output)

5. Key Python Concepts Used:
   - Dictionaries for grouping (similar to SQL GROUP BY)
   - Lists to store grouped records
   - max() with key function
   - Sorting with lambda
   - While loops for grouping logic