Roman to Integer

Easy  
+10 APs  
Solved

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol Values:
I = 1  
V = 5  
X = 10  
L = 50  
C = 100  
D = 500  
M = 1000  

For example:

2 is written as II in Roman numeral, just two ones added together.  
12 is written as XII, which is simply X + II.  
27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written from largest to smallest from left to right.  
However, there are cases where subtraction is used.

For example:

4 is written as IV (5 − 1)  
9 is written as IX (10 − 1)

There are six subtraction rules:

I can be placed before V (5) and X (10) to make 4 and 9.  
X can be placed before L (50) and C (100) to make 40 and 90.  
C can be placed before D (500) and M (1000) to make 400 and 900.

Given a Roman numeral string, convert it to an integer.

Example 1

Input  
III

Output  
3

Example 2

Input  
IV

Output  
4

Example 3

Input  
MCMXCIV

Output  
1994