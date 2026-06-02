# Next Prime Number

## Pattern
**Linear Search + Primality Check**

When asked to find the first number greater than `n` that satisfies a condition, start from `n + 1` and keep checking until you find a valid answer.

---

## Prime Number Rule

A number is prime if it has no divisors other than `1` and itself.

```python
for i in range(2, int(num**0.5) + 1):
```

Check divisibility only up to `√num`.

---

## Why √n?

Factors always occur in pairs.

Example: `36`

```text
1 × 36
2 × 18
3 × 12
4 × 9
6 × 6
```

After `6` (which is `√36`), the factor pairs start repeating in reverse.

Therefore, if no divisor exists before or at `√n`, no divisor can exist after it.

---

## Algorithm

1. Start with `n + 1`
2. Check if the number is prime
3. If not prime, increment by 1
4. Repeat until a prime is found
5. Return the prime number

---

## Edge Cases

- Numbers `< 2` are not prime
- `2` is the first prime number

---

## Memory Trick

> To prove a number is prime, check divisors only up to `√n`.
>
> Any factor larger than `√n` must have a matching factor smaller than `√n`.
>
> If the smaller factor does not exist, the larger factor cannot exist either.
