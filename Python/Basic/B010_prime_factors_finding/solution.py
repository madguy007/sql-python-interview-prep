def prime_factors(n):
    factors = []
    
    # Check for factor 2
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    
    # Check odd factors from 3 to sqrt(n)
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n // i
    
    # Remaining number is prime
    if n > 2:
        factors.append(n)
    
    return factors


# Test cases
print(sum(prime_factors(12)))    # 7
print(sum(prime_factors(105)))   # 15
print(sum(prime_factors(13)))    # 13
print(sum(prime_factors(100)))   # 14