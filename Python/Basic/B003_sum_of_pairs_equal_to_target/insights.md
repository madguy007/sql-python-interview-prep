# Insight

The most confusing line in the solution was:

pairs.add(tuple(sorted((nums[i], nums[j]))))

Understanding this step clarified several Python concepts.

## Step 1: Creating a tuple

(nums[i], nums[j])

This creates a tuple containing two numbers.

Example:

nums[i] = 4  
nums[j] = 3  

(nums[i], nums[j]) → (4,3)

This is not one element.  
It is a **two-element tuple**.

---

## Step 2: Why sorted(nums[i], nums[j]) does not work

The sorted() function expects **one iterable argument**.

Valid:

sorted([4,3])  
sorted((4,3))

Invalid:

sorted(4,3)

Because Python interprets it as two separate arguments instead of one iterable.

Correct usage:

sorted((nums[i], nums[j]))

Output:

[3,4]

---

## Step 3: Why tuple() is used

sorted() returns a **list**.

Example:

sorted((4,3)) → [3,4]

But we are storing pairs inside a **set**, and sets require **hashable objects**.

Lists are not hashable, but tuples are.

So we convert the list to a tuple:

tuple(sorted((nums[i], nums[j])))

Result:

(3,4)

---

## Step 4: Why sorting is important

Without sorting:

(3,4) and (4,3)

would be treated as two different pairs.

Sorting ensures both become:

(3,4)

This guarantees that the set stores **only unique pairs**.