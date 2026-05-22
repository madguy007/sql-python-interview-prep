- Base conversion works using:
  quotient = num // base
  remainder = num % base

- remainder gives current digit
- quotient moves to next higher digit

Example:
49 ÷ 13
quotient = 3
remainder = 10 → A

Result:
3A

==================================================
How Recursion Helped
==================================================

Main recursion idea:
- Higher place values must appear BEFORE lower place values

Example:
49
→ quotient = 3
→ remainder = A

We first recursively solve:
base_13(3)

Then append:
A

So recursion naturally builds digits from left to right.

Flow:
base_13(49)
→ base_13(3) + 'A'
→ '3' + 'A'
→ "3A"

Why recursion fits perfectly:
- Each recursive call reduces number size
- Digits get built in correct order automatically

==================================================
How Sign Was Handled
==================================================

Instead of handling negative logic everywhere:
- We stored sign separately as a simple string

Example:
sign = '-'

Then converted number to positive:
num = abs(num)

Finally:
return sign + result

Why elegant:
- Keeps recursion logic clean
- Conversion logic works only on positive numbers
- Sign added once at final output

==================================================
Important Base Conversion Logic
==================================================

Special mapping:
10 → A
11 → B
12 → C

Handled using dictionary:
dic = {
    10:'A',
    11:'B',
    12:'C'
}

==================================================
Key Python Concepts
==================================================

- Recursion
- Base conversion
- Modulus operator
- Integer division
- Dictionary mapping
- String concatenation
- Ternary operator

==================================================
Interview Pattern
==================================================

Repeated division problems
→ Usually recursion friendly

Need digits from left to right
→ Solve quotient first recursively

==================================================
Memory Rule
==================================================

Base conversion:
remainder → current digit
quotient → recursive next step

Recursion builds:
Most significant digit → least significant digit