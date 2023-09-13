#!/usr/bin/python3.10
from collections import defaultdict

s = "a-bC-dj"

def reverseWords(s):
    left, right = 0, len(s) - 1
    s = list(s)
    while left < right:
        if s[left].isalpha() == True and s[right].isalpha() == True:
            s[left], s[right] = s[right], s[left]
        left, right = left + 1, right - 1
    return ''.join(s)

print(reverseWords(s))