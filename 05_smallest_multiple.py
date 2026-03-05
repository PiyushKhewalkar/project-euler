def get_prime_factors(n):
    factors = {}
    divisor = 2

    while n > 1:
        count = 0

        while n % divisor == 0:
            count += 1
            n = n // divisor

        if count > 0:
            factors[divisor] = count

        divisor += 1

    return factors


def smallest_multiple(low, high):

    highest_powers = {}

    for i in range(low, high + 1):

        factors = get_prime_factors(i)

        for prime in factors:

            if prime not in highest_powers or factors[prime] > highest_powers[prime]:
                highest_powers[prime] = factors[prime]

    result = 1

    for prime in highest_powers:
        result *= prime ** highest_powers[prime]

    return result


print(smallest_multiple(1,20))