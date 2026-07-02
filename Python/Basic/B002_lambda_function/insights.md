# Lambda Function Insight (Python)

A **lambda function** is a small anonymous function written in a single line. It is useful when we need a short function for a temporary purpose without defining it using `def`.

Syntax:

lambda arguments : expression

Example:

lambda x: x + 5

This function takes `x` as input and returns `x + 5`.

Lambda functions are often used with functions like `filter()`, `map()`, and `sorted()`.

Example (filter even numbers):

nums = [1,2,3,4,5,6]

even = list(filter(lambda num: num % 2 == 0, nums))

Explanation:

lambda num: num % 2 == 0

For each number in the list:
- If the condition is **True**, the number is kept
- If the condition is **False**, the number is removed

Evaluation:

1 % 2 == 0 → False  
2 % 2 == 0 → True  
3 % 2 == 0 → False  
4 % 2 == 0 → True  

Result:

[2,4,6]

Key Points:
- Lambda functions have **no name**
- They contain **only one expression**
- They are commonly used for **short, simple operations**
