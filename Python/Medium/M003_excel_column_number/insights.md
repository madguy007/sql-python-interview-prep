# Insight

Excel column titles follow a **base-26 number system using letters instead of digits**.

A → 1  
B → 2  
...  
Z → 26

To compute the column number, we process each character from left to right.

At every step we shift the previous value by multiplying with **26** and add the value of the current letter.

Formula:

num = num * 26 + value_of_letter

Letter value can be calculated using:

ord(ch) - ord('A') + 1

Example:

AB

Step 1  
num = 0 * 26 + 1 = 1

Step 2  
num = 1 * 26 + 2 = 28

Result = 28