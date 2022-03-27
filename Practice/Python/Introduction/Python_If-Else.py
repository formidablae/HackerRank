# Task
# Given an integer, , perform the following conditional actions:
# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird

# Input Format
# A single line containing a positive integer, n.

# Constraints
# 1 <= n <= 100

# Output Format
# Print Weird if the number is weird. Otherwise, print Not Weird.

# Sample Input 0
# 3

# Sample Output 0
# Weird

# Explanation 0
# n = 3
# n is odd and odd numbers are weird, so print Weird.

# Sample Input 1
# 24

# Sample Output 1
# Not Weird

# Explanation 1
# n = 24
# n > 20 and is even, so it is not weird.

def main():
    n = int(input())
    if n % 2 == 1:
        print('Weird')
    elif (n >= 2 and n <= 5):
        print('Not Weird')
    elif (n >= 6 and n <= 20):
        print('Weird')
    else:
        print('Not Weird')

if __name__ == '__main__':
    main()
