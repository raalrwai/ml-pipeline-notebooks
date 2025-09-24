def prime_factors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2

    divisor = 3
    while divisor * divisor <= n:
        while n % divisor == 0:
            factors.append(divisor)
            n = n // divisor
        divisor += 2

    if n > 1:
        factors.append(n)

    return factors

print(prime_factors(84))
print(prime_factors(5))

