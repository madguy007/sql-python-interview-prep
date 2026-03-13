1. Why recursion works well here:
A nested list can contain lists inside lists with unknown depth.

Example:
[1,[2,3],4,[5,[6,7]],8]

Inside this list we again find another list:
[5,[6,7]]

And inside that another list:
[6,7]

Recursion allows the same function to process these inner lists automatically.


2. Recursive logic:

Step 1:
Iterate through each element in the list.

Step 2:
Check the type of the element.

If the element is a list  
→ call the same function again on that list.

If the element is a number  
→ add it to the result list.

Step 3:
Each recursive call processes its own small list and returns numbers to the outer call.

Finally all numbers combine into one flat list.


3. Example execution flow

flatten([1,[2,3],4,[5,[6,7]],8])

1 → append → [1]

[2,3] → recursive call  
    2 → append  
    3 → append  
return [2,3]

result → [1,2,3]

4 → append → [1,2,3,4]

[5,[6,7]] → recursive call  
    5 → append  
    [6,7] → recursive call  
        6 → append  
        7 → append  

final result:
[1,2,3,4,5,6,7,8]


4. Key idea:
Recursion breaks a big nested problem into smaller sublists and solves them using the same function repeatedly.