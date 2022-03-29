#!/bin/python3

import sys


def sum_of_multiples_of_below(x, threshold):
    smallest_multiple_of_x = x
    largest_multiple_of_x = x * ((threshold - 1) // x)
    count_multiples_of_x = (threshold - 1) // x
    if count_multiples_of_x % 2 == 0:
        return (count_multiples_of_x * (largest_multiple_of_x + smallest_multiple_of_x)) // 2
    return (count_multiples_of_x - 1) * (largest_multiple_of_x + smallest_multiple_of_x) // 2 + (smallest_multiple_of_x * ((count_multiples_of_x + 1) // 2))


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    sum_of_multiples_of_3_below_n = sum_of_multiples_of_below(3, n)
    sum_of_multiples_of_5_below_n = sum_of_multiples_of_below(5, n)
    sum_of_multiples_of_15_below_n = sum_of_multiples_of_below(15, n)
    print(sum_of_multiples_of_3_below_n + sum_of_multiples_of_5_below_n - sum_of_multiples_of_15_below_n)
