#!/bin/python3

import sys

fib_numbers = [
    {"num": 1, "prev": 0, "next": 2},
    {"num": 2, "prev": 1, "next": 3},
]


def dicotomic_search_max_below(num, fibonacci_numbers):
    left = 0
    right = len(fibonacci_numbers) - 1
    while left < right:
        mid = (left + right) // 2
        if fibonacci_numbers[mid]["num"] < num:
            left = mid + 1
        else:
            right = mid
    return fibonacci_numbers[left - 1]["num"]


sum_fib_numbers = {}
sum_fib_numbers[1] = 0
sum_fib_numbers[2] = 2

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())

    if n <= fib_numbers[-1]["num"]:
        greatest_fib_number = dicotomic_search_max_below(n - 1, fib_numbers)
        print(sum_fib_numbers[greatest_fib_number])
    else:
        while fib_numbers[-1]["num"] < n:
            fib_numbers.append(
                {
                    "num": fib_numbers[-1]["next"],
                    "prev": fib_numbers[-1]["num"],
                    "next": fib_numbers[-1]["num"] + fib_numbers[-1]["next"]
                }
            )

            sum_fib_numbers[fib_numbers[-1]["num"]
                            ] = sum_fib_numbers[fib_numbers[-2]["num"]]
            if fib_numbers[-1]["num"] % 2 == 0:
                sum_fib_numbers[fib_numbers[-1]
                                ["num"]] += fib_numbers[-1]["num"]

        print(sum_fib_numbers[fib_numbers[-2]["num"]])
    # print(fib_numbers)
    # print(sum_fib_numbers)
