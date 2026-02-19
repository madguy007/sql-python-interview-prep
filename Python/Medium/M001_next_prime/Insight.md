Pattern: Linear search + primality check

Core Idea:
To find the next prime after n, do not try to predict primes.
Instead, keep moving forward and stop at the first number that satisfies the prime condition.

Prime Logic:
A number is prime if it has no divisors other than 1 and itself.

Optimization:
We only check divisibility up to √num.

Reason:
Factors always occur in pairs (a × b = n).
Once we pass √n, we are just repeating the same factor pairs.
So if no divisor exists before √n → number must be prime.

Edge Handling:
Numbers < 2 are not prime.
For num = 2, loop runs zero times → automatically prime.

Algorithm Thinking:
1. Start from n + 1
2. Check if number is prime
3. If not → increment
4. Stop at first valid number

Key Learning:
Never try to mathematically jump to next valid answer.
When problem asks "first number satisfying a condition"
→ always use incremental search (while loop).
