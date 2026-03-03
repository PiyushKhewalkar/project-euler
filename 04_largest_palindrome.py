def largest_palindrome(low, high):
    max_palindrome = 0

    for i in range(high, low - 1, -1):
        for j in range(i, low - 1, -1):
            product = i * j

            if product <=max_palindrome:
                break

            if str(product) == str(product)[::-1]:
                max_palindrome = product

    return max_palindrome

print(largest_palindrome(100, 999))