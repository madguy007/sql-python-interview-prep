Core Idea

The problem requires building the target array step-by-step by inserting numbers at specific positions.

For each index i:
nums[i] → value to insert  
index[i] → position where it should be inserted in the target array.

We read both arrays from left to right and keep inserting values into the target list.


Why insert() is needed

Initially I tried using something like:

target[i] = nums[i]

But that performs replacement, not insertion.

Replacement means the value already at that index gets overwritten.

However, in this problem we must add the value at that position and shift the existing elements to the right.


Example

Before operation

[0,1,2]

Insert 3 at index 2

After operation

[0,1,3,2]

The value 2 moves one position to the right.  
Nothing gets overwritten.

That behavior is exactly what Python's insert() method does.


How insert() works

Syntax

list.insert(index, value)

Example

lst = [0,1,2]

lst.insert(1,4)

Result

[0,4,1,2]


Step-by-step example

nums  
[0,1,2,3,4]

index  
[0,1,2,2,1]

Process

Insert 0 at index 0 → [0]

Insert 1 at index 1 → [0,1]

Insert 2 at index 2 → [0,1,2]

Insert 3 at index 2 → [0,1,3,2]

Insert 4 at index 1 → [0,4,1,3,2]


Time Complexity

O(n²)

Each insert operation may shift elements in the list, and we perform it n times.