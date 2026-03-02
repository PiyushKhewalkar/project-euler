# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6, and 9.
# The sum of these multiples is 23.

# Find the sum of all the natural numbers below 1000 that are multiples of 3 or 5.

# My Solution

num = 1000

var_1 = 3
var_2 = 5

multiples = []

def list_numbers():
    for i in range(num):
        if i%var_1 == 0 or i%var_2 == 0:
            if i != 0:
                multiples.append(i)
    return multiples

def calculate_sum(numbers):
    total = 0
    for number in numbers:
        total = total + number
    print(total)
    return total

calculate_sum(list_numbers())



# Solution given by llm 

num = 1000
total = 0

for i in range(num):
    if i % 3 == 0 or i % 5 == 0:
        total += i

print(total)