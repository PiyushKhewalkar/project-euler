def sum_fibonacci(max_num):
    prev = 1
    curr = 2
    total = 0
    while curr <= max_num:
        prev, curr = curr, prev + curr
        if curr%2 == 0:
            total = total + curr
    return total

print(sum_fibonacci(4000000))