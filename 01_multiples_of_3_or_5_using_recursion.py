# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6, and 9.
# The sum of these multiples is 23.

# Find the sum of all the natural numbers below 1000 that are multiples of 3 or 5.

# My Solution


# num = 1000

# def calculate_sum(n):

#     # base case
#     if n == 0:
#         return 0
    
#     if n % 3 == 0 or n % 5 == 0:
#         return n + calculate_sum(n - 1)
#     else:
#         return calculate_sum(n - 1)

# print(calculate_sum(1000))

# the above solution throws stack error since it exceeds to recursion limit

# def calculate_sum(n):

#     # base case
#     sum_1 = 0
#     sum_2 = 0
#     if (n == 0):
#         return 0
    
#     # divide n into 2 parts

#     n1 = n / 2
#     n2 = n #this would recount n1 actually

#     if n1 % 3 == 0 or n1 % 5 == 0:
#         sum_1 = n1 + calculate_sum(n1 - 1)
#     if n2 % 3 == 0 or n2 % 5 == 0:
#         sum_2 = n2 + calculate_sum(n2 - 1)
    
#     total = sum_1 + sum_2
#     return total

# print(calculate_sum(1000))





# get the start and end

# base case if range size if less than 500. don't split.

# split in half (start to end1, end1 + 1 to end)

# find sum for the first range

# find sum for the second range

# add both ranges

# return

#  just compute the plain sum between a range

# def calculate(num_1, num_2):
#     total = 0
#     if num_2 - num_1 <= 50:
#         for nums in range (num_1, num_2):
#             total = total + nums
#         return total

#     middle = int((num_1 + num_2) / 2)
    
#     left_sum = calculate(num_1, middle)
#     right_sum = calculate(middle+1, num_2)
#     total_sum = left_sum + right_sum
#     return total_sum

# print(calculate(0, 1000))

# still in progress