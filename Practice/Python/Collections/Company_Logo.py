# A newly opened multinational brand has decided to base their
# company logo on the three most common characters in the company name.
# They are now trying out various combinations of company names
# and logos based on this condition. Given a string s,
# which is the company name in lowercase letters,
# your task is to find the top three most common characters in the string.

# Print the three most common characters along with their occurrence count.
# Sort in descending order of occurrence count.
# If the occurrence count is the same,
# sort the characters in alphabetical order.

# For example, according to the conditions described above,
# GOOGLE would have it's logo with the letters G, O, E.

# Input Format
# A single line of input containing the string S.

# Constraints
# 0 < len(S) <= 10^4
# S has at least 3 distinct characters

# Output Format
# Print the three most common characters along with
# their occurrence count each on a separate line.
# Sort output in descending order of occurrence count.
# If the occurrence count is the same,
# sort the characters in alphabetical order.

# Sample Input 0
# aabbbccde

# Sample Output 0
# b 3
# a 2
# c 2

# Explanation 0
# aabbbccde
# Here, b occurs 3 times. It is printed first.
# Both a and c occur 2 times. So, a is printed in the second line
# and c in the third line because a comes before c in the alphabet.

# Note: The string S has at least 3 distinct characters.


#!/bin/python3

import math
import os
import random
import re
import sys
from collections import OrderedDict


if __name__ == '__main__':
    s = input()
    dictOfLetters = OrderedDict()

    for i in range(0, len(s)):
        
        if s[i] not in dictOfLetters.keys():
            dictOfLetters.update({s[i] : 1})
            continue
        dictOfLetters[s[i]] += 1
    
    result = ""
    printed = 0
    for key, value in sorted(dictOfLetters.items(), key=lambda x: (-x[1], x[0])):
        if printed < 3:
            result = result + key + " " + str(value) + "\n"
            printed += 1
        else:
            break

    print(result)
