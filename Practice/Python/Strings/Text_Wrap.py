# You are given a string S and width w.
# Your task is to wrap the string into a paragraph of width w.

# Function Description
# Complete the wrap function in the editor below.

# wrap has the following parameters:
# string string: a long string
# int max_width: the width to wrap to

# Returns
# string: a single string with newline characters('\n')
# where the breaks should be

# Input Format
# The first line contains a string, string.
# The second line contains the width, max_width.

# Constraints
# 0 < len(string) <= 1000
# 0 < max_width < len(string)

# Sample Input 0
# ABCDEFGHIJKLIMNOQRSTUVWXYZ
# 4

# Sample Output 0
# ABCD
# EFGH
# IJKL
# IMNO
# QRST
# UVWX
# YZ


import textwrap


def wrap(string, max_width):
    result = ""
    for x in textwrap.wrap(string, max_width):
        result = result + x + "\n"
    return result


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
