def largest_prime_factor(n):
    d = 2
    largest = None

    while d*d <= n:
        while n%d == 0:
            largest = d
            n = n // d
        d += 1

    if n > 1:
        largest = n

    return largest

print(largest_prime_factor(600851475143))