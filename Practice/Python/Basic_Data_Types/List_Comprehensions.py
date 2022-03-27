# Let's learn about list comprehensions!
# You are given three integers x, y and z representing the dimensions
# of a cuboid along with an integer n.
# Print a list of all possible coordinates given by (i, j, k) on a 3D grid
# where the sum of i + j + k is not equal to n.
# Here, 0 <= i <= x; 0 <= j <= y; 0 <= k <= z.
# Please use list comprehensions rather than multiple loops, as a learning exercise.

# Example
# x = 1
# y = 1
# z = 2
# n = 3

# All permutations of [i, j, k] are:
# [
#   [0, 0, 0],
#   [0, 0, 1],
#   [0, 0, 2],
#   [0, 1, 0],
#   [0, 1, 1],
#   [0, 1, 2],
#   [1, 0, 0],
#   [1, 0, 1],
#   [1, 0, 2],
#   [1, 1, 0],
#   [1, 1, 1],
#   [1, 1, 2],
# ].

# Print an array of the elements that do not sum to n = 3.
# [
#   [0, 0, 0],
#   [0, 0, 1],
#   [0, 0, 2],
#   [0, 1, 0],
#   [0, 1, 1],
#   [1, 0, 0],
#   [1, 0, 1],
#   [1, 1, 0],
#   [1, 1, 2],
# ].

# Input Format
# Four integers x, y, z and n, each on a separate line.

# Constraints
# Print the list in lexicographic increasing order.

# Sample Input 0
# 1
# 1
# 1
# 2

# Sample Output 0
# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

# Explanation 0
# Each variable and will have values of 0 or 1.
# All permutations of lists in the form
# [i, j, k] = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 1, 0], [1, 1, 1]].
# Remove all arrays that sum to 2 to leave only the valid permutations.

# Sample Input 1
# 2
# 2
# 2
# 2

# Sample Output 1
# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1], [0, 2, 2], [1, 0, 0], [1, 0, 2], [1, 1, 1], [1, 1, 2], [1, 2, 0], [1, 2, 1], [1, 2, 2], [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2]]


def print_cuboid_coords(x, y, z, n):
    cuboid = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
    print(cuboid)


def main():
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print_cuboid_coords(x, y, z, n)


if __name__ == '__main__':
    main()
