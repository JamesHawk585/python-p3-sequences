#!/usr/bin/env python3

# Fibonacci sequence
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233,
# 0 + 1 = 1
# 1 + 1 = 2
# 1 + 2 = 3
# 2 + 3 = 5
# 3 + 5 = 8
# 5 + 8 = 13
# 8 + 13 = 21
# 13 + 21 = 34 

# 1. Create list with first two fibonacci numbers
# 2. Extend sum of last two numbers to list
# 3. Repeat step 2 until list has reached the desired length

fibonacci_list = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
print(fibonacci_list(15))

def print_fibonacci(length):
    fibonacci_list = [0, 1]
    if length <= 2:
        return fibonacci_list[:length]
    while len(fibonacci_list) < length:
       next_num = fibonacci_list[-1] + fibonacci_list[-2]
       fibonacci_list.append(next_num)
    return fibonacci_list





