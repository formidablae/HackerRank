# You are given an integer, N.
# Your task is to print an alphabet rangoli of size N.
# (Rangoli is a form of Indian folk art based on creation of patterns.)

# Different sizes of alphabet rangoli are shown below:

# #size 3

# ----c----
# --c-b-c--
# c-b-a-b-c
# --c-b-c--
# ----c----

# #size 5

# --------e--------
# ------e-d-e------
# ----e-d-c-d-e----
# --e-d-c-b-c-d-e--
# e-d-c-b-a-b-c-d-e
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# --------e--------

# #size 10

# ------------------j------------------
# ----------------j-i-j----------------
# --------------j-i-h-i-j--------------
# ------------j-i-h-g-h-i-j------------
# ----------j-i-h-g-f-g-h-i-j----------
# --------j-i-h-g-f-e-f-g-h-i-j--------
# ------j-i-h-g-f-e-d-e-f-g-h-i-j------
# ----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
# --j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
# j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
# --j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
# ----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
# ------j-i-h-g-f-e-d-e-f-g-h-i-j------
# --------j-i-h-g-f-e-f-g-h-i-j--------
# ----------j-i-h-g-f-g-h-i-j----------
# ------------j-i-h-g-h-i-j------------
# --------------j-i-h-i-j--------------
# ----------------j-i-j----------------
# ------------------j------------------

# The center of the rangoli has the first alphabet letter a,
# and the boundary has the Nth alphabet letter (in alphabetical order).

# Function Description
# Complete the rangoli function in the editor below.

# rangoli has the following parameters:
# int size: the size of the rangoli

# Returns
# string: a single string made up of each of the lines
# of the rangoli separated by a newline character (\n)

# Input Format
# Only one line of input containing size, the size of the rangoli.

# Constraints
# 0 < size < 27

# Sample Input
# 5

# Sample Output
# --------e--------
# ------e-d-e------
# ----e-d-c-d-e----
# --e-d-c-b-c-d-e--
# e-d-c-b-a-b-c-d-e
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# --------e--------


def print_rangoli(size):
    # your code goes here
    theSize = size
    alph = "abcdefghijklmnopqrstuvwxyz"
    spaces = "----------------------------------------------------"
    row = ""
    row = row + spaces[0:(size - 1) * 2]
    row = row + alph[size - 1]
    row = row + spaces[0:(size - 1) * 2]
    previousRow = row

    for i in range(size - 1, 0, -1):
        newRow = ""
        newRow = previousRow[2:(size - 1) * 2 + 2]
        newRow = newRow + alph[i - 1]
        newRow = newRow + previousRow[(size - 1) * 2 - 1:-2]
        if i == 1:
            row = row + "\n" + newRow + "\n" + row[::-1]
        else:
            row = row + "\n" + newRow
            previousRow = newRow

    print(row)


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
