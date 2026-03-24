1. Brute Force Logic:
- Try all possible triplets using 3 loops
- Check if sum is zero
- Sort triplet to handle duplicates
- Use list or set to remove duplicates

Why it works:
- Covers all combinations

Time Complexity:
- O(n^3)

Space Complexity:
- O(n) for storing results


2. Set-Based Optimization:
- Same brute force logic
- Use set(tuple(...)) to remove duplicates

Key concept:
- Lists are not hashable → convert to tuple
- Sets automatically remove duplicates

Time Complexity:
- O(n^3)
Space Complexity:
- O(n)


3. Two Pointer Optimization (Most Important):

Step-by-step:
1. Sort the array
2. Fix one element (i)
3. Use two pointers:
   - j (left)
   - k (right)
4. Calculate sum:
   - If sum < 0 → move j forward
   - If sum > 0 → move k backward
   - If sum == 0 → store result and move both

Why sorting helps:
- Enables two-pointer technique
- Helps skip duplicates easily

Duplicate handling:
- Skip same values of i
- Skip repeated values of j and k after finding a triplet

Time Complexity:
- O(n^2)

Space Complexity:
- O(1) (excluding output)


Key Python Concepts Used:
- Sorting (nums.sort())
- Two pointers technique
- Sets and tuples for deduplication
- Nested loops
- List operations

Important Interview Insight:
- Brute force is acceptable for understanding
- Optimal solution must be O(n^2)
- Handling duplicates is the tricky part