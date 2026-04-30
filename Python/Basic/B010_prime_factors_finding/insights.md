- The minimum sum of factors is achieved through prime factorization.
- Breaking a number into its smallest prime factors always minimizes total sum.

Example:
12
- 12 + 1 = 13
- 2 + 6 = 8
- 3 + 4 = 7
- 2 + 2 + 3 = 7

So prime factors provide the minimum.

Core Logic:
1. Repeatedly divide by 2
2. Then check odd numbers from 3 to √n
3. If remainder > 2, it is prime

Why sqrt(n):
- Factors always occur in pairs
- Once smaller factor is checked, larger is automatically handled
- This reduces unnecessary checks

Important Concept:
for i in range(3, int(n**0.5) + 1, 2)

Meaning:
- Start from 3
- Go up to square root
- Step by 2 (only odd numbers)

Optimization:
- Even numbers handled separately
- Greatly improves efficiency

Time Complexity:
- O(√n)

Special Cases:
- Prime number:
  13 → [13]
- Composite:
  100 → [2,2,5,5]

Interview Pattern:
- Prime factorization
- Mathematical optimization
- Efficient divisor checking

This is a classic number theory interview problem.