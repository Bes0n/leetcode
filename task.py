#!/usr/bin/python3.10
from collections import defaultdict

s = "Let's take LeetCode contest"

def reverseWords(s):
    n = s.split()
    for c in n:
        s = " ".join([c[::-1]])
    
    print(s)

reverseWords(s)